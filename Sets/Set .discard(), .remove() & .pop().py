n = int(input())
s = set(map(int, input().split()))
numComands = int(input())

listComandTargetItems = []
for i in range(numComands):
    comandTargetItem = input().split(' ')
    listComandTargetItems.append(comandTargetItem)

for i2 in range(len(listComandTargetItems)):
   if listComandTargetItems[i2][0] == 'pop':
       try:
        s.pop()
       except KeyError:
           pass
   elif listComandTargetItems[i2][0] == 'remove':
       try:
           s.remove(int(listComandTargetItems[i2][1]))
       except KeyError:
           pass
   elif listComandTargetItems[i2][0] == 'discard':
       try:
           s.discard(int(listComandTargetItems[i2][1]))
       except KeyError:
           pass
sumListNumbers = sum(list(s))
print(sumListNumbers)