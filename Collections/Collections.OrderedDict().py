from collections import OrderedDict

ordered_dictionary = OrderedDict()
num_item = int(input())

for i in range(0,num_item):
    item, price = input().rsplit(' ', 1)
    if item in ordered_dictionary:
        ordered_dictionary[item] += int(price)
    else:
        ordered_dictionary[item] = int(price)

for j in ordered_dictionary:
    print(j +' '+ str(ordered_dictionary[j]))
