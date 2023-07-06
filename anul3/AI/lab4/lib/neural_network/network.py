import numpy as np
from .loss_function import MSELossFunction, CrossEntropyLossFunction

class NeuralNetwork:
    def __init__(self):
        self.layers = []
        self.loss_func = CrossEntropyLossFunction
        self.validation_set = []
        self.convergency = []
        self.train_valid = []

    def add_validation_set(self, validation_set):
        self.validation_set = validation_set

    def add_convergency(self, error, accuracy):
        self.convergency.append([error, accuracy])

    def get_convergency(self):
        return self.convergency

    def valid_training(self, train, valid):
        self.train_valid.append([train, valid])

    def add_layer(self, layer):
        self.layers.append(layer)    

    def predict(self, input_data):
        # sample dimension first
        samples = len(input_data)
        result = []

        # run network over all samples
        for img in range(samples):
            # forward propagation
            output = np.array([input_data[img]])
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)

        return result

    def get_accuracy(self, dataset):
        images, labels = dataset
        accuracy = 0
        guesses = self.predict(images)
        for idx in range(len(guesses)):
            if np.argmax(guesses[idx]) == labels[idx]:
                accuracy += 1
        return accuracy/len(labels) * 100

    def transform_to_array(self, label):
        result = np.zeros(3)
        result[label] = 1
        return np.array([result])

    def fit(self, x_train, y_train, epochs, learning_rate):
        # sample dimension first
        samples = len(x_train)

        # training loop
        for epoch in range(epochs):
            err = 0
            for img in range(samples):
                print(f"[Epoch {epoch}] Image number: {img}",end='\r')
                
                # forward propagation
                output = np.array([x_train[img]])

                label = self.transform_to_array(y_train[img])

                for layer in self.layers:
                    output = layer.forward_propagation(output)

                err += self.loss_func.loss(label, output)

                # backward propagation
                error = self.loss_func.loss_derivative(label, output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, learning_rate)

            # calculate average error on all samples
            err /= samples * 100
            validation_accuracy = self.get_accuracy(self.validation_set)
            training_accuracy = self.get_accuracy([x_train, y_train])
            self.valid_training(training_accuracy, validation_accuracy)
            self.add_convergency(err*1000, validation_accuracy)
            print(f"[Epoch {epoch}] Computed Error: {err} | Validation accuracy: {validation_accuracy}%")