from bs4 import BeautifulSoup
import requests
from book import books

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

if __name__ == '__main__':
    obj = books()
    book_name = input("Enter book name")
    result = search(book_name,obj)
    i = 1
    while(i < 4):
        obj.show_results(i)
        response = input("Select:")
        if(response != '0'):
            print("Downloading")
        else:
            i = i+1
