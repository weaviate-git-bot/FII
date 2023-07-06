import sys

from typing import List, Dict

def compare_dict(d1: dict, d2: dict):
    if len(d1.keys()) != len(d2.keys()):
        return False
    for k in d1.keys():
        if k not in d2:
            return False

        if type(d1[k]) != type(d2[k]):
            return False

        if type(d1[k]) == dict:
            if not compare_dict(d1[k], d2[k]):
                return False
            continue

        if d1[k] != d2[k]:
            return False
    return True
        

def main():
    """
    3. Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
    """
    try:

        dict1 = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': {
                'x': 1,
            },
            'data': [1,2]
        }

        dict2 = {
            'a': 1, 
            'b': 2,
            'c': 3,
            'd': {
                'x': 1
            },
            'data': [1,2]
        }

        print(f"Dict1 and Dict2 are {'not ' if not compare_dict(dict1, dict2) else ''}equal")
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()