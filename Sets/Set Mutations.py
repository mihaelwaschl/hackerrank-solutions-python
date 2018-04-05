numInSet = int(input())
setA = set(map(int, input().split()))
N = int(input())
for i in range(0,N):
    operation = input().split()
    setB = set(map(int, input().split()))
    if operation[0] == 'intersection_update':
        setA.intersection_update(setB)
    elif operation[0] == 'update':
        setA.update(setB)
    elif operation[0] == 'symmetric_difference_update':
        setA.symmetric_difference_update(setB)
    elif operation[0] == 'difference_update':
        setA.difference_update(setB)

print(sum(setA))