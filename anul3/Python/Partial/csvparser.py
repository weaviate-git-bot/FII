import sys

from typing import List, Dict

def help():
    print("""
    Usage example: ./csvparser.py file column_name
    """)

def validate(data: List[str]):
    if len(data) != 3:
        help()
        raise Exception("Error: Invalid number of arguments")

def file_reader(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def parse_line(csv_reader_dict: dict, line: str, line_nr: int, is_header = False):
    data = line.split(',')

    if len(csv_reader_dict.keys()) != len(data) and is_header is False:
        raise Exception(f"Invalid format - different words on line {line_nr}")
    
    if is_header:
        for k in data:
            if k in csv_reader_dict.keys():
                raise Exception('Invalid format - duplicate column names')
            csv_reader_dict[k] = list()
    else:
        idx = 0
        for k in csv_reader_dict.keys():
            csv_reader_dict[k].append(data[idx])
            idx += 1
        

def parse_csv(file_path: str) -> Dict[str, str]:
    data = file_reader(file_path).strip('\n').split('\n')
    
    csv_reader_dict = dict()

    header = data[0]

    parse_line(csv_reader_dict, header, 0, True)

    table = data[1:]
    for idx in range(len(table)):
        parse_line(csv_reader_dict, table[idx], idx, False)

    return csv_reader_dict

def words_finder(input_d: List[str]) -> List[str]:
    data = dict()
    for x in input_d:
        x = x.lower()
        if x in data.keys():
            data[x] += 1
        else:
            data[x] = 1
    
    result = sorted(data, key=lambda data: data[1])

    return result

        
def find_column(csv_data: Dict[str, List[str]], column_name: str, callback= None) -> List[object]:
    if column_name not in csv_data.keys():
        raise Exception(f"Unknown column name {column_name}")
    
    output = csv_data[column_name]
    if callback is not None:
        output = callback(output)
    
    return output

def main():
    try:
        validate(sys.argv)

        file_path = sys.argv[1]
        column_name = sys.argv[2]

        csv_data = parse_csv(file_path)
        
        data = find_column(csv_data, column_name, words_finder)
        if data:
            print("[OK]")
            print('\n'.join(data))
        
    except PermissionError as e:
        print(f"[ERROR] Insuficient permissions error for opening the input file.")
    except FileNotFoundError as e:
        print(f"[ERROR] Trying to read the input file failed. Error: {e}")
    except IOError as e:
        print(f"[ERROR] Error while reading data from file. Error: {e}")
    except Exception as e:
        print(f"[Error] {e}")
if __name__ == '__main__':
    main()