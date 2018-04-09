from collections import Counter

numShoes = int(input())
allShoes = list(input().split())
numCustomers = int(input())

sum = 0
for i in range(0,numCustomers):
    size, price = input().split()
    result = Counter(allShoes).keys()
    if size in result:
        sum += int(price)


print(sum)