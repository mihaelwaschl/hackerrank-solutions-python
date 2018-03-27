while True:
    try:
        number = int(input('Vpiši številko!\n'))
        break
    except ValueError:
        print('Nisi vnesel številke.\n')
array = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for elementi in a:
    if elementi < number:
        array.append(elementi)
print(array)
