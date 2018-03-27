def splitJoin(string):
    splited = string.split(" ")
    joined = "-".join(splited)
    return joined

string = input()
funkcija = splitJoin(string)
print(funkcija)