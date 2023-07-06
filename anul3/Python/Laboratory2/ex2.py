import sys
import math
from typing import List

def is_prime(x: int) -> bool:
    if x in {0, 1}:
        return False
    if x != 2 and x % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    
    return True

def get_prime_numbers_from_list(l: List[int]) -> List[int]:
    return [ x for x in l if is_prime(x) is True]

def validate(arguments: List[str]):
    if len(arguments) < 2:
        raise Exception(f'You must have at least 2 arguments. Example usage: ./{arguments[0]} 1 2 3 5 12')

def main():
    """
    2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
    """
    try:
        validate(sys.argv)
        numbers = [int(x) for x in sys.argv[1:]]

        prime_numbers = get_prime_numbers_from_list(numbers)

        print(prime_numbers)

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()