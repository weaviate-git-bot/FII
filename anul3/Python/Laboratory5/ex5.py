def my_function(l: list) -> list:
    return [x for x in l if isinstance(x, (int, float))]

def main():
    """
    5. Write a function with one parameter which represents a list. The function will return a new list containing all the numbers 
    found in the given list.
    """
    try:
        print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()