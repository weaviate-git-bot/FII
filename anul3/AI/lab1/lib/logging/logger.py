import logging

class LoggerBuilder:
    __handlers = []
    __INSTANCE = None

    def __init__(self, filename: str = '', logger_name: str = 'ai-lab1'):
        if LoggerBuilder.__INSTANCE is not None:
            raise Exception('LoggerBuilder is a singleton class.')
        
        self.__filename = filename
        self.__logger_name = logger_name
        self.__handlers.append(logging.StreamHandler())

        self.__get_logger()
        LoggerBuilder.__INSTANCE = self

    @staticmethod
    def get_instance() -> 'LoggerBuilder':
        if LoggerBuilder.__INSTANCE is None:
            LoggerBuilder()
        return LoggerBuilder.__INSTANCE

    @property
    def logger(self) -> logging.Logger:
        return self.__current_logger

    @staticmethod
    def get_logger() -> logging.Logger:
        if LoggerBuilder.__INSTANCE is None:
            LoggerBuilder()
        return LoggerBuilder.__INSTANCE.logger

    def __get_logger(self) -> logging.Logger:
        self.__current_logger = logging.getLogger(self.__logger_name)
        self.__current_logger.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s "
                                      "- %(message)s")

        self.__setup_logger_handlers(self.__handlers, formatter)
        self.__add_logger_handlers(self.__current_logger, self.__handlers)

        return self.__current_logger

    def __setup_logger_handlers(self, handlers: list, formatter: logging.Formatter) -> None:
        for handler in handlers:
            handler.setLevel(logging.INFO)
            handler.setFormatter(formatter)

    def __add_logger_handlers(self, destination_logger: logging.Logger, handlers: list) -> None:
        for handler in handlers:
            destination_logger.addHandler(handler)