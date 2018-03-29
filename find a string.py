def count_substring(string, sub_string):
    result = 0
    for i in range(0,len(string)):
        found = string[i:i+len(sub_string)]
        if found == sub_string:
            result += 1
    return result

string = input()
sub_string = input()
count = count_substring(string, sub_string)
print(count)

