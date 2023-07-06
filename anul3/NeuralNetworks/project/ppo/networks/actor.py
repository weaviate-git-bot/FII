import numpy as np
import tensorflow.keras as keras
from tensorflow.keras.layers import Dense

class ActorNetwork(keras.Model):
    def __init__(self, n_actions, fc1_dim = 256, fc2_dim = 256):
        super(ActorNetwork, self).__init__()
        self.__keras_layers = [
            Dense(fc1_dim, activation='relu'),
            Dense(fc2_dim, activation='relu'),
            Dense(n_actions, activation='softmax')
        ]

    def call(self, state):
        x = state
        for layer in self.__keras_layers:
            x = layer(x)

        return x