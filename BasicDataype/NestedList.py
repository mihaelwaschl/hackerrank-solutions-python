list = []
for num_st in range(int(input())):
    name = input()
    point = float(input())
    nested_list = [name, point]
    list += [nested_list]

points = ''
for list_one in list:
    for list_two in list_one:
        str_list_two =str(list_two)
        splited = str_list_two.split(' ')
        print(splited[0])

print(points)