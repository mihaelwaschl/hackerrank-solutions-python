def capitalize(name):
    name_splited = name.split(' ')
    fulNameCap = ''
    for i in name_splited:
        cap = i.capitalize()
        fulNameCap += cap+' '
    return fulNameCap


n = input()
p = capitalize(n)
print(p)