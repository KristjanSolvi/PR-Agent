import xml.etree.ElementTree as ET


def parse_user_xml(xml_string: str) -> dict:
    root = ET.fromstring(xml_string)
    return {child.tag: child.text for child in root}


def load_user_xml_file(path: str) -> dict:
    tree = ET.parse(path)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
