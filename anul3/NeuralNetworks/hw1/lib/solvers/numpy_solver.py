import numpy as np
from typing import List

from .solver import Solver

class NumpySolver(Solver):
    """
    Extending the base class, using the numpy library
    """
    def solve(self) -> List[int]:
        print('Numpy solver')
        a = np.matrix(self.A)
        b = np.matrix(self.B)

        a_1 = np.linalg.inv(a)

        result = (a_1 @ b.reshape((3,1)))
        return result.reshape((1,3)).tolist()[0]