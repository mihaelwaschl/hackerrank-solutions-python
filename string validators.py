string = input()
if any(i.isalnum() for i in string) is True:
    print('True')
else:
    print('False')
if any(i.isalpha() for i in string) is True:
    print('True')
else:
    print('False')
if any(i.isdigit() for i in string) is True:
    print('True')
else:
    print('False')
if any(i.islower() for i in string) is True:
    print('True')
else:
    print('False')
if any(i.isupper() for i in string) is True:
    print('True')
else:
    print('False')



