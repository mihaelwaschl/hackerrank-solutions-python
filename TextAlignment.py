import textwrap
string = input()
width = int(input())

fill = textwrap.fill(string, width)
print(fill)