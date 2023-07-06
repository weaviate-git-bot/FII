from typing import List, Union

class Parser:
    """
    This class will help you parse an input like

    a1X + b1Y + c1Z = r1
    a2X + b2Y + c2Z = r2
    a3X + b3Y + c3Z = r3

    And output it like:
    ([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]], [r1, r2, r3])
    """
    def __init__(self, file_path: str) -> None:
        self.__file = file_path

    def parse(self) -> Union[List[List[int]], List[int]]:
        matrix = []
        results = []
        with open(self.__file, 'r') as f:
            data = f.readline()
            while data:
                left, right = self.__parse_line(data.strip())
                matrix.append(left)
                results.append(right)
                data = f.readline()

        return matrix, results

    def __parse_line(self, line) -> Union[List[int], int]:
        coefficient = [0]*3
        r = 0

        digit = ''
    
        for c in line:
            if c in ['x', 'y', 'z']:
                sanitize = digit.replace('+', '').replace(' ', '')
                # default case for x + y + z
                if sanitize == '':
                    sanitize = '1'

                coefficient[{
                    'x': 0,
                    'y': 1,
                    'z': 2
                }[c]] = int(sanitize)
                digit = ''
                continue

            if c == '=':
                digit = ''
                continue

            digit += c

        r = int(digit.replace('+', '').replace(' ', ''))
        return [coefficient, r]