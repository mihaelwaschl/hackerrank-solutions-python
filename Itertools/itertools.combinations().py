from itertools import combinations

string, k = input().split()
for i in range(1,int(k)+1):
    result = list(combinations(sorted(string), i))
    print(result)

