''' Class to hold book data. '''

from termcolor import colored
from . import logger

logger = logger.logger()


class books:

    def __init__(self):
        self.dict = dict()
        self.itr = 1

    def add(self, index, title, link):
        self.dict[index] = {}
        self.dict[index]['Title'] = title
        self.dict[index]['Link'] = link

    def get_results(self):
        return self.dict

    def show_results(self):
        size = len(self.dict)
        last = self.itr + 5
        i = self.itr
        while i < last:
            try:
                title = self.dict[i]['Title']
                text = colored(title, 'yellow', attrs=['bold'])
                index = colored(f"[{i}]", "magenta", attrs=['bold'])
                print("{}.{}".format(index, text))
            except Exception as e:
                logger.debug(e)
                break
            i += 1
        if(i <= size):
            text = colored("more", "yellow", attrs=['bold'])
            index = colored("[0]", "magenta", attrs=['bold'])
            print("{} {}".format(index, text))
        self.itr = i

    def get_url(self, i):
        return self.dict[i]['Link']

    def get_title(self, i):
        return self.dict[i]['Title']
