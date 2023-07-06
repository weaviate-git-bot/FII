from queue import Queue
from typing import List
from copy import deepcopy

from lib.models import State, Problem


from .default_algorithm import DefaultAlgorithm


class HillClimbingAlgorithm(DefaultAlgorithm):
    def __init__(self, problem: Problem):
        super().__init__(problem)

    def getNeighbours(self, ct):
        self.logger.debug('Adding new transitions!')

        neighbours = []

        neighbours.append(self.define_transition(ct, ct.n.max_capacity, 0))
        neighbours.append(self.define_transition(ct, 0, ct.m.max_capacity))
        neighbours.append(self.define_transition(
            ct, ct.n.max_capacity, ct.m.current_filled_litters))
        neighbours.append(self.define_transition(
            ct, ct.n.current_filled_litters, ct.m.max_capacity))
        neighbours.append(self.define_transition(
            ct, 0, ct.m.current_filled_litters))
        neighbours.append(self.define_transition(
            ct, ct.n.current_filled_litters, 0))

        filled_bucket = ct.m.max_capacity - ct.m.current_filled_litters
        amount_to_transfer = min(ct.n.current_filled_litters, filled_bucket)

        b1 = ct.n.current_filled_litters - amount_to_transfer
        b2 = ct.m.current_filled_litters + amount_to_transfer
        neighbours.append(self.define_transition(ct, b1, b2))

        filled_bucket = ct.n.max_capacity - ct.n.current_filled_litters
        amount_to_transfer = min(ct.m.current_filled_litters, filled_bucket)

        b1 = ct.n.current_filled_litters + amount_to_transfer
        b2 = ct.m.current_filled_litters - amount_to_transfer
        neighbours.append(self.define_transition(ct, b1, b2))

        return neighbours

    def getBestNeighbour(self, state, neighbours):
        bestNeighbourHeuristic = self.heuristic(state)
        bestNeighbour = neighbours[0]

        for neighbour in neighbours:
            if bestNeighbourHeuristic < self.heuristic(neighbour):
                bestNeighbourHeuristic = self.heuristic(neighbour)
                bestNeighbour = neighbour

        return bestNeighbour, bestNeighbourHeuristic

    def heuristic(self, state):
        return (state.n.max_capacity * state.n.current_filled_litters) + (state.m.max_capacity * state.m.current_filled_litters)

    def define_transition(self, state: State, v1: int, v2: int) -> State:
        new_state = deepcopy(state)
        new_state.n.pour(v1)
        new_state.m.pour(v2)
        new_state.set_path(state.trace_back)
        return new_state

    def solve(self):
        self.logger.info("Started Hill climbing algorithm")

        initial_state = self.problem.get_initial_state()
        current_heuristic = self.heuristic(initial_state)
        neighbours = self.getNeighbours(initial_state)
        bestNeighbour, bestNeighbourHeuristic = self.getBestNeighbour(initial_state, neighbours)

        while bestNeighbourHeuristic > current_heuristic:
            initial_state = bestNeighbour

            if self.problem.is_final_state(initial_state):
                self.logger.info('Hill climbing successfully finished!')
                break

            current_heuristic = bestNeighbourHeuristic
            neighbours = self.getNeighbours(initial_state)
            bestNeighbour, bestNeighbourHeuristic = self.getBestNeighbour(initial_state,
                neighbours)
