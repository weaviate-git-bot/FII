from lib.models import Problem, State
from lib.logging import LoggerBuilder

from typing import List

class DefaultAlgorithm:
    def __init__(self, problem: Problem):
        self.problem = problem
        self.transitions = list()
        self.logger  = LoggerBuilder.get_instance().get_logger()


    def solve(self):
        pass

    def get_transitions(self) -> List[State]:
        return [str(t) for t in self.transitions]