import sys

from utils import process_item

def main():
    while True:
        try:
            item = input('Enter an integer: ')
            if item == 'q':
                print('Bye bye!')
                break
            print(process_item(int(item)))
        except ValueError:
            print('Error: Item must be an integer')
            continue


if __name__ == '__main__':
    main()