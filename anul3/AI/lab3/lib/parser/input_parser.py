class InputParser:
    SPLIT_BY = ' '

    def __init__(self, input_file):
        self.__input_file = input_file

    def parse(self):
        data = ''
        with open(self.__input_file, 'r') as fd:
            data = fd.read()
        
        return self.__parse_input(data)

    def __parse_input(self, data: str):
        lines = data.splitlines()
        p1, dir1,dir2 = list(filter(lambda x: x !=' ', lines[0].split(self.SPLIT_BY)))
        p2, dir3,dir4 = list(filter(lambda x: x !=' ', lines[1].split(self.SPLIT_BY)))
        m1, m2 = list(filter(lambda x: x !=' ', lines[2].split(self.SPLIT_BY)))
        m3, m4 = list(filter(lambda x: x !=' ', lines[3].split(self.SPLIT_BY)))

        return {
            'names': [p1, p2],
            'directions': [dir1, dir2, dir3, dir4],
            'matrix': [[m1, m2], [m3, m4]]
        }