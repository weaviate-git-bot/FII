import logging

from typing import List
class Logger:
    """
    Use this class to log any action you may need.
    """
    __INSTANCE__ = None
    LEVEL = logging.INFO
    
    def __init__(self, file_name: str = 'sniff.log', logger_name: str = 'K9'):
        if Logger.__INSTANCE__ is not None:
            raise Exception('This class must be a singleton')

        self.__file_name = file_name 
        self.__logger_name = logger_name
        self.__handlers = []
        self.logger = None

        handlers = ['file', 'syslog']
        self.__add_handlers(handlers)

        self.__build_logger()

        Logger.__INSTANCE__ = self

    @staticmethod
    def get_logger() -> logging.Logger:
        """
        Get the logger instance.
        """
        if Logger.__INSTANCE__ is None:
            Logger()
        
        return Logger.__INSTANCE__.logger

    def __build_logger(self):
        """
        Build the logger with handlers and formatter
        """
        self.logger = logging.getLogger(self.__logger_name)
        self.logger.setLevel(Logger.LEVEL)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s')

        self.__setup_handlers(formatter)

        for handler in self.__handlers:
            self.logger.addHandler(handler)

    def __setup_handlers(self, formatter: logging.Formatter):
        """
        Setup the handlers (setting logging level and formatter for each logger)
        """
        for handler in self.__handlers:
            handler.setLevel(Logger.LEVEL)
            handler.setFormatter(formatter)

    def __add_handlers(self, handlers: List[str]) -> None:
        """
        Adding all needed handlers for each stream
        """
        handler_mapping = {
            'file': logging.FileHandler(self.__file_name, 'w'),
            'syslog': logging.StreamHandler()       
        }

        for handler in handlers:
            h = handler_mapping.get(handler, None)
            if h is None:
                print(f'Warning: Handler {handler} not found')
                continue
            
            self.__handlers.append(h)