import sys

from typing import List


def ascii_flags(data: List[str], x: int = 1, flag: bool = True) -> List[List]:
    strings = []

    for s in data:
        strings.append([ y for y in s if (ord(y) % x == 0) == flag ])
    return strings

def main():
    """
    8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True. For each 
    string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True, otherwise it 
    should contain characters that have the ASCII code not divisible by x.
    """
    try:
        print(ascii_flags(
            x = 2, data = ["test", "hello", "lab002"], flag=False
        ))

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()