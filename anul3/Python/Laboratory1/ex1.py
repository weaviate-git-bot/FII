import sys

from typing import List


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b % a, a)

def validate(arguments: List[str]):
    if len(arguments) < 3:
        raise Exception(f'You must have at least 3 arguments. Example usage: ./{arguments[0]} 1 2')

def main():
    """
    1. Find The greatest common divisor of multiple numbers read from the console.
    """
    try:
        validate(sys.argv)

        result = int(sys.argv[1])
        for i in range(2, len(sys.argv)):
            result = gcd(result, int(sys.argv[i]))
        
        print(f"GCD of given numbers is: {result}")

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()