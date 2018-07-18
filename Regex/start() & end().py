import re
string = input()
patern = input()
count = 0
for i in range(len(string)):
    matches = re.match(patern, string[i:])
    if matches:
        p_start = matches.start() + i
        p_end = matches.end() + i -1
        count += 1
        print('({}, {})'.format(p_start, p_end))
if count == 0:
    print('(-1, -1)')