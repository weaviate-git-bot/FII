import os
import numpy as np
import csv
import random

from typing import List

class InputReader:

    def __init__(self, path: str):
        self.__path = os.path.join(os.getcwd(), path)

    def __transform_to_array(self, label: str):
        return {
            'Iris-setosa': 0,
            'Iris-versicolor': 1,
            'Iris-virginica': 2,
        }[label]

    def read(self) -> List:
        data = []
        labels = []
        with open(self.__path) as fd:
            reader = csv.reader(fd,delimiter=',')
            for row in reader:
                if len(row) != 5:
                    continue
                
                data.append(np.array([float(x) for x in row[0:4]], dtype='float64'))
                labels.append(row[4])
        
        labels = [self.__transform_to_array(label) for label in labels]
        c = list(zip(data, labels))
        random.shuffle(c)
        data, labels = zip(*c)

        train_size = int(len(data)*0.8)
        train_set = data[:train_size], labels[:train_size]
        validation_set = data[train_size:], labels[train_size:]
        return train_set, validation_set