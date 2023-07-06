import numpy as np

class MSELossFunction:
    @staticmethod
    def loss(y_true, y_pred):
        return np.mean(np.power(y_true - y_pred, 2));

    @staticmethod
    def loss_derivative(y_true, y_pred):
        return 2 * (y_pred - y_true) / y_true.size

class CrossEntropyLossFunction:
    @staticmethod
    def loss(y_true, y_pred):
        y_pred_temp = np.copy(y_pred)
        y_pred_temp -= y_pred.max(keepdims = True)
        probs = np.exp(y_pred)/np.sum(np.exp(y_pred), keepdims = True)

        y_true_pos = np.argmax(y_true, axis = 1)[0]
        loss = -np.log(probs[0][y_true_pos])
        loss = np.sum(loss)
        
        y_pred[0][y_true_pos] -= 1
        
        return loss

    @staticmethod
    def loss_derivative(y_true, y_pred):
        y_true_pos = np.argmax(y_true, axis = 1)
        y_pred[0][y_true_pos] -=  1
        return y_pred