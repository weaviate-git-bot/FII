import sys

def my_function(*args, **kwargs):
    return sum(list(kwargs.values()))

def main():
    """
    7. Create a function and an anonymous function that receive a variable number of arguments. Both will return the sum of the values of the keyword arguments.

    Example:

    For the call my_function(1, 2, c=3, d=4) the returned value will be 7.
    """
    try:
        print(my_function(1,2, c=3, d=4))
        print((lambda *args, **kwargs: sum(list(kwargs.values())))(1, 2,c=3, d=4))
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()