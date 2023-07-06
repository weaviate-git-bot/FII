from typing import List

def lists_work(a: List, b: List):
    a_n_b = list(set(a) & set(b))
    a_u_b = list(a + b)
    a_minus_b = [ x for x in a if x not in b]
    b_minus_a = [ x for x in b if x not in a]
    return a_n_b, a_u_b, a_minus_b, b_minus_a

def main():
    """
    3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
    """
    try:
        print(lists_work([10,20,30], [20, 14, 59]))
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()