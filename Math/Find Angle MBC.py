import math

ab = int(input())
bc = int(input())
x = str(int(round(math.degrees(math.atan2(ab,bc)))))+'°'
print(x)
