from collections import defaultdict
d = defaultdict(list)
n,m=map(int,input().split())

for i in range(0,n):
    word = input()
    d[word].append(str(i +1))
for i2 in range(m):
    compareWord = input()
    print(' '.join(d[compareWord]) or -1)
