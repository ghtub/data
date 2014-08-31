import xml.etree.ElementTree as ET

class ParseXML:
    """A simple example class for parsing XML"""
    i = 12345
    def __init__(self,filename):
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()
        
parser = ParseXML("sample.xml")

print parser.root.tag