from re import L
import numpy as np
import random

from typing import List

class Perceptron:
    def __init__(self, data_set, weights: List[int] = None, aim: int = 0, epoch: int = 100, learning_rate = 0.1):
        self.images = np.array(data_set[0])
        self.tags = data_set[1]
        self.bias = 0
        self.epoch = epoch
        self.aim = aim

        if weights is None:
            self.weights = np.zeros(self.images.shape[1])
        else:
            self.weights = weights

        self.learning_rate = learning_rate

    def update_set(self, data_set):
        self.images = np.array(data_set[0])
        self.tags = data_set[1]

    def learn(self):
        for idx in range(self.images.shape[0]):
            image = np.array(self.images[idx])
            label = self.tags[idx] == self.aim
            
            predictions = self.predict(image)

            self.update(label, image, predictions)

    def run(self):
        for epoch in range(self.epoch):
            print(f"Learning in epoch: {epoch}", end='\r')
            self.learn()
        print("\nFinished learning")

    def predict(self, image):
        out = np.dot(image, self.weights) + self.bias
        return self.activation_function(out)

    def multiple_output(self, image):
        out = np.dot(image, self.weights) + self.bias
        return (out, self.activation_function(out))

    def accuracy(self, model_set):
        aim_target = np.array([1 if x == 0 else 0 for x in model_set[1]])
        predictions = self.predict(model_set[0])

        correct = 0
        for idx in range(aim_target.shape[0]):
            if aim_target[idx] == predictions[idx]:
                correct += 1

        return correct/aim_target.shape[0]

    def update(self, label, image, predictions):
        update = self.learning_rate * (label - predictions)
        self.weights += update * image
        self.bias += update * 1

    def activation_function(self, z):
        return np.where(z >= 0, 1, 0)
