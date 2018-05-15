from collections import deque

result = 'Yes'
numTestCases = int(input())

for i in range(numTestCases):
    numCubes = int(input())
    start = deque(map(int, input().split()))
    base = max(start[0], start[-1])

    while len(start) > 0:
        if int(start[0]) < int(start[-1]):
            item =start.pop()
        else:
            item = start.popleft()
        if item > base:
            print('No')
            break
        else:
            base = item
    else:
        print('Yes')
        start.clear()
