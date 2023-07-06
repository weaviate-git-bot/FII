from typing import List, Tuple


def sorting_lists(*input_lists) -> List[Tuple]:
    max_size = max([len(x) for x in input_lists])
    result = [list() for _ in range(max_size)]

    for l in input_lists:
        list_size = len(l)

        for idx in range(max_size):

            if idx >= list_size:
                result[idx].append(None)
            else:
                result[idx].append(l[idx])

    return [ tuple(x) for x in result ]

def main():
    """
    10. Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains 
    the first items in the lists, the second element contains the items on the position 2 in the lists, etc. 
    Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 
    """
    try:
        print(sorting_lists(
            [1,2,3], [5,6,7], ["a", "b", "c"], [1, 2]
        ))

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()