from typing import List, Tuple


def sorting(data: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    return sorted(data, key=lambda x: x[1][2])

def main():
    """
    11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
    """
    try:
        print(sorting(
            [('abc', 'bcd'), ('abc', 'zza')] 
        ))

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()