class AbstractActivationFunction:
    """Abstract class for activation functions."""

    @staticmethod
    def func(x):
        """Activation function."""
        raise NotImplementedError

    def derivative(x):
        """Derivative of the activation function."""
        raise NotImplementedError
        