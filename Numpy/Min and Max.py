import numpy as np

n, m = map(int, input().split())
array = np.array([input().split() for _ in range(n)], int)
min_array = np.min(array, axis=1)
max_in_min = np.max(min_array, axis=None)
print(max_in_min)