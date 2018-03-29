n,m = input().strip().split()
arr = list(input().strip().split(' '))
setA = set(input().strip().split(' '))
setB = set(input().strip().split(' '))

happines = 0
print(sum([(i in setA) - (i in setB) for i in arr]))

