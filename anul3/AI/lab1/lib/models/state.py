from .bucket import Bucket

class State:
    def __init__(self, n: Bucket, m: Bucket):
        self.n = n
        self.m = m
        self.trace_back = list()

    def __str__(self):
        return f"{str(self.n)} - {str(self.m)}"

    def set_path(self, path: list):
        self.trace_back = list()
        for x in path:
            self.trace_back.append(x)
        self.trace_back.append(State(self.n, self.m))