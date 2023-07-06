import sys
import json

from typing import List, Dict

def combine_sets(s1: set, s2: set) -> Dict[str, set]:
    return {
        f"{s1} | {s2}": s1.union(s2),
        f"{s1} & {s2}": s1.intersection(s2),
        f"{s1} - {s2}": s1.difference(s2),
    }


def op_sets(*sets) -> Dict[str, set]:
    all_sets = dict()
    for s1 in range(len(sets)):
        for s2 in range(s1 + 1, len(sets)):
            all_sets.update(combine_sets(sets[s1], sets[s2]))

    return all_sets

def serialize_set(sset: set) -> None:
    return list(sset)

def main():
    """
    7. Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -. 
    """
    try:
        sets_dict = op_sets({1,2}, {2,3})
        print(json.dumps(sets_dict, indent=2, default=serialize_set))
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()