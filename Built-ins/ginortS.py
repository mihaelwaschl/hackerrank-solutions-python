string = input()
lower_case = ''
uper_case = ''
num_evan = ''
num_odd = ''

for letter in string:
    if letter.islower():
        lower_case += letter
    elif letter.isupper():
        uper_case += letter
    elif letter.isdigit():
        if int(letter) % 2 > 0:
            num_odd += letter
        else:
            num_evan += letter

sorted_upper = ''.join(sorted(uper_case))
sorted_odd = ''.join(sorted(uper_case))
print(''.join(sorted(lower_case)) + ''.join(sorted(uper_case)) + ''.join(sorted(num_odd)) + ''.join(sorted(num_evan)))
