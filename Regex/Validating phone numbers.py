import re

for i in range(int(input())):
    mobile_number = input().strip()
    if re.search(r'^(7|8|9)([0-9]{9})$', mobile_number):
        print('YES')
    else:
        print('NO')

