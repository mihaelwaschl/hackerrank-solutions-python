from itertools import combinations

string, k = input().split()
result = list(combinations(string,int(k)))

print(result)
