import numpy as np
from .abstract_activation import AbstractActivationFunction

class SoftmaxActivationFunction(AbstractActivationFunction):
    """Softmax activation function."""
    @staticmethod
    def func(x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    @staticmethod
    def derivative(x):
        """
        This function will be used to calcule the derivative of softmax function.
        """
        sm = x.reshape((-1,1))
        jac = np.diagflat(x) - np.dot(sm, sm.T)
        # print(x.shape, jac.shape, sum(jac))
        return sum(jac)