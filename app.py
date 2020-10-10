# # pip install --upgrade lxml

import xml.etree.ElementTree as ET
tree = ET.parse('test-week3.xml')
root = tree.getroot()
print(root.findall('.//module'))


for i in root.findall(".//module"):
    print(i)


