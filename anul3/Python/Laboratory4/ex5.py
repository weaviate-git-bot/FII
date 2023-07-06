import sys
import os
from typing import List, Dict

def open_file_and_search(file: str, needle: str) -> bool:
    with open(file, 'r') as f:
        return f.read().count(needle) > 0

def needle_in_haystack(haystack: str, needle: str) -> List[str]:
    if not os.path.exists(haystack):
        raise ValueError(f'The given path does not exist: {haystack}')
    
    if not os.path.isfile(haystack) and not os.path.isdir(haystack):
        raise ValueError(f'The given path is not a file or a directory: {haystack}')

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
    5. Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza o listă de 
    fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in fișierul respectiv 
    iar dacă este un director se va căuta recursiv in toate fișierele din acel director. Dacă target nu este nici fișier, nici 
    director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
    """
    try:
        validate(sys.argv)

        print(needle_in_haystack(sys.argv[1], sys.argv[2]))

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()