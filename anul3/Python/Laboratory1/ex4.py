'''
vezi ca aici nu tratezi chiar toate cazurile in regula, de exemplu poti primi ceva care nu e UpperCamelCase sau poti primi o litera majuscula si se apendeaa aiurea la inceput un '_'.
poti verifica prima litera daca e majuscula si sa vezi de acolo ce mai poti face.

BZV: Am fixuit aici problema cu _ la inceput. Din ce am vazut pe cazurile helloWorld helloworld, hello_World (aici pune __ la rand dar cred ca e corect ca in the end nici nu e un camelCase valid ala)
'''

import sys

from typing import List

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} SomeString')

def main():
    """
    4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
    """
    try:
        validate(sys.argv)

        s1 = sys.argv[1]
        buffer = ''
        transformed_word = ''
        for c in s1:
            if not c.isupper():
                buffer += c
                continue

            if len(buffer) == 0:
                buffer = c.lower()
                continue
            
            if len(transformed_word) != 0:
                transformed_word += "_"
            transformed_word += f"{buffer}"

            buffer = c.lower()

        transformed_word += f"_{buffer}"
        if transformed_word[0] == '_':
            transformed_word = transformed_word[1:]
        print(transformed_word)

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()
