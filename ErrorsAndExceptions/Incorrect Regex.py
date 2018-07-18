import re

for i in range(int(input())):
    try:
        matches = re.match(input(), 'abc')
        print('True')
    except:
        print('False')