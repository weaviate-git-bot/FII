from queue import Queue
from typing import List
from copy import deepcopy
from lib.models import State, Problem
from .default_algorithm import DefaultAlgorithm
from collections import deque


class A_Star_Algorithm(DefaultAlgorithm):
    def __init__(self, problem: Problem):
        super().__init__(problem)

    def define_transition(self, state: State, v1: int, v2: int) -> State:
        new_state = deepcopy(state)
        new_state.n.pour(v1)
        new_state.m.pour(v2)
        new_state.set_path(state.trace_back)
        return new_state

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

    def heuristic(self, state):
        return (state.n.max_capacity * state.n.current_filled_litters) + (state.m.max_capacity * state.m.current_filled_litters)

    def solve(self):
        self.logger.info("Started A* algorithm")

        initial_state = self.problem.get_initial_state()

        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([initial_state])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[initial_state] = 0

        parents = {}
        parents[initial_state] = initial_state

        while len(open_list) > 0:
            current_state = None

            for state in open_list:
                if current_state == None or g[state] > self.heuristic(state):
                    current_state = state
                    print("First bucket: %d " %
                          (current_state.n.current_filled_litters), end=" ")
                    print("Second bucket: %d " %
                          (current_state.m.current_filled_litters))

            if current_state == None:
                print('No solution exist!')
                return None

            if self.problem.is_final_state(current_state):
                self.logger.info('Hill climbing successfully finished!')
                break

            # for all neighbors of the current node do
            for neighbour in self.getNeighbours(current_state):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if neighbour not in open_list and neighbour not in closed_list:
                    open_list.add(neighbour)
                    parents[neighbour] = current_state
                    g[neighbour] = g[current_state]

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[neighbour] > g[current_state]:
                        g[neighbour] = g[current_state]
                        parents[neighbour] = current_state

                    if neighbour in closed_list:
                        closed_list.remove(neighbour)
                        open_list.add(current_state)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(current_state)
            closed_list.add(current_state)
