setA = set(input().split())
numOfSets = int(input())
result = 'True'
for i in range(0,numOfSets):
    setB = set(input().split())
    if setB.issubset(setA) == False:
        result = False
        break
print(result)