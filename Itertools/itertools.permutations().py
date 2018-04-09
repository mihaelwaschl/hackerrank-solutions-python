from itertools import permutations

string = input().split()
premutations = tuple(permutations(string[0], int(string[1])))
listResult = []
for i in premutations:
    result = ''.join(i)
    listResult.append(result)
for i2 in sorted(listResult):
    print(i2)


