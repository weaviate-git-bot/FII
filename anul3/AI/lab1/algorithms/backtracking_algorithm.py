from queue import LifoQueue
from typing import List
from copy import deepcopy

from lib.models import State, Problem


from .default_algorithm import DefaultAlgorithm

class BacktrackingAlgorithm(DefaultAlgorithm):
    def __init__(self, problem: Problem):
        super().__init__(problem)

    def solve(self):
        self.logger.info("Started backtracking algorithm")

        visited = dict()
        stack = LifoQueue()

        initial_state = self.problem.get_initial_state()
        initial_state.set_path([])
        stack.put(initial_state)

        while not stack.empty():
            ct: State = stack.get()
            transition_hash = self.__compute_unique(ct)
            if transition_hash in visited:
                self.logger.debug("Hash already found %s", transition_hash)
                continue

            visited[transition_hash] = True

            # checking if final transition
            if self.problem.is_final_state(ct):
                self.logger.info('BKT successfully finished!')
                self.transitions = ct.trace_back
                break;

            # adding new transitions
            self.logger.debug('Adding new transitions!')

            # fill one and empty the other
            stack.put(self.define_transition(ct, ct.n.max_capacity, 0))
            stack.put(self.define_transition(ct, 0, ct.m.max_capacity))
            # one is maxed out, one untouched
            stack.put(self.define_transition(ct, ct.n.max_capacity, ct.m.current_filled_litters))
            stack.put(self.define_transition(ct, ct.n.current_filled_litters, ct.m.max_capacity))

            # one empty, one untouched
            stack.put(self.define_transition(ct, 0, ct.m.current_filled_litters))
            stack.put(self.define_transition(ct, ct.n.current_filled_litters, 0))

            # transfer water
            filled_bucket = ct.m.max_capacity - ct.m.current_filled_litters
            amount_to_transfer = min(ct.n.current_filled_litters, filled_bucket)
            
            b1 = ct.n.current_filled_litters - amount_to_transfer
            b2 = ct.m.current_filled_litters + amount_to_transfer
            stack.put(self.define_transition(ct, b1, b2))

            filled_bucket = ct.n.max_capacity - ct.n.current_filled_litters
            amount_to_transfer = min(ct.m.current_filled_litters, filled_bucket)
            b1 = ct.n.current_filled_litters + amount_to_transfer
            b2 = ct.m.current_filled_litters - amount_to_transfer
            stack.put(self.define_transition(ct, b1, b2))

    def define_transition(self, state: State, v1: int, v2: int) -> State:
        new_state = deepcopy(state)
        new_state.n.pour(v1)
        new_state.m.pour(v2)
        new_state.set_path(state.trace_back)
        return new_state

    def __compute_unique(self, transition: State) -> str:
        return f"{transition.m.current_filled_litters}/{transition.m.max_capacity}_{transition.n.current_filled_litters}/{transition.n.max_capacity}"