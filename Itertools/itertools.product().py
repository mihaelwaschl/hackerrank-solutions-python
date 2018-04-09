import itertools

listA = list(map(int,input().split()))
listB = list(map(int,input().split()))
cartProduvt = tuple(itertools.product(listA, listB))
for i in cartProduvt:
    print(i, end=' ')