n = int(input())
list = []

for i in range(0,n):
    print(i)
    type_item = input('metoda\n')
    type_item_strip = type_item.lower().strip().split(" ")
    type_item_search = str(type_item_strip[0])
    if type_item_search == 'print':
        print(list)
    elif type_item_search == 'remove':
        num = int(type_item_strip[1])
        list.remove(num)
    elif type_item_search == 'insert':
        key = int(type_item_strip[1])
        val = int(type_item_strip[2])
        list.insert(key, val)
    elif type_item_search == 'append':
        val = int(type_item_strip[1])
        list.append(val)
    elif type_item_search == 'sort':
        list.sort()
    elif type_item_search == 'pop':
        list.pop()
    elif type_item_search == 'reverse':
        list.reverse()






