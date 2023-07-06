'''
e ok
'''

import sys

from typing import List

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 1234')

def main():
    """
    6. Write a function that validates if a number is a palindrome.
    """
    try:
        validate(sys.argv)

        number = sys.argv[1]

        if number == number[::-1]:
            print('Is a palindrome')
        else:
            print('Not a palindrome')

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()
