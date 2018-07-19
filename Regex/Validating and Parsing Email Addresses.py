import email.utils
import re

for i in range(int(input())):
    data = email.utils.parseaddr(input())
    valid_mail = re.search(r'^[a-z][a-z0-9-\._]+@[a-z]+\.[a-z]{1,3}$', data[1], re.I)
    if valid_mail:
        print(email.utils.formataddr((data[0], valid_mail.string)))
