from typing import List, Tuple


def bad_luck_spectators(spectators: List[List[int]]) -> List[Tuple[int, int]]:
    results = []

    cached_rows = dict()

    s_t = list(zip(*spectators))

    for idx in range(len(s_t)):
        row = s_t[idx]
        row_size = len(row)
        for col_1 in range(1, row_size):
            for col_2 in range(0, col_1):
                val = f"{col_1, idx}"
                if row[col_1] <= row[col_2] and val not in cached_rows.keys():
                    results.append((col_1, idx))
                    cached_rows[val] = True


    return results

def main():
    """
    9.  Write a function that receives as parameter a matrix which represents the heights of the spectators in a stadium and will 
    return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see 
    the game if there is at least one taller spectator standing in front of him. All the seats are occupied. All the seats 
    are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field.
    """
    try:
        print(bad_luck_spectators(
            [[1, 2, 3, 2, 1, 1],
            [2, 4, 4, 3, 7, 2],
            [5, 5, 2, 5, 6, 4],
            [6, 6, 7, 6, 7, 5]] 
        ))

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()