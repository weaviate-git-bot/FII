from .constraint import Constraint

class SameColumnConstraint(Constraint):
    def is_safe(self, line: int, col: int) -> bool:
        for q in self.table.queens:
            if q.col == col:
                return False
        return True