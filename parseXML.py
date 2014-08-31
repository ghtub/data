import xml.etree.ElementTree as ET

class ParseXML:
    """A simple example class for parsing XML"""
    i = 12345
    def printChildren(self,root):
		for child in root:
			print child.tag, child.attrib
	def printGrandChildren(self,child):
		for grandchild in child:
			print grandchild.tag, grandchild.attrib
    def __init__(self,filename):
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()
	

			
parser2 = ParseXML("sample.xml")
parser = ParseXML("iTunes Music Library.xml")

print parser2.root.tag
root = parser2.root
parser2.printChildren(root)
    
#print parser.root.tag
#parser.printGrandChildren(parser.root.getchildren())

# for reference: https://docs.python.org/2/library/xml.etree.elementtree.html