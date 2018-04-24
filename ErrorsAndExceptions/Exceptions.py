n = int(input())
for i in range(0,n):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as f:
<<<<<<< HEAD
        print('Error Code:', f)
=======
        print('Error Code:', f)
>>>>>>> origin/master
