import errno
import os
import shutil
import zipfile
from tqdm import tqdm

TARGETDIR = os.getcwd()
zip_file1 = 'minjust_info.zip'
zip_file2 = 'minjust_structure.zip'

def unzip_file(target_dir, zip_files=(zip_file1, zip_file2)):
    for zf in zip_files:
        with open(zf, "rb") as zipsrc:
            zfile = zipfile.ZipFile(zipsrc)
            print(zf)
            for member in tqdm(zfile.infolist(), desc='Extracting...'):
               target_path = os.path.join(target_dir, member.filename)
               if target_path.endswith('/'):  # folder entry, create
                   try:
                       os.makedirs(target_path)
                   except (OSError, IOError) as err:
                       # Windows may complain if the folders already exist
                       if err.errno != errno.EEXIST:
                           raise
                   continue
               with open(target_path, 'wb') as outfile, zfile.open(member) as infile:
                   shutil.copyfileobj(infile, outfile)


if __name__ == '__main__':
    unzip_file(TARGETDIR)
