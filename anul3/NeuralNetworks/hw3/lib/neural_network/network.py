import numpy as np
from .loss_function import MSELossFunction, CrossEntropyLossFunction

class NeuralNetwork:
    def __init__(self):
        self.layers = []
        self.loss_func = CrossEntropyLossFunction

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

    def transform_to_array(self, label):
        result = np.zeros(10)
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
            err /= samples
            print(f"[Epoch {epoch}] Computed Error: {err}")