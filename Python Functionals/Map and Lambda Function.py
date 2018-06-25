cube = lambda x: x**3

def fibonacci(n):
    numbers = []
    for i in range(n):
        if i == 0:
            numbers.append(0)
        elif i == 1:
            numbers.append(1)
        else:
            new_number = numbers[-1] + numbers [-2]
            numbers.append(new_number)
    return numbers

n = int(input())
print(list(map(cube, fibonacci(n))))
