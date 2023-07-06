from functools import reduce
from typing import List
import numpy as np

from .solver import Solver

class VanillaSolver(Solver):
    """
    Extending the base class, using only vanilla python functions
    """
    def solve(self) -> List[int]:
        print('Firing up vanilla solver')
        
        # a)
        det = self.__determinant(self.A)
        if det == 0:
            raise Exception("Determinant can't be 0")
            
        # b)
        a_t = self.__transpose_matrix(self.A)

        # c)
        a_star = self.__get_a_star(a_t)

        #  d
        for x in a_star:
            for i in range(len(x)):
                x[i] = (1/det)*x[i]

        final_result = self.__multiply(a_star, self.B)
        print('Successfully solved')
        return final_result

    def __multiply(self, A: List[List[int]], B: List[int]) -> List[int]:
        rez = []
        for l in A:
            s = sum(a*b for a, b in zip(l,B))
            rez.append(s)

        return rez

    def __base_determinant(self, m: List[List[int]]) -> int:
        return m[0][0] * m[1][1] - m[0][1]*m[1][0]

    def __determinant(self, m: List[List[int]]) -> int:
        order=len(m)
        positive_det=0

        for i in range(order):
            positive_det += reduce((lambda x, y: x * y), [m[(i+j)%order][j] for j in range(order)])
        negative_det=0
        for i in range(order):
            negative_det += reduce((lambda x, y: x * y), [m[(order-i-j)%order][j] for j in range(order)])
        return positive_det - negative_det

    def __transpose_matrix(self, m: List[List[int]]) -> None:
        return list(zip(*m))

    def __get_matrix_minor(self, a, i: int, j: int):
        return [row[:j] + row[j+1:] for row in (a[:i]+a[i+1:])]


    def __get_a_star(self, a: List[List[int]]) -> List[List[int]]:
        matrix_of_minors = [
            [1, -1, 1],
            [-1, 1, -1],
            [1, -1, 1]
        ]

        for i in range(len(a)):
            for j in range(len(a[i])):
                matrix_of_minors[i][j] *= self.__base_determinant(self.__get_matrix_minor(a, i, j)) 

        return matrix_of_minors
