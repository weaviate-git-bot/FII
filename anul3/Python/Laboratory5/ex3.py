import sys

def my_function_1(input_data: str):
    return list(filter(lambda x: x.lower() in "aeiou", input_data))

def my_function_2(input_data: str):
    return [x for x in input_data if x.lower() in "aeiou"]

def my_function_3(input_data: str):
    vowels = []
    for x in input_data:
        if x.lower() in "aeiou":
            vowels.append(x)
    return vowels

def main():
    """
    Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list with all the vowels in a given string.

    For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].
    """
    try:
        input_data = "Programming in Python is fun"
        print("Function 1: {}".format(my_function_1(input_data)))
        print("Function 2: {}".format(my_function_2(input_data)))
        print("Function 3: {}".format(my_function_3(input_data)))
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()