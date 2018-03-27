def minionGame(string):
    splitedString = string.strip()
    kevinPoints = 0
    stuartPoints = 0
    s_length = len(string)
    vowels = ('A','E','I', 'O','U')
    for i in range(s_length):
        if string[i] in vowels:
            kevinPoints += s_length -i
        else:
            stuartPoints += s_length-i
    if kevinPoints == stuartPoints:
        print('Draw')
    elif kevinPoints < stuartPoints:
        print('Stuart ' + str(stuartPoints))
    elif kevinPoints > stuartPoints:
        print('Kevin ' + str(kevinPoints))

string = input()
minionGame(string)
