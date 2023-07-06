import sys
import os
from typing import List, Dict

def get_from_path(my_path: str, extensions = {}) -> List[str]:
    if not os.path.exists(my_path):
        print(f'The given path does not exist: {my_path}')
        return

    if os.path.isfile(my_path):
        with open(my_path, 'r') as f:
            return f.read()[-20:]

    for file in os.listdir(my_path):
        if not os.path.isfile(os.path.join(my_path, file)):
            get_from_path(os.path.join(my_path, file), extensions)
            continue

        if file[0] == '.': 
            continue
        extension = file.split('.')
        if len(extension) <= 1:
            continue
        
        extension = extension[-1]
        extensions.update({extension: extensions.get(extension, 0) + 1})
    
    return sorted(list([(k, v) for k,v in extensions.items()]), key=lambda x: x[1], reverse=True)

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} dir_or_file')

def main():
    """
    3. Să se scrie o funcție ce primește ca parametru un string my_path.

    Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. Dacă parametrul 
    reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată descrescător după count, unde extensie 
    reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv) din 
    directorul dat ca parametru. 
    """
    # try:
    #     validate(sys.argv)

    print(get_from_path(sys.argv[1]))
    # except Exception as e:
    #     print(f"Error: {e}")
    
if __name__ == '__main__':
    main()