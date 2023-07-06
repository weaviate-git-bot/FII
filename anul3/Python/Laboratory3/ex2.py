import sys

from typing import List, Dict

def frequency_chars(sentence: str) -> Dict[str, int]:
    data = dict()
    for x in sentence:
        if x in data:
            data[x] += 1
        else:
            data[x] = 1

    data = dict(sorted(data.items(), key=lambda x: x[0]))
    return data

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} "Ana has apples"')

def main():
    """
    2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text.
    """
    try:
        validate(sys.argv)

        result = frequency_chars(sys.argv[1])
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()