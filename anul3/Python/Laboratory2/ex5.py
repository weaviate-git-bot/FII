import sys

from typing import List

def triangulate_matrix(m: List[List]) -> List[List]:
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i > j:
                m[i][j] = 0
    return m

def main():
    """
    5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements 
    under the main diagonal with 0 (zero).
    """
    try:
        result = triangulate_matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()