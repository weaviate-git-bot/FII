from typing import List


def group_by_rhyme(words: List[str]) -> List[List[str]]:
    data = dict()
    
    for word in words:
        ids = word[-2:]

        if ids in data:
            data[ids].append(word)
        else:
            data[ids] = [word]

    return [ x for x in data.values() ]

def main():
    """
    12. Write a function that will receive a list of words  as parameter and will return a list of lists of words, 
    grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
    """
    try:
        print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))

    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()