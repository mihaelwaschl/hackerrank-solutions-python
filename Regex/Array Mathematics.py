import numpy as np

n, m = map(int, input().split())
a = np.array(input().split(), int)
b = np.array(input().split(), int)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)