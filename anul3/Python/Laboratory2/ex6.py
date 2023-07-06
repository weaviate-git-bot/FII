import sys

from typing import List

def count_elements_in_lists(*lists, x) -> List[List]:
    values = dict()
    for l in lists:
        for val in l:
            if val in values:
                values[val] += 1
            else:
                values[val] = 1
    
    result = []
    for k, v in values.items():
        if v == x:
            result.append(k)
    return result

def main():
    """
    Write a function that receives as a parameter a variable number of lists and a whole number x. 
    Return a list containing the items that appear exactly x times in the incoming lists. 
    """
    try:
        result = count_elements_in_lists(
            [1,2,3], [2,3,4],[4,5,6], [4,1, "test"],
            x=2
        )
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()