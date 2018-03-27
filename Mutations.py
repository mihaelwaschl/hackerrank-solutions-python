def mutate_string(string, position, character):
    newString = ''
    listedString = list(string)
    listedString[position-1] = character
    newString += ''.join(listedString)
    return newString

s = input()
i, c = input().split()
spremenljivka = mutate_string(s, int(i), c)
print(spremenljivka)
