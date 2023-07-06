class Constraint:
    def __init__(self, table: 'Table'):
        self.table = table

    def is_safe(self, line: int, col: int) -> bool:
        pass