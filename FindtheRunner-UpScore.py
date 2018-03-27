n = int(input())
ar = input().strip()
split_ar = ar.split(' ')
set_ar = set(split_ar)
sordet_ar = sorted(set_ar, key = int)
print(sordet_ar[-2])



