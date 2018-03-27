def swap_case(niz):
    newNiz = ''
    for letter in range(0, len(niz)):
        if niz[letter].strip().istitle() is True:
            change_letter = niz[letter].lower()
            newNiz += change_letter
        else:
            change_letter = niz[letter].upper()
            newNiz += change_letter
    return newNiz
s = input()
convert = swap_case(s)
print(convert)