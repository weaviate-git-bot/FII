'''
e okay ish, aici mi-ar placea sa tratezi si cazul in care de exemplu ai s1 = 'aaa' si s2 = 'aaaaa' -> ar trebui sa ai 3 aparitii, nu 1. check find function

BZV: Added
'''

import sys

from typing import List

def validate(arguments: List[str]):
    if len(arguments) != 3:
        raise Exception(f'You must have exactly 3 arguments. Example usage: ./{arguments[0]} some_string other_string')

def count(s1: str, s2: str) -> int:
    counter = 0
    idx = 0

    s2_len = len(s2) 

    while idx < s2_len:
        idx = s2.find(s1, idx)
        if idx == -1:
            return counter
        idx += 1
        counter += 1

    return counter


def main():
    """
    3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.
    """
    try:
        validate(sys.argv)

        s1 = sys.argv[1]
        s2 = sys.argv[2]

        # print(f"String '{s1}' can be found in '{s2}' {s2.find(s1)} times")
        print(f"String '{s1}' can be found in '{s2}' {count(s1,s2)} times")



    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()
