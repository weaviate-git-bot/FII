from .abstract_layer import AbstractLayer
from lib.neural_network.activation_functions import AbstractActivationFunction

class ActivationLayer(AbstractLayer):
    def __init__(self, activationFunc: AbstractActivationFunction):
        self.activation = activationFunc

    def forward_propagation(self, input_d):
        self.input = input_d
        self.output = self.activation.func(self.input)
        return self.output

    def backward_propagation(self, output_error, learning_rate):
        return self.activation.derivative(self.input) * output_error