import sys
import os
from typing import List, Dict

def get_extensions(directory: str) -> List[str]:
    extensions = set()
    for file in os.listdir(directory):
        if not os.path.isfile(os.path.join(directory, file)):
            continue
        extension = file.split('.')
        if len(extension) > 1 and not file.startswith(f'.{extension}'):
            extensions.add(extension[-1])
    return sorted(extensions, key=lambda x: len(x))

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def main():
    """
    4. Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la linia de
    comandă (nerecursiv). Lista trebuie să fie sortată crescător.
    """
    try:
        validate(sys.argv)

        print(get_extensions(sys.argv[1]))
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()