import sys
import re

from typing import List, Dict

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def censor_words(text):
    # find all words that begin and end with vowels
    all_matches = re.findall(r'\b[aeiouAEIOU]\w*[aeiouAEIOU]\b', text)
    print(all_matches)

    for match in all_matches:
        tmp = ''.join([ '*' if i % 2 == 1 else c for i, c in enumerate(match)])
        text = text.replace(match, tmp)

    return text


def main():
    """
    6. Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship means replacing characters from odd positions with *.
    """
    try:
        validate(sys.argv)
        text = sys.argv[1]
        result = censor_words(text)
        print(result)

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()