
import sys
import os
import re

def find_files(path, regex):
    for file in os.listdir(path):
        print(file)
        p = os.path.join(path, file)
        if os.path.isdir(p):
            find_files(p, regex)
        else:
            conditions_met = 0 
            if re.match(regex, file):
                conditions_met = 1
            
            with open(p, 'r') as f:
                if re.search(regex, f.read()):
                    conditions_met += 1
            
            if conditions_met == 2:
                print(f">> {p}")
            if conditions_met == 1:
                print(f"{p}")

def main():
    """
    8. Write a function that recursively scrolls a directory and displays those files whose name matches a regular 
    expression given as a parameter or contains a string that matches the same expression. Files that satisfy both 
    conditions will be prefixed with ">>"
    """
    try:
        find_files('../', '\w+')

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()