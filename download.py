# downloading with requests
# import the requests library
from tqdm import tqdm
import requests

# url1 = 'https://minjust.gov.ua/files/general/2021/08/30/20210830183442-76.zip'
# url2 = 'https://minjust.gov.ua/files/general/2020/09/05/20200905170019-89.zip'


def download_zips(url, dir_to_save):
    # Streaming, so we can iterate over the response.
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 KB
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc='Uploading...')
    print('\nUpload file: ', dir_to_save)
    with open(dir_to_save, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
    return dir_to_save

#
# if __name__ == '__main__':
#     download_zips(url1, 'minjust_info.zip')
#     download_zips(url2, 'minjust_structure.zip')
