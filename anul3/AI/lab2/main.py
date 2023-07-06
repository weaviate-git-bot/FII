import sys
import ast

from lib.models import Table
from lib.algorithm import BacktrackingAlgorithm

from typing import List, Tuple


def validate_input(arguments: List[str]) -> Tuple[int, List[List[int]]]:
    try:
        if len(arguments) < 3:
            raise KeyError('Too little arguments')

        n = int(arguments[1]) # table dimension
        invalid_positions = ast.literal_eval(arguments[2])

        # if len(invalid_positions) != n or [type(x) != list for x in invalid_positions]:
        #     raise Exception('Invalid argument. It must be like [[4],[],[2],[]]')

        return {
            'n': n,
            'invalid_positions': invalid_positions,
        }
    except Exception as e:
        print(f"Error at starting the script. Error: {e}")
        return None


def main(n: int, invalid_positions: List[List[int]]) -> None:
    table = Table(n)

    for pair in invalid_positions:
        table.block_position(pair[0], pair[1])
    
    algorithm = BacktrackingAlgorithm(table)
    result = algorithm.solve()

    if not result:
        print("Failed to solve the problem")
        return False

    queens_positions = list([str(queen) for queen in table.queens])
    print(f"Queens will be at positions: {queens_positions}")

if __name__ == '__main__':
    response = validate_input(sys.argv)
    if response is not None:
        main(**response)