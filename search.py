from bs4 import BeautifulSoup
import requests
from book import books
from selenium import webdriver
import time
import re
import sys


def search(book_name,book):
    url = "https://www.pdfdrive.com/search?q={}".format(book_name)
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'html5lib')
    results = soup.findAll('a', attrs = {'class': 'ai-search'})
    i = 1
    for result in results:
        title = result.find('h2').text
        link = result['href']
        book.add(i,title,link)
        i += 1
    return book.get_results()

def download(title,url):
    url = ("https://www.pdfdrive.com"+url)
    source = requests.get(url)
    soup = BeautifulSoup(source.content,'html5lib')
    results = soup.find('a',attrs = {'id':'download-button-link'})
    link = results['href']
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("/usr/lib/chromium/chromedriver", options=chrome_options)
    driver.get("https://www.pdfdrive.com"+link)
    html = driver.page_source
    soup = BeautifulSoup(html,'html5lib')
    button = soup.find('a',attrs = {'onclick':re.compile('AiD(.*)')})

    try:
        link = re.findall('http(.*)',button['href'])
        pdf = "http"+link[0]
    except:
        pdf = "https://www.pdfdrive.com"+button['href']
        #book = requests.get(pdf, allow_redirects=True)
        #open('/home/kaushalp/Books/{}.pdf'.format(title), 'wb').write(book.content)
    save(title, pdf)

def save(title, url):
    try:
        extension = re.findall('.*ext=(.*)',url)
        extension = '.' + extension[0].strip(' ')
    except:
        extension = ".pdf"
    filename = f"/home/kaushal/Downloads/{title + extension}"
    print(extension)
    with open(filename, 'wb') as f:
        try:
            response = requests.get(url, stream = True)
        except:
            print("file not found!")
        total = response.headers.get('content-length')
        size = int(total) / (1024 * 1024)
        size = round(size, 2)
        if total is None:
            f.write(response.content)
        else:
            print(url)
            print(f"Downloading {title} of size {size}")
            downloaded = 0
            total = int(total)
            chunk = max(int(total / 1000), 1024 * 1024)
            for data in response.iter_content(chunk_size = chunk):
                downloaded += len(data)
                f.write(data)
                done = int(50 * downloaded / total)
                sys.stdout.write("\r[{}{}]".format('#' * done, '.' * (50 - done)))
                sys.stdout.flush()
    sys.stdout.write('\n')


    

if __name__ == '__main__':
    obj = books()
    book_name = input("Enter book name")
    result = search(book_name,obj)
    response = 0
    while(True):
        obj.show_results()
        response = input("Select:")
        if(response != '0'):
            break
    url = obj.get_url(int(response))
    title = obj.get_title(int(response))
    download(title,url)