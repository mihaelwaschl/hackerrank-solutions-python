import re

for i in range(int(input())):
    print(bool(re.match(r'[0-9+-.]?(\d?)+\.\d+$', input())))
