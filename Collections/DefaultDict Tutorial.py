from collections import defaultdict

n, m = input().split()
d = defaultdict(list)

for a in range(0,int(n)):
    d['A'].append(input())
for b in range(int(m), int(n)-1):
    d['B'].append(input())
for i in d['B']:
    for i2 in d['A']:
        if i == 'a':
            print('to je ok')
# print(d['A'])
# print(d['B'])

