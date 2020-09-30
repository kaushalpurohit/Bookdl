from pdfdrive import search, download
from books import books

if __name__ == '__main__':
    obj = books()
    book_name = input("Enter a book name:")
    result = search(book_name,obj)
    response = 0
    while(True):
        obj.show_results()
        response = input("Enter choice:")
        if(response != '0'):
            break
    url = obj.get_url(int(response))
    title = obj.get_title(int(response))
    download(title,url)