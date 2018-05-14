from collections import deque

start = deque()
finish = deque()
result = 'Yes'
numTestCases = int(input())

for i in range(numTestCases):
    numCubes = int(input())
    sideLength = map(int, input().split())
    for cube in sideLength:
        start.append(cube)
    while len(start) > 0:
        if int(start[0]) < int(start[-1]):
            finish.append(start[-1])
            start.pop()
        elif int(start[0]) > int(start[-1]):
            finish.append(start[0])
            start.popleft()
        elif int(start[0]) == int(start[-1]):
            finish.append(start[0])
            start.popleft()
    for j in range(1,len(finish)):
       if finish[j-1] < finish[j]:
           result = 'No'
           print(finish[j-2])
           print(finish[j - 1])
           print(finish[j])
           print(finish[j + 1])
           print(finish[j + 2])
           break
    start.clear()
    finish.clear()
    print(result)