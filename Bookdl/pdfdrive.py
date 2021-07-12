''' Contains functions to search and download the book '''

import sys
import re
import cloudscraper
from bs4 import BeautifulSoup
from termcolor import colored
from . import books, save
from . import logger

logger = logger.logger()
scraper = cloudscraper.create_scraper()

def search(book_name, book):
    '''
    Function to search for related books and save the
    results in books dictionary
    '''

    print("searching for " + colored(book_name, "green", attrs=['bold']))
    url = "https://www.pdfdrive.com/search?q={}".format(book_name)
    source = scraper.get(url)
    soup = BeautifulSoup(source.content, 'html5lib')
    results = soup.findAll('a', attrs={'class': 'ai-search'})

    for i, result in enumerate(results):
        title = result.find('h2').text
        link = result['href']
        book.add(i, title, link)


def download(title, url, ext):
    '''Using selenium driver here to get the download link.'''

    url = "https://www.pdfdrive.com" + url
    resp = scraper.get(url)
    soup = BeautifulSoup(resp.content, 'html5lib')

    bookId = soup.find('button', attrs={'id': 'previewButtonMain'})['data-id']
    session = re.findall(r'session=(.+?)"', str(soup))[0]
    logger.debug(bookId)
    logger.debug(session)

    url = "https://www.pdfdrive.com/download.pdf"
    parameters = {'id': bookId, 'h': session, 'ext': ext}
    save.save(title, url, parameters)
