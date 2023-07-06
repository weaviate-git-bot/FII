
def my_function(l: list) -> list:
    odd = [x for x in l if x % 2 != 0]
    even = [x for x in l if x % 2 == 0]

    return [(even[idx], odd[idx]) for idx in range(min(len(odd), len(even)))]

def main():
    """
    5. Write a function that receives a list with integers as parameter that contains an equal number of even and odd numbers that 
    are in no specific order. The function should return a list of pairs (tuples of 2 elements) of numbers (Xi, Yi) such that Xi is 
    the i-th even number in the list and Yi is the i-th odd number
    """
    try:
        result = my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]) 
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()