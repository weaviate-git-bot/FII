import sys
import os

from typing import List, Dict

def get_all_files(dir_path: str) -> List[str]:
    if not os.path.isdir(dir_path):
        raise Exception(f'The given path is not a directory: {dir_path}')
    files = []
    for file in os.listdir(dir_path):
        if not os.path.isfile(os.path.join(dir_path, file)):
            continue
        files.append(os.path.join(dir_path, file))
    return files

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def main():
    """
    8. Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un director aflat pe
    disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.
    """
    try:
        validate(sys.argv)

        print(get_all_files(sys.argv[1]))


    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()