import re

result = []
for i in range(int(input())):
    string = input()
    remove_and = re.sub(r'(?<= )(&&)(?= )', 'and', string)
    remove_or = re.sub(r'(?<= )(\|\|)(?= )', 'or', remove_and)
    result.append(remove_or)
for p in result:
    print(p)
