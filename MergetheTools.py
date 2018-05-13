def merge_the_tools(string, k):
    for i in range(len(string)//k):
        result = ''
        for j in string[i*k:i*k+k]:
            if j not in result:
                result += j
        print(result)

string = input()
k = int(input())
result = merge_the_tools(string,k)
