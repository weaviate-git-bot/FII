import tensorflow.keras as keras
from tensorflow.keras.layers import Dense

class CriticNetwork(keras.Model):
    def __init__(self, fc1_dim = 256, fc2_dim = 256):
        super(CriticNetwork, self).__init__()

        self.__keras_layers = [
            Dense(fc1_dim, activation='relu'),
            Dense(fc2_dim, activation='relu'),
            Dense(1, activation=None)
        ]

    def call(self, state):
        x = state
        for layer in self.__keras_layers:
            x = layer(x)
        return x