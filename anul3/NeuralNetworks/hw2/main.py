import multiprocessing
import numpy as np

from lib.utils import InputReader
from lib.neural_network import Perceptron

train_set, valid_set, test_set = InputReader('mnist.pkl.gz').read()


def check_number(all_perceptrons, image, label):
    guess = -1
    max_chance = -1
    chance_for_correct_label = 0
    for idx, perceptron in enumerate(all_perceptrons):
        chance, is_ok = perceptron.multiple_output(image)

        if is_ok == 1 and chance > max_chance:
            max_chance = chance
            guess = idx

        if idx == label:
            chance_for_correct_label = chance
    
    if label == guess:
        # print(f"Found digit {label} with accuracy {max_chance}%")
        return True
    if guess == -1:
        return False
    print(f"Failed to find digit {label}. Accuracy for label was {chance_for_correct_label} while we found {max_chance}% for {guess}")
    return False

def train_perceptron(perceptron):
    perceptron.run()

all_perceptrons = []
jobs = []


for idx in range(10):
    print(f"Training for {idx}")
    perceptron = Perceptron(train_set, epoch=5, aim=idx, learning_rate=0.001)
    perceptron.run()
    print(f"Accuracy for perceptron {perceptron.aim} valid_set is: {perceptron.accuracy(valid_set)}")
    print(f"Accuracy for perceptron {perceptron.aim} test_set is: {perceptron.accuracy(test_set)}")
    all_perceptrons.append(perceptron)

images, labels = test_set

accuracy = 0
for idx in range(labels.shape[0]):
    image, label = (images[idx], labels[idx])
    accuracy += check_number(all_perceptrons, image, label)

print(f"Algorithm accuracy is: {accuracy/labels.shape[0]}")