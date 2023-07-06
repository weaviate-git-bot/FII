import sys
import re

from typing import List, Dict

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def is_cnp(text):
    # check if is a valid cnp regex
    return re.match('^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$', text)


def main():
    """
    6. Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship means replacing characters from odd positions with *.
    """
    try:
        validate(sys.argv)
        text = sys.argv[1]
        result = is_cnp(text)
        print(f"{text} is {'not' if result is False else ''}a valid CNP")

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()