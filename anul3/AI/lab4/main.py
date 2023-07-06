import numpy as np
import matplotlib.pyplot as plt
import time

from lib.utils import InputReader
from lib.neural_network import NeuralNetwork
from lib.neural_network.layers import FullyConnectedLayer, ActivationLayer
from lib.neural_network.activation_functions import SigmoidActivationFunction, SoftmaxActivationFunction


train_set, validation_set = InputReader('bezdekIris.data').read()
network = NeuralNetwork()
network.add_layer(FullyConnectedLayer(4, 10))
network.add_layer(ActivationLayer(SigmoidActivationFunction))
network.add_layer(FullyConnectedLayer(10, 3))
network.add_layer(ActivationLayer(SigmoidActivationFunction))

network.add_validation_set(validation_set)

network.fit(np.array(train_set[0]), np.array(train_set[1]), 100, 0.009)

print("\n")
print("-="*10 + "   Accuracy   " + "-="*10)
print(f"Algorithm at cross validation accuracy is: {network.get_accuracy(validation_set)}")

fig, alx = plt.subplots()
convergency = network.train_valid
alx.plot([i[0] for i in convergency], label="Training")
alx.plot([i[1] for i in convergency], label="Validation")
# alx.plot([i[1] for i in convergency], label="Validation accuracy")
plt.title('Convergency')
plt.legend()
plt.show()