import xml.etree.ElementTree as ET

n_lines = int(input())
xml = ('\n').join(input() for i in range(n_lines))
tree = ET.ElementTree(ET.fromstring(xml))
maxdepth = -1
def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
    for child in elem:
        depth(child, level+1)
depth(tree.getroot(), -1)
print(maxdepth)