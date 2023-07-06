import sys

from typing import List, Dict, FrozenSet, Tuple

from regex import R

def validate_dict(s: FrozenSet[Tuple[str, str, str, str]], d: Dict[str, str]):
    keys_visited = []
    for rule in s:
        key, start, mid, end = rule


        keys_visited.append(key)
        if key not in d:
            print(f'-> Failed to find key \'{key}\' in dict')
            continue

        v = d[key]
        if not v.startswith(start):
            return False
        if not v.endswith(end):
            return False

        if not v.startswith(mid) and not v.endswith(mid) and mid in v:
            continue
    
    return len(keys_visited) == d.keys()

def main():
    """
    5. The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.
    """
    try:
        s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
        d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

        print(validate_dict(s,d))
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()