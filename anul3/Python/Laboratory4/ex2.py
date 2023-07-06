import sys
import os

from typing import List, Dict

def get_directory(directory: str) -> List[str]:
    if not os.path.isdir(directory):
        raise Exception(f'The given directory does not exist: {directory}')

    data = []

    for file in os.listdir(directory):
        if not os.path.isfile(os.path.join(directory, file)):
            continue
        if file[0].startswith('A'):
            data.append(os.path.join(directory, file))

    return '\n'.join(data)

def write_to_file(file: str, data: str):
    with open(file, 'w') as f:
        f.write(data)

def validate(arguments: List[str]):
    if len(arguments) != 3:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} dir file')

def main():
    """
    2)	Să se scrie o funcție ce primește ca argumente două căi: director si fișier. 

    Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a fiecărui 
    fișier din interiorul directorului de la calea folder, ce incepe cu litera A. 
    """
    try:
        validate(sys.argv)

        data = get_directory(sys.argv[1])

        write_to_file(sys.argv[2], data)

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()