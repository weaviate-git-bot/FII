'''
e in regula
'''
import sys

from typing import List, Tuple

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} SomeString')

def top_left_to_right_direction(top: int, left: int, right: int, bottom: int, matrix: List[str]) -> Tuple[str, int, int, int, int]:
    result = ''
    for i in range(left, right + 1):
        result += matrix[top][i]

    top += 1
    return result, top, left, right, bottom

def top_right_to_down_direction(top: int, left: int, right: int, bottom: int, matrix: List[str]) -> Tuple[str, int, int, int, int]:
    result = ''
    for i in range(top, bottom + 1):
        result += matrix[i][right]

    right -= 1

    return result, top, left, right, bottom

def down_right_to_left_direction(top: int, left: int, right: int, bottom: int, matrix: List[str]) -> Tuple[str, int, int, int, int]:
    result = ''
    for i in range(right, left - 1, -1):
        result += matrix[bottom][i]
    
    bottom -= 1
    return result, top, left, right, bottom

def down_left_to_top_direction(top: int, left: int, right: int, bottom: int, matrix: List[str]) -> Tuple[str, int, int, int, int]:
    result = ''
    for i in range(bottom, top - 1, -1):
        result += matrix[i][left]
    
    left += 1
    return result, top, left, right, bottom

def spiral_print(row: int, col: int, matrix: List[str]) -> str:
    top = 0
    bottom = row - 1
    left = 0
    right = col - 1

    direction = 0

    s = ''

    while top <= bottom and left <= right:
        word, top, left, right, bottom = {
            0: top_left_to_right_direction(top, left, right, bottom, matrix),
            1: top_right_to_down_direction(top, left, right, bottom, matrix),
            2: down_right_to_left_direction(top, left, right, bottom, matrix),
            3: down_left_to_top_direction(top, left, right, bottom, matrix)
        }[direction]

        s += word
        direction = (direction + 1) % 4 
    
    return s

def main(matrix: List[str]):
    """
    5. Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):
        firs      1  2  3  4    =>   first_python_lab
        n_lt      12 13 14 5
        oba_      11 16 15 6
        htyp      10 9  8  7
    """
    try:
        n = len(matrix)
        print(spiral_print(n,n, matrix))
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    matrix = ["firs", "n_lt", "oba_", "htyp"]
    main(matrix)
