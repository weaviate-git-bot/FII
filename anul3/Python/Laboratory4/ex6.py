import sys
import os

from typing import List, Dict

def handle_exception(e):
    print(f"Error handled by callback")
    raise e

def open_file_and_search(file: str, needle: str) -> bool:
    with open(file, 'r') as f:
        return f.read().count(needle) > 0

def needle_in_haystack(haystack: str, needle: str, callback) -> List[str]:
    if not os.path.exists(haystack):
        callback(ValueError(f'The given path does not exist: {haystack}'))
    
    if not os.path.isfile(haystack) and not os.path.isdir(haystack):
        callback(ValueError(f'The given path is not a file or a directory: {haystack}'))

    if os.path.isfile(haystack):
        if open_file_and_search(haystack, needle):
            return [haystack]
        return []

    files = []
    for file in os.listdir(haystack):
        if not os.path.isfile(os.path.join(haystack, file)):
            continue
        if open_file_and_search(os.path.join(haystack, file), needle):
            files.append(os.path.join(haystack, file))
    return files

def validate(arguments: List[str]):
    if len(arguments) != 3:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} haystack needle')
def main():
    """
    6. Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește un parametru
    în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea fișierelor, se va apela 
    funcția respectivă cu instanța excepției ca parametru.
    """
    try:
        validate(sys.argv)

        print(needle_in_haystack(sys.argv[1], sys.argv[2], handle_exception))

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()