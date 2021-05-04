''' Contains functions to search and download the book '''

import re
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from termcolor import colored
from . import save
from . import logger

logger = logger.logger()


def search(book_name, book):
    '''
    Function to search for related books and save the
    results in books dictionary
    '''

    print("searching for " + colored(book_name, "green", attrs=['bold']))
    book_name = quote_plus(book_name)
    url = "https://www.pdfdrive.com/search?q={}".format(book_name)
    print(url)

    # https://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    source = urlopen(req).read()
    # source = source.decode('utf-8')

    soup = BeautifulSoup(source, 'html5lib')
    results = soup.findAll('a', attrs={'class': 'ai-search'})

    for i, result in enumerate(results):
        title = result.find('h2').text
        link = result['href']
        book.add(i, title, link)


def download(title, url, ext):
    '''Using selenium driver here to get the download link.'''

    url = "https://www.pdfdrive.com" + url
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urlopen(req).read()
    soup = BeautifulSoup(resp, 'html5lib')

    bookId = soup.find('button', attrs={'id': 'previewButtonMain'})['data-id']
    session = re.findall(r'session=(.+?)"', str(soup))[0]
    logger.debug(bookId)
    logger.debug(session)

    url = "https://www.pdfdrive.com/download.pdf"
    parameters = {'id': bookId, 'h': session, 'ext': ext}
    save.save(title, url, parameters)
