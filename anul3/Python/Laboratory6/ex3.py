import sys
import re

from typing import List, Dict

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def long_length_substrings(regex: List[str], text: List[str]) -> List[str]:
    return [
        t_str for t_str in text if any([re.match(r, t_str) for r in regex])
    ]


def main():
    """
    3. Write a function that receives two parameters: a list of strings and a list of regular expressions. The function will return a list of the strings 
    that match on at least one regular expression from the list given as parameter.
    """
    try:
        validate(sys.argv)
        text = sys.argv[1]
        result = long_length_substrings([r'\d+'], text.split())

        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()