import traceback
import sys
from typing import List, Tuple
from algorithms.hillcliming_algorithm import HillClimbingAlgorithm

from lib.logging import LoggerBuilder

from problems import WaterJugProblem
from algorithms import BacktrackingAlgorithm, BFSAlgorithm, star_algorithm

ENABLE_TRACEBACK = False
AVAILABLE_ALGORITHMS = ['bkt', 'bfs', 'hill-climbing', 'a*']

def help():
    print("""
    Laboratory 1 - Artificial Intelligence
    Authors: Bogdan Zavadovschi & Bianca Nechita
    
    Usage: ./main.py 5 4 1 bkt

    n - maximum capacity of first bucket
    m - maximum capacity of second bucket
    k - desired capacity to be found in a bucket
    algorithm - the algorithm to solve the problem. Available ones: BKT, BFS, Hill Climbing, A*
    """)

def validate_input(arguments: List[str]) -> Tuple[int, int, int, str]:
    try:
        if len(arguments) < 5:
            raise KeyError('Too little arguments')
        n = int(arguments[1])
        m = int(arguments[2])
        k = int(arguments[3])
        algo = arguments[4].lower()
        
        if algo not in AVAILABLE_ALGORITHMS:
            raise ValueError('Invalid value for algorithms!')
        return {
            'n': n,
            'm': m,
            'k': k,
            'algo': algo
        }
    except Exception as e:
        print(f"Error at starting the script. Error: {e}")
        help()
        return None
        

def main(n: int, m: int, k: int, algo: str):
    logger = LoggerBuilder.get_logger()

    problem = WaterJugProblem(n, m, k)

    algorithm = {
        'bkt': BacktrackingAlgorithm,
        'bfs': BFSAlgorithm,
        'hill-climbing': HillClimbingAlgorithm,
        'a*': star_algorithm.A_Star_Algorithm
    }[algo](problem)

    try:
        if not problem.is_solvable():
            raise Exception('Problem doesn\'t have a solution!')

        algorithm.solve()

        transitions = algorithm.get_transitions()
        logger.info("Number of steps: %d",len(transitions))
        logger.info("Steps:\n%s", '\n'.join(transitions))
    except Exception as e:
        logger.error(f'Failed to run algorithm. Error: {e}')
        if ENABLE_TRACEBACK is True:
            traceback.print_exc()

if __name__ == '__main__':
    response = validate_input(sys.argv)
    if response is not None:
        main(**response)