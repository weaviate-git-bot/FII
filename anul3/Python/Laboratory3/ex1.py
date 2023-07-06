import sys
from ast import literal_eval

from typing import List, Dict

def lists_work(a: List, b: List):
    a_n_b = list(set(a) & set(b))
    a_u_b = list(a + b)
    a_minus_b = [ x for x in a if x not in b]
    b_minus_a = [ x for x in b if x not in a]
    return a_n_b, a_u_b, a_minus_b, b_minus_a

def validate(arguments: List[str]):
    if len(arguments) != 3:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def main():
    """
    1.Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
    """
    try:
        validate(sys.argv)

        list1 = list(literal_eval(sys.argv[1]))
        list2 = list(literal_eval(sys.argv[2]))

        if type(list1) != list or type(list2) != list:
            raise Exception('Both arguments must be lists')

        print(lists_work(list1, list2))

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()