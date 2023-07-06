from lib.models import Table

class BacktrackingAlgorithm:
    def __init__(self, table: Table):
        self.table = table

    def solve(self):   
        return self.recurse(0)

    def recurse(self, col: int) -> bool:
        if col >= self.table.size:
            return True

        for i in range(self.table.size):
            if self.table.is_safe(i, col):
                self.table.set_queen(i, col)
                if self.recurse(col + 1):
                    return True
                self.table.remove_queen(i, col)
        
        return False