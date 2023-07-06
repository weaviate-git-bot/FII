import os
import pickle
import gzip

from typing import List

class InputReader:

    def __init__(self, path: str):
        self.__path = os.path.join(os.getcwd(), path)

    def read(self) -> List:
        with gzip.open(self.__path, 'rb') as fd:
            return pickle.load(fd, encoding='latin')
