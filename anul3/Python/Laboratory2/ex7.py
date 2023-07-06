import sys

from typing import List, Tuple

def validate(arguments: List[str]):
    if len(arguments) < 2:
        raise Exception(f'You must have at least 2 arguments. Example usage: ./{arguments[0]} 1 2 3 5 12')

def is_palindrome(x: int):
    str_x = str(x)
    len_x = int(len(str_x) / 2)
    is_odd = len(str_x) % 2
    return str_x[:len_x] == str_x[len_x + is_odd:][::-1]

def palindrome_work(numbers: List[int]) -> Tuple[int, int]:
    palindromes = [ x for x in numbers if is_palindrome(x)]

    mp = 0
    for p  in palindromes:
        mp = max(p, mp)
    return (len(palindromes), mp)

def main():
    """
    7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. The first 
    element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest 
    palindrome number.
    """
    try:
        validate(sys.argv)
        numbers = [int(x) for x in sys.argv[1:]]
        print(palindrome_work(numbers))

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()