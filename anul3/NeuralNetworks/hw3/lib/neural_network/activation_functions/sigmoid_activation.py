import numpy as np
from .abstract_activation import AbstractActivationFunction

class SigmoidActivationFunction(AbstractActivationFunction):
    """Sigmoid activation function."""
    @staticmethod
    def func(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def derivative(x):
        y = SigmoidActivationFunction.func(x)
        return y * (1 - y)