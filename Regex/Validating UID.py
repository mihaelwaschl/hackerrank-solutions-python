import re

for i in range(int(input())):
    uid = input()
    if len(uid) == 10:
        two_character = re.search(r'.*([A-Z].*){2,}', uid)
        three_num = re.search(r'.*([0-9].*){3,}', uid)
        repeat_check = re.search(r'.*(.).*\1', uid)
        if two_character and three_num and not repeat_check:
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')