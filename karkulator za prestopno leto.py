year = int(input())

if year%400 is 0:
    print('True')
else:
    if year%4 != 0:
        print('False')
    elif year%4 is 0:
        if year%100 is 0:
            print('False')
        else:
            print('True')
