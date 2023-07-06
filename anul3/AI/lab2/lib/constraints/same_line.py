from .constraint import Constraint

class SameLineConstraint(Constraint):

    def is_safe(self, line: int, col: int) -> bool:
        for q in self.table.queens:
            if q.line == line:
                return False
        return True