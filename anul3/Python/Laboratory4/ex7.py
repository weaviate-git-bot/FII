import sys
import os

from typing import List, Dict

def get_file_stats(file_path: str) -> Dict:
    if not os.path.isfile(file_path):
        raise Exception(f'The given file does not exist: {file_path}')
    
    extension = file_path.split('.')[-1]
    if extension == file_path:
        extension = ''

    file_stats = {
        'full_path': os.path.abspath(file_path),
        'size': os.path.getsize(file_path),
        'extension': extension,
        'can_read': os.access(file_path, os.R_OK),
        'can_write': os.access(file_path, os.W_OK),
    }

    return file_stats

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def main():
    """
    7)	Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si returnează un 
    dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea fisierului in octeti, 
    file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca se poate citi din/scrie in fisier.
    """
    try:
        validate(sys.argv)

        print(get_file_stats(sys.argv[1]))
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()