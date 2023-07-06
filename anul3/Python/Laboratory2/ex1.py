import sys

from typing import List, Dict



def __fib_generator(n: int, already_computed: Dict[int, int]) -> int:
    if n in already_computed:
        return already_computed[n]
    
    already_computed[n] = __fib_generator(n - 1, already_computed) + __fib_generator(n - 2, already_computed)
    return already_computed[n]

def fibonacci(c: int) -> List:
    already_computed = {0: 0, 1: 1}
    return [__fib_generator(n, already_computed) for n in range(c)]

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def main():
    """
    1. Write a function to return a list of the first n numbers in the Fibonacci string.
    """
    try:
        validate(sys.argv)

        count = int(sys.argv[1])

        if count < 0:
            raise Exception("You must give a positive number.")
        
        fibonacci_numbers = fibonacci(count)

        print(fibonacci_numbers)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()