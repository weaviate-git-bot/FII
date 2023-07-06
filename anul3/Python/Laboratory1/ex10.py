'''
e in regula, ai putea sa te uiti si dupa functia strip
'''

import sys

from typing import List

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} \"Some random string here\"')

def main():
    """
    10. Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated 
    by only ONE space. For example: "I have Python exam" has 4 words.
    """
    try:
        validate(sys.argv)

        text = sys.argv[1]

        list_text = text.split(' ')

        list_text_without_empty = list(filter(lambda x: len(x) > 0, list_text))

        print(len(list_text_without_empty))
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()
