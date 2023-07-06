import sys
import json

from typing import List, Dict

def original_duplicated(l:List[object]):
    items = dict()
    for o in l:
        if o in items:
            items[o] += 1
        else:
            items[o] = 1
    dup = 0
    orig = 0
    for v in items.values():
        if v == 1:
            orig += 1
        else:
            dup += v

    return (orig, dup)

def main():
    """
    6. Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this objective).
    """

    try:
        result = original_duplicated(
            [1,2,3,3,3, 2, 9,4,5,0,12]
        )
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()