class Queen:
    def __init__(self, line: int, col: int):
        self.line = line
        self.col = col

    def __str__(self):
        return f"queen({self.line+1}, {self.col+1})"