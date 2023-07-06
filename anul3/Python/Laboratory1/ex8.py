'''
e in regula
'''
import sys

from typing import List

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 124')

def main():
    """
    8. Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
    """
    try:
        validate(sys.argv)

        # print(bin(int(sys.argv[1])).count('1'))
        print(int(sys.argv[1]).bit_count())

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()
