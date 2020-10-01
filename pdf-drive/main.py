import argparse
import sys
from logger import logger
from pdfdrive import search, download
from books import books

logger = logger()
parser = argparse.ArgumentParser(description = 'A Program to download books from pdf-drive.')

parser.add_argument("Book_name", type = str, help = "Book name to search for")
args = parser.parse_args()

def main():
    obj = books()
    search(args.Book_name,obj)
    response = 0
    while(True):
        obj.show_results()
        response = input("Enter choice:")
        if(response != '0'):
            break
    url = obj.get_url(int(response))
    title = obj.get_title(int(response))
    download(title,url)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\nExiting...")
        sys.exit()