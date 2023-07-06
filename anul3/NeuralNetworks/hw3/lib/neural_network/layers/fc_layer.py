import numpy as np
from .abstract_layer import AbstractLayer

class FullyConnectedLayer(AbstractLayer):
    def __init__(self, input_size, output_size, weights = None, bias = None):
        self.weights = weights if weights is not None else np.random.rand(input_size, output_size) - 0.5
        self.bias = bias if bias is not None else np.random.rand(1, output_size) - 0.5

        self._gradients = 0
        self.decay = 0.9

    def forward_propagation(self, input_d):
        self.input = input_d
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output

    def backward_propagation(self, output_error, learning_rate):
        input_error = np.dot(output_error, self.weights.T)
        weights_error = np.dot(self.input.T, output_error)

        self.gradient_descend(weights_error, output_error, learning_rate)
        # self.RMSProp(weights_error, self.input, self.weights, learning_rate)
        return input_error

    def gradient_descend(self, weights_error, output_error, learning_rate):
        self.weights -= learning_rate * weights_error
        self.bias -= learning_rate * output_error

    def RMSProp(self, weights_error, layer_input, curr_weights, learning_rate):
        gradient = weights_error - learning_rate * curr_weights

        eps = 1e-8

        self._gradients = self.decay * self._gradients + (1-self.decay) * np.power(gradient,2)

        return curr_weights - learning_rate * gradient / (np.sqrt(self._gradients) + eps)
