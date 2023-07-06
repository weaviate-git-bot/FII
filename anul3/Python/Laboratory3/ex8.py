import sys
import json

from typing import List, Dict

def loop(data: dict) -> List[str]:
    visited = set()
    path = list()

    curr_node = 'start'

    while curr_node not in visited:
        visited.add(curr_node)
        path.append(curr_node)
        curr_node = data[curr_node]

    return path

def main():
    """
    8. Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: the value of the current key is the key for the next value, until you find a loop (a key that was visited before). The function must return the list of objects obtained as previously described. 
    """
    try:
        result = loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()