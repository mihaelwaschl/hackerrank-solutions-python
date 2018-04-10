import collections, re

numElements = int(input())
for i in range(0,numElements):
    record_list = re.split(r'(\d+)', input().strip())
    print(record_list)