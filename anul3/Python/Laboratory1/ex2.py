'''
vezi ca aici vad ca nu tratezi cazul in care string ul are si majuscule vocale
BZV: am adaugat
'''

import sys

from typing import List

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} some_string')

def main():
    """
    2. Write a script that calculates how many vowels are in a string.
    """
    try:
        validate(sys.argv)

        counter = 0
        for c in sys.argv[1]:
            if c.casefold() in ['a', 'e', 'i', 'o', 'u']:
                counter += 1

        print(f"Word '{sys.argv[1]}' has {counter} vowels")

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()
