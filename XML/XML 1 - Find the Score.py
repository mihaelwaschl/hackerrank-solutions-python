import xml.etree.ElementTree as ET

n_line = int(input())
xml = '\n'.join(input() for i in range(n_line))
root = ET.fromstring(xml)
num_attr = len(root.attrib)
for child in root:
    num_attr += len(child.attrib)
print(num_attr)

