import sys
import re

from typing import List, Dict

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def extract_words(text: str) -> List[str]:
    return re.findall(r'\w+', text)

def main():
    """
    1. Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters.
    """
    try:
        validate(sys.argv)
        text = sys.argv[1]
        result = extract_words(text)
        print(result)

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()