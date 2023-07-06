import sys

def is_valid(x):
    return isinstance(x, dict) and len(x.keys()) >= 2 and any(isinstance(y, str) and len(y) >= 3 for y in x)

def my_function(*args, **kwargs):
    return [
        x for x in list(args) + list(kwargs.values()) if is_valid(x)
    ]

def main():
    """
    4. Write a function that receives a variable number of arguments and keyword arguments. The function returns a list containing 
    only the arguments which are dictionaries, containing minimum 2 keys and at least one string key with minimum 3 characters.
    """
    try:
        result = my_function(
            {1: 2, 3: 4, 5: 6}, 
            {'a': 5, 'b': 7, 'c': 'e'}, 
            {2: 3}, 
            [1, 2, 3],
            {'abc': 4, 'def': 5},
            3764,
            dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
            test={1: 1, 'test': True}
        )
        print(result)

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()