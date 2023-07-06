import sys
import os
from typing import List, Dict

def get_extensions(directory: str, extensions: list = []) -> List[str]:
    if not os.path.isdir(directory):
        raise Exception(f'The given directory does not exist: {directory}')

    for file in os.listdir(directory):
        if not os.path.isfile(os.path.join(directory, file)):
            get_extensions(os.path.join(directory, file), extensions)
            continue
        extension = file.split('.')[-1]
        if extension not in extensions:
            extensions.append(extension)

    return extensions

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} directory_name')

def main():
    """
    1.Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director. 
    Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca parametru.
    """
    try:
        validate(sys.argv)

        extensions = get_extensions(sys.argv[1])

        print(extensions)

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()