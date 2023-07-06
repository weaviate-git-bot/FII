from .state import State

class Validator:
    def __init__(self):
        pass


    def __str__(self):
        return self.__class__.__name__

    def validate(self, state: State) -> bool:
        pass