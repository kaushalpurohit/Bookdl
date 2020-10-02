import logging
import os

class logger:
    def __init__(self):
        path = os.path.expanduser("~") + '/.cache/Bookdl'
        file = "bookdl.log"
        if not os.path.exists(path):
            os.makedirs(path)
            path = os.path.join(path, file)
        else:
            path = os.path.join(path, file)
        logging.basicConfig(filename = path, 
                            format = "[%(levelname)s] %(asctime)s %(message)s",
                            filemode = "w", level = logging.DEBUG)
        logging.getLogger('requests').setLevel(logging.WARNING)
        logging.getLogger('urllib3.connectionpool').setLevel(logging.WARNING)
        logging.getLogger('selenium').setLevel(logging.WARNING)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
    
    def debug(self, message):
        self.logger.debug(message)
    
    def info(self, message):
        self.logger.info(message)
        print(message)
    
    def warning(self, message):
        self.logger.warning(message)
        self.console_message(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def critical(self,message):
        self.logger.critical(message)
    
    def console_message(self, message):
        print(message)