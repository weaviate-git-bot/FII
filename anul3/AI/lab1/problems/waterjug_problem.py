import math

from lib.models import Problem, State, Bucket

class WaterJugProblem(Problem):
    def __init__(self, n: int, m: int, k: int) -> None:
        self.first_bucket = n
        self.second_bucket = m
        self.desired_liters_to_be_filled = k

    def get_initial_state(self) -> State:
        return State(Bucket(self.first_bucket), Bucket(self.second_bucket))
    
    def is_final_state(self, state: State) -> bool:
        return state.m.current_filled_litters == self.desired_liters_to_be_filled or state.n.current_filled_litters == self.desired_liters_to_be_filled
    
    
    def is_solvable(self) -> bool:
        if self.first_bucket + self.second_bucket < self.desired_liters_to_be_filled:
            return False
        
        if not self.first_bucket and not self.desired_liters_to_be_filled:
            if not self.desired_liters_to_be_filled:
                return True
            return False
        

        return (self.desired_liters_to_be_filled % math.gcd(self.first_bucket, self.second_bucket)) == 0