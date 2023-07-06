def f9(pairs = []):
    return [
        {
            "sum": pair[0] + pair[1],
            "prod": pair[0] * pair[1],
            "pow": pair[0] ** pair[1]
        }
        for pair in pairs
    ]    

def main():
    """
    9. Write a function that receives a list of pairs of integers (tuples with 2 elements) as parameter (named pairs). The function
    should return a list of dictionaries for each pair (in the same order as in the input list) that contain the following keys (as 
    strings): sum (the value should be sum of the 2 numbers), prod (the value should be product of the two numbers), pow (the value 
    should be the first number raised to the power of the second number) 
    """
    try:
        result = f9(pairs= [(5, 2), (19, 1), (30, 6), (2, 2)]) 
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()