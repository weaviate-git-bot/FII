import sys

from lib.parser import InputParser
from lib.model import Player
from lib.algorithm import DominantStrategyAlgorithm, NashEquilibriaAlgorithm

from typing import List, Tuple


def validate_input(arguments: List[str]) -> Tuple[int, List[List[int]]]:
    try:
        if len(arguments) < 2:
            raise KeyError('Too little arguments')

        game_file = str(arguments[1]) # game file

        return {
            'game_file': game_file,
        }
    except Exception as e:
        print(f"Error at starting the script. Error: {e}")
        return None


def main(game_file: str) -> None:
    parser = InputParser(game_file)
    input_data = parser.parse()

    player1 = Player(0, **input_data)
    player2 = Player(1, **input_data)

    DominantStrategyAlgorithm(player1, player2).run()
    NashEquilibriaAlgorithm(player1, player2).run()


if __name__ == '__main__':
    response = validate_input(sys.argv)
    if response is not None:
        main(**response)