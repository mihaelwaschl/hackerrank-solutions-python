numberStamps = int(input())
listCountry =list()
for i in range(0,numberStamps):
    country = input()
    listCountry.append(country)
setListCountry = set(listCountry)
lengthSet = len(setListCountry)

print(lengthSet)