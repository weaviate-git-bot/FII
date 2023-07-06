import numpy as np

from lib.utils import InputReader
from lib.neural_network import NeuralNetwork
from lib.neural_network.layers import FullyConnectedLayer, ActivationLayer
from lib.neural_network.activation_functions import SigmoidActivationFunction, SoftmaxActivationFunction

def compute_accuracy(network, dataset):
    images, labels = dataset
    accuracy = 0
    guesses = network.predict(images)
    for idx in range(len(guesses)):
        if np.argmax(guesses[idx]) == labels[idx]:
            accuracy += 1
    return accuracy/labels.shape[0] * 100

train_set, valid_set, test_set = InputReader('mnist.pkl.gz').read()

network = NeuralNetwork()
network.add_layer(FullyConnectedLayer(784, 100))
network.add_layer(ActivationLayer(SigmoidActivationFunction))
network.add_layer(FullyConnectedLayer(100, 10))
network.add_layer(ActivationLayer(SigmoidActivationFunction))

network.fit(np.array(train_set[0]), np.array(train_set[1]), 30, 0.01)

print("\n")
print("-="*10 + "   Accuracy   " + "-="*10)
print(f"Algorithm at cross validation accuracy is: {compute_accuracy(network, valid_set)}")
print(f"Algorithm at testing is: {compute_accuracy(network, test_set)}")
