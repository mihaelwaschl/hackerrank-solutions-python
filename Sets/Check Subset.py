numberOfCases = int(input())

for i in range(0, numberOfCases):
    numElementsA = int(input())
    setA = set(input().split())
    numElementsB = int(input())
    setB = set(input().split())

    print(setA.issubset(setB))


