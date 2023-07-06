from math import sqrt

def process_item(x: int) -> int:
    def isPrime(x: int):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for idx in range(3, int(sqrt(x) + 1), 2):
            if x % idx == 0:
                return False
        return True

    while not isPrime(x):
        x += 1
    return x

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python3 utils.py <item>')
        sys.exit(1)
    try:
        print(process_item(int(sys.argv[1])))
    except ValueError:
        print('Error: Item must be an integer')
        sys.exit(1)