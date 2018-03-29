a = int(input())
listA =input().strip().split(' ')
b = int(input())
listB = input().strip().split(' ')

setA = set(listA)
setB = set(listB)
notInB = setA.difference(setB)
notInA = setB.difference(setA)

notInB.update(notInA)
sort = sorted(notInB, key=int)
for i in sort:
    print(int(i))


