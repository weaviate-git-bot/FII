# Laboratoare Python - Bogdan Zavadovschi 3B5

### Homeworks done

- [x] Laboratory 1. [Lab1](https://sites.google.com/site/fiipythonprogramming/laboratories/lab-1?authuser=0)
- [x] Laboratory 2. [Lab2](https://sites.google.com/site/fiipythonprogramming/laboratories/lab-2?authuser=0)
- [X] Laboratory 3. [Lab3](https://sites.google.com/site/fiipythonprogramming/laboratories/lab-3?authuser=0)
- [X] Laboratory 4. [Lab4](https://sites.google.com/site/fiipythonprogramming/laboratories/lab-4?authuser=0)
- [X] Laboratory 5. [Lab4](https://sites.google.com/site/fiipythonprogramming/laboratories/lab-5?authuser=0)

### Template
```python
import sys

from typing import List, Dict

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def main():
    """
    Boileplate
    """
    try:
        validate(sys.argv)


    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()
```