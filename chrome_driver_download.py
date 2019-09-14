import requests
from bs4 import BeautifulSoup
import zipfile
import os
import argparse

def main(args):

    file_name = 'chromedriver_win32.zip'
    if args.l:
        file_name = 'chromedriver_linux64.zip'
    if args.m:
        file_name = 'chromedriver_mac64.zip'
    
    download_url = 'https://chromedriver.storage.googleapis.com/'
    latest_release = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'

    s = requests.session()
    r = s.get(latest_release)
    version = r.content.decode("utf-8").strip()
    download_url = download_url + version + '/' + file_name 
    r = s.get(download_url)
    with open(file_name, 'wb') as f:
        f.write(r.content)
    s.close()
    zip_ref = zipfile.ZipFile(file_name, 'r')
    zip_ref.extractall('.')
    zip_ref.close()
    os.remove(file_name)

parser = argparse.ArgumentParser()
parser.add_argument("-w", 
                    default=True,
                    action='store_true',
                    help="Windows")
parser.add_argument("-l", 
                    default=False,
                    action='store_true',
                    help="Linux")
parser.add_argument("-m", 
                    default=False,
                    action='store_true',
                    help="OSX")
args = parser.parse_args()
main(args)

