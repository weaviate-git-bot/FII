def sum_digits(x):
    return sum(map(int, str(x)))

 
def fibonacci(n = 1000, fibo_list = [0, 1]):
    fibs = [0, 1, 1]                                                                                           
    for f in range(2, n):                                                                                      
        fibs.append(fibs[-1] + fibs[-2])                                                                         
    return fibs

def process(filters = None, limit = None, offset = None) -> list:
    fibo_list = fibonacci()

    if filters:
        fibo_list = [item for item in fibo_list if all(filter(item) for filter in filters)]

    if offset:
        fibo_list = fibo_list[offset:]

    if limit:
        fibo_list = fibo_list[:limit]
    
    return fibo_list

def main():
    """
    7. Write a function called process that receives a variable number of keyword arguments
    The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:
    - If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument and 
    returning True/False) and will retain from the generated numbers only those for which the predicates are True. 
    - If the function receives a parameter called limit, it will return only that amount of numbers from the sequence. 
    - If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list. 
    The function will return the processed numbers.
    """
    try:
        result = process(
            filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
            limit=2,
            offset=2
        )
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()