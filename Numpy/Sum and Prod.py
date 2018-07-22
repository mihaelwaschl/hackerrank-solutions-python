import numpy as np

n, m = map(int, input().split())
array = np.array([input().split() for _ in range(m)], int)
s = np.sum(array, axis=0)
prod = np.prod(s, axis=0)
print(prod)
