import sys

from typing import List, Dict

def build_xml_element(tag: str, content: str, **kwargs) -> str:
    data = " ".join([f"{k}=\\\"{v}\\\"" for k,v in kwargs.items() ])

    return f"<{tag} {data}> {content} </{tag}>"

def main():
    """
    4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters. Build and return a string that represents the corresponding XML element.     
    """
    try:

        xml_result = build_xml_element("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")

        print(xml_result)
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    main()