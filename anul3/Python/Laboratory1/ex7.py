'''
e in regula dar daca nu primesti un string cu un numar in interior castarea aia la int nu merge
BZV: Fixed
'''

import sys

from typing import List

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} string1234hello')

def main():
    """
    7. Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the 
    text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.
    """
    try:
        validate(sys.argv)

        s = sys.argv[1]

        last_was_digit = False
        is_first_digit = True

        extracted_number = ''

        for c in s:
            if not c.isdigit():
                if last_was_digit is True:
                    break;
                continue
            
            if is_first_digit is True:
                last_was_digit = True
                is_first_digit = False

            extracted_number += c

        extracted_number = 0 if extracted_number == '' else int(extracted_number)
        print(extracted_number)
        
        return extracted_number
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()
