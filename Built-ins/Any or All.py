n = int(input())
num = list(map(str, input().split()))
print(all(map(lambda x: int(x)>=0, num)) and any(map(lambda x: x==x[::-1], num)))
