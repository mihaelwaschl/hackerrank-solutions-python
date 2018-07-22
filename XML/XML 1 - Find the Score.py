import xml.etree.ElementTree as ET

n_line = int(input())
xml = '\n'.join(input() for i in range(n_line))
tree = ET.ElementTree(ET.fromstring(xml))
root = tree.getroot()
attr_num = 0
for element in tree.iter():
    attr_num += len(element.attrib)
print(attr_num)
