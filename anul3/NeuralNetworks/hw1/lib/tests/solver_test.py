from typing import List

from lib.solvers import VanillaSolver, NumpySolver

class TestSolver:
    def __init__(self, A: List[List[int]], B: List[int]):
        self.A = A
        self.B = B

    def solve(self) -> bool:
        result_vanilla = VanillaSolver(self.A, self.B).solve()
        result_numpy = NumpySolver(self.A, self.B).solve()

        return (result_vanilla == result_numpy)