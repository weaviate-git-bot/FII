from typing import List

class Solver:
    """
    The base class that will solve a equation like:

    a1X + b1Y + c1Z = r1
    a2X + b2Y + c2Z = r2
    a3X + b3Y + c3Z = r3

    They will find X, Y, Z and return them as a List[int]
    """
    def __init__(self, A: List[List[int]], B: List[int]) -> None:
        self.A = A
        self.B = B

    def solve(self) -> List[int]:
        pass