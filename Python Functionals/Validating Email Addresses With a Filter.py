import re

n = int(input())
allmails = ''
for i in range(n):
    mail = str(input())
    allmails += mail +'\n'

pattern = re.compile(r'[a-zA-Z0-9\.-]+@[a-zA-Z0-9]+\.\w{3}')
finded = pattern.findall(allmails)

result = []
for match in finded:
    result.append(match)

print(result)