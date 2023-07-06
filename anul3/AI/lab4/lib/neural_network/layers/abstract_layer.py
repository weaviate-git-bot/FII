class AbstractLayer:
    def __init__(self):
        self.input = None
        self.output = None

    def forward_propagation(self, input):
        raise Exception('Not implemented FP')

    def backwards_propagation(self, output_error, learning_rate):
        raise Exception('Not implemented BP')