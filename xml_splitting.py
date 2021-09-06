import os
import shutil
dir_minjust_info = '/home/diakap/PycharmProjects/XML_S3/17-ufop_full_30.08.2021'
dir_minjust_structure = '/home/diakap/PycharmProjects/XML_S3/20200120143151-17_refresh/20200120143151-17_refresh'

smallfile = None
os.makedirs('result', exist_ok=True)


def splitter(which_list: str, dir_minjust_info, dir_minjust_structure, lines_per_file=20000):
    # create dict of pathes for split uo and fop files
    smallfile = None
    only_files_info = []
    only_files_struct = []

    for path in os.listdir(dir_minjust_info):
        full_path = os.path.join(dir_minjust_info, path)
        if os.path.isfile(full_path):
            only_files_info.append(full_path)
    for path in os.listdir(dir_minjust_structure):
        full_path = os.path.join(dir_minjust_structure, path)
        if os.path.isfile(full_path):
            only_files_struct.append(full_path)

    uo_dict = {}
    fop_dict = {}
    for il in only_files_info:
        if '_UO_' in il:
            uo_dict['info'] = il
        elif '_FOP_' in il:
            fop_dict['info'] = il
    for sl in only_files_struct:
        if '_UO_' in sl:
            uo_dict['struct'] = sl
        elif '_FOP_' in sl:
            fop_dict['struct'] = sl

    if which_list == 'uo':
        print('Makes UO split')
        dir_target = '/home/diakap/PycharmProjects/XML_S3/result/' + which_list
        os.makedirs(dir_target, exist_ok=True)
        dict_path = uo_dict
        head, tail = os.path.split(dict_path['struct'])
        shutil.copyfile(dict_path['struct'], '/'.join([dir_target, tail]))
        xml_file = dict_path['info']
        lines_per_file = 20000
        with open(xml_file, encoding='windows-1251') as bigfile:
            for lineno, line in enumerate(bigfile):
                if lineno == 0:
                    line_enc = line
                if lineno == 1:
                    line_ver = line
                if lines_per_file == lineno + lines_per_file:
                    if lineno % lines_per_file == 0:
                        if smallfile:
                            smallfile.write('</DATA>')
                            smallfile.close()
                        small_filename = which_list.upper() + '_XML_EDR_FULL_30.08.2021_{}_{}.xml'.format(lineno, lineno + lines_per_file)
                        small_folder = dir_target + '/' + small_filename[:-4]
                        os.makedirs(small_folder, exist_ok=True)
                        smallfile = open('/'.join([small_folder, small_filename]), "w", encoding='windows-1251')

                    smallfile.write(line)
                else:
                    if lineno % lines_per_file == 0:
                        if smallfile:
                            smallfile.write('</DATA>')
                            smallfile.close()
                        small_filename = which_list.upper() + '_XML_EDR_FULL_30.08.2021_{}_{}.xml'.format(lineno, lineno + lines_per_file)
                        small_folder = dir_target + '/' + small_filename[:-4]
                        os.makedirs(small_folder, exist_ok=True)
                        smallfile = open('/'.join([small_folder, small_filename]), "w", encoding='windows-1251')
                        shutil.copyfile(dict_path['struct'], '/'.join([small_folder, tail]))
                        smallfile.write(line_enc)
                        smallfile.write(line_ver)
                    smallfile.write(line)

            if smallfile:
                smallfile.close()

    elif which_list == 'fop':
        print('Makes FOP split')
        dir_target = '/home/diakap/PycharmProjects/XML_S3/result/' + which_list
        os.makedirs(dir_target, exist_ok=True)
        dict_path = fop_dict
        head, tail = os.path.split(dict_path['struct'])
        shutil.copyfile(dict_path['struct'], '/'.join([dir_target, tail]))
        xml_file = dict_path['info']
        lines_per_file = 20000
        with open(xml_file, encoding='windows-1251') as bigfile:
            for lineno, line in enumerate(bigfile):
                if lineno == 0:
                    line_enc = line
                if lineno == 1:
                    line_ver = line
                if lines_per_file == lineno + lines_per_file:
                    if lineno % lines_per_file == 0:
                        if smallfile:
                            smallfile.write('</DATA>')
                            smallfile.close()
                        small_filename = which_list.upper() + '_XML_EDR_FULL_30.08.2021_{}_{}.xml'.format(lineno, lineno + lines_per_file)
                        small_folder = dir_target + '/' + small_filename[:-4]
                        os.makedirs(small_folder, exist_ok=True)
                        smallfile = open('/'.join([small_folder, small_filename]), "w", encoding='windows-1251')
                        shutil.copyfile(dict_path['struct'], '/'.join([small_folder, tail]))
                    smallfile.write(line)
                else:
                    if lineno % lines_per_file == 0:
                        if smallfile:
                            smallfile.write('</DATA>')
                            smallfile.close()
                        small_filename = which_list.upper() + '_XML_EDR_FULL_30.08.2021_{}_{}.xml'.format(lineno, lineno + lines_per_file)
                        small_folder = dir_target + '/' + small_filename[:-4]
                        os.makedirs(small_folder, exist_ok=True)
                        smallfile = open('/'.join([small_folder, small_filename]), "w", encoding='windows-1251')
                        shutil.copyfile(dict_path['struct'], '/'.join([small_folder, tail]))
                        smallfile.write(line_enc)
                        smallfile.write(line_ver)
                    smallfile.write(line)

            if smallfile:
                smallfile.close()


if __name__ == '__main__':
    splitter(which_list='uo', dir_minjust_info=dir_minjust_info,
             dir_minjust_structure=dir_minjust_structure)
    splitter(which_list='fop', dir_minjust_info=dir_minjust_info,
             dir_minjust_structure=dir_minjust_structure)