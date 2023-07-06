from copy import deepcopy
from symbol import break_stmt
from typing import List

from lib.constraints import SameLineConstraint, SameColumnConstraint, OnDiagonalConstraint

from .queen import Queen

class Table:
    __CSP = [
        SameLineConstraint,
        SameColumnConstraint,
        OnDiagonalConstraint
    ]

    def __init__(self, size: int):
        self.size = size
        self.table = self.__generate_table()
        self.invalid_positions = []
        self.queens = []

    def __str__(self):
        custom = '\n'.join(str(x) for x in self.table)
        return f"Size: {self.size}\nTable:\n{custom}"

    def is_queen_at(self, line: int, col: int) -> bool:
        for queen in self.queens:
            if queen.line == line and queen.col == col:
                return True
        return False

    def block_position(self, line: int, col: int) -> None:
        self.invalid_positions.append([line-1, col-1])

    def is_safe(self, line: int, col: int) -> bool:
        for pos in self.invalid_positions:
            if pos[0] == line and pos[1] == col:
                return False

        for csp in Table.__CSP:
            if not csp(self).is_safe(line, col):
                return False
        return True

    def set_queen(self, line: int, col: int) -> None:
        self.queens.append(Queen(line, col))
        self.forward_propagate(line, col)

    def remove_queen(self, line: int, col: int) -> None:
        tbr_queen = None
        for queen in self.queens:
            if queen.line == line and queen.col == col:
                tbr_queen = queen
                break
        self.queens.remove(tbr_queen)

        self.forward_propagate(line, col, reverse_effect=True)

    def __generate_table(self) -> List[List[int]]:
        value_list = list([x for x in range(1, self.size+1)])
        possible_values = []
        for _ in range(self.size):
            x = deepcopy(value_list)
            possible_values.append(x)
        
        return possible_values

    def forward_propagate(self, line: int, col: int, reverse_effect: bool = False):
        # the line will be blocked
        for col_idx in range(self.size):
            if reverse_effect:
                self.invalid_positions.remove([line, col_idx])
            else:
                self.invalid_positions.append([line, col_idx])

        for line_idx in range(self.size):
            if reverse_effect:
                self.invalid_positions.remove([line_idx, col])
            else:
                self.invalid_positions.append([line_idx, col])
        
        # the diagonals will be blocked
        for i, j in zip(range(line, -1, -1), range(col, -1, -1)):
            if reverse_effect:
                self.invalid_positions.remove([i,j])
            else:
                self.invalid_positions.append([i,j])
        
        for i, j in zip(range(line, self.size, 1), range(col, -1, -1)):
            if reverse_effect:
                self.invalid_positions.remove([i,j])
            else:
                self.invalid_positions.append([i,j])
