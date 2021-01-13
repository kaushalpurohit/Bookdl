''' Contains functions to search and download the book '''

from selenium import webdriver
from bs4 import BeautifulSoup
from . import books, save
from termcolor import colored
from . import logger
import sys
import requests
import re

logger = logger.logger()


def search(book_name, book):
    '''
    Function to search for related books and save the
    results in books dictionary
    '''

    print("searching for " + colored(book_name, "green", attrs=['bold']))
    url = "https://www.pdfdrive.com/search?q={}".format(book_name)
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'html5lib')
    results = soup.findAll('a', attrs={'class': 'ai-search'})
    i = 1
    for result in results:
        title = result.find('h2').text
        link = result['href']
        book.add(i, title, link)
        i += 1


def download(title, url):
    '''Using selenium driver here to get the download link.'''

    url = "https://www.pdfdrive.com" + url
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'html5lib')
    results = soup.find('a', attrs={'id': 'download-button-link'})
    link = results['href']
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver_path = "/usr/lib/chromium/chromedriver"
    driver = webdriver.Chrome(driver_path, options=chrome_options)
    driver.get("https://www.pdfdrive.com" + link)
    driver.set_page_load_timeout(10)
    driver.set_script_timeout(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html5lib')
    button = soup.find('a', attrs={'onclick': re.compile('AiD(.*)')})
    if button is not None:
        try:
            link = re.findall('http(.*)', button['href'])
            pdf = "http" + link[0]
        except Exception as e:
            logger.debug(e)
            pdf = "https://www.pdfdrive.com" + button['href']
        save.save(title, pdf)
    else:
        print("Book not found!")
        print("Exiting...")
        sys.exit()
