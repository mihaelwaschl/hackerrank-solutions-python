from collections import deque

d = deque()
num_operations = int(input())
for i in range(num_operations):
    inputs = input().split()
    if inputs[0] == 'append':
        d.append(inputs[1])
    elif inputs[0] == 'pop':
        d.pop()
    elif inputs[0] == 'popleft':
        d.popleft()
    elif inputs[0] == 'appendleft':
        d.appendleft(inputs[1])
for j in d:
    print(j, end=' ')

