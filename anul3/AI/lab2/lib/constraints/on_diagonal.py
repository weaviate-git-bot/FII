from .constraint import Constraint

class OnDiagonalConstraint(Constraint):
    def is_safe(self, line: int, col: int) -> bool:
        for i, j in zip(range(line, -1, -1), range(col, -1, -1)):
            if self.table.is_queen_at(i,j):
                return False

        for i, j in zip(range(line, self.table.size, 1), range(col, -1, -1)):
            if self.table.is_queen_at(i,j):
                return False
        return True