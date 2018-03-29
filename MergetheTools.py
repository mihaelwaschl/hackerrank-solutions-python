import textwrap

def merge_the_tools(string, k):
    length = len(string)
    segments = textwrap.fill(string, length//k)
    splited = segments.split('\n')
    print(splited)
    for i in splited:
        result = ''.join(set(i))
        print(result)

string = input()
k = int(input())
result = merge_the_tools(string,k)
