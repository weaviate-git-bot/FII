import sys

from typing import List
from string import ascii_lowercase

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} \"a string here\"')

def main():
    """
    9. Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common 
    character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.
    """
    try:
        validate(sys.argv)

        s = sys.argv[1].casefold()

        chars = dict()

        for c in s:
            if c not in ascii_lowercase:
                continue
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        
        most_frequent_char = sorted(chars.items(), key = lambda x: x[1], reverse=True)[0]
        print(most_frequent_char[0])

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()