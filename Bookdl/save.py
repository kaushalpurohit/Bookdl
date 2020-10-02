import requests
import re
import sys
import os
from . import logger
from termcolor import colored

logger = logger.logger()

def save(title, url):
    '''Function to save the file in downloads directory.'''

    try:
        extension = re.findall('.*ext=(.*)',url)
        extension = '.' + extension[0].strip(' ')
    except:
        extension = ".pdf"

    home = os.path.expanduser("~")
    logger.debug(home)
    path = os.path.join(home, "Downloads/") + title + extension

    if check(path):
        with open(path, 'wb') as f:
            try:
                response = requests.get(url, stream = True)
            except:
                print("file not found!")
                sys.exit()

            total = response.headers.get('content-length')
            size = int(total) / (1024 * 1024)
            size = round(size, 2)
            if total is None:
                f.write(response.content)
            else:
                progress_bar(title, total, path, response, f)
    else:
        logger.info("No changes were made.")

def progress_bar(title, total, path, response, f):
    '''Function to display the progress of download'''

    print(f"Downloading {colored(title, 'green', attrs = ['bold'])}")
    logger.info(f"saving the file to: {path}")

    downloaded = 0
    total = int(total)
    chunk = max(int(total / 1000), 1024 * 1024)
    for data in response.iter_content(chunk_size = chunk):
        downloaded += len(data)
        f.write(data)
        done = int(50 * downloaded / total)
        sys.stdout.write(colored("\r|{}{}|".format('▇' * done, '░' * (50 - done)),"cyan") + f"{done * 2}%")
        sys.stdout.flush()

    sys.stdout.write('\n')
    logger.info("File saved.")

def check(path):
    if os.path.exists(path):
        logger.warning("File already exists! Do you want to overwrite it?(y/n)")
        choice = input()
        return True if choice == 'y' else False