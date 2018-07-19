import re

for i in range(int(input())):
    css_line = input().strip()
    color = re.findall(r'(#[0-9a-f]{3}|#[0-9a-f]{6})(?:[;,.)]{1})', css_line, re.I)
    for i in color:
        if i != '':
            print(i)
