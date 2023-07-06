import sys
import json

from typing import List, Dict

def my_function(*args, **kwargs):
    values = 0
    for v in kwargs.values():
        if v in args:
            values += 1
    return values

def main():
    """
    9. Write a function that receives a variable number of positional arguments and a variable number of keyword arguments adn will return the number of positional arguments whose values can be found among keyword arguments values.
    """

    try:
        result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()