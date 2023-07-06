import sys

import xml.etree.ElementTree as ET

from typing import List, Dict

def validate(arguments: List[str]):
    if len(arguments) != 2:
        raise Exception(f'You must have exactly 2 arguments. Example usage: ./{arguments[0]} 10')

def extract_elements_by_attrs(xml_path, attrs):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return [elem.tag for elem in root.iter() if any([elem.attrib.get(key) == value for key, value in attrs.items()])]

def main():
    """
    5. Write another variant of the function from the previous exercise that returns those elements that have at least one attribute that corresponds to a key-value pair in the dictionary.
    """
    try:
        validate(sys.argv)

        result = extract_elements_by_attrs(sys.argv[1], {"class": "url", "name": "url-form", "data-id": "item"})

        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()