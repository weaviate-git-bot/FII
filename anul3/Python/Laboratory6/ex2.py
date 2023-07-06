import sys
import re

from typing import List, Dict

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def long_length_substrings(regex: str, text: str, w_len: int) -> List[str]:
    return [x for x in re.findall(regex, text) if len(x) == w_len]


def main():
    """
    2. Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns those long-length x substrings that 
    match the regular expression.
    """
    try:
        validate(sys.argv)
        text = sys.argv[1]
        result = long_length_substrings(r'\w+', text, 3)

        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()