import re

all_mails = []
for i in range(int(input())):
    all_mails.append(input())
result = list(filter(lambda x: re.search(r'^[a-z0-9_-]+@+[a-z0-9]+\.\w{1,3}$', x , re.IGNORECASE), all_mails))
print(sorted(result))

