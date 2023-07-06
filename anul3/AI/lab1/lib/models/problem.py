from lib.models import State

class Problem:
    def __init__(self) -> None:
        pass

    def get_initial_state(self) -> State:
        pass

    def is_final_state(self, state: State) -> bool:
        pass

    def is_solvable(self) -> bool:
        pass