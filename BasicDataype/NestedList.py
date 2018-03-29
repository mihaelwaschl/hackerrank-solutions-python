ar = []
n = int(input())
for num_st in range(n):
    name = input()
    point = float(input())
    nested_list = [name, point]
    ar += [nested_list]

points = []
for i in range(0,n):
    points_list = points.append(ar[i][1])

set_points = set(points)
ar_noDouble = list(set_points)

sort_points_list = sorted(ar_noDouble, key = float)
predzadnji = sort_points_list[1]

nameOfpredzadnji = []
for results in ar:
    for i in range(0, len(ar)):
        if predzadnji == ar[i][1]:
            nameOfpredzadnji.append(str(ar[i][0]))
            #print(str_name)
    break
sortedNames = (sorted(nameOfpredzadnji))
for final_result in sortedNames:
    print(final_result)