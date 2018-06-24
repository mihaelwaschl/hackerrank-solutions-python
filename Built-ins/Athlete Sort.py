n, m = map(int, input().split())
elements = []
for i in range(n):
    elements.append(list(map(int, input().rstrip().split())))
k = int(input())
sorted_elements = sorted(elements, key= lambda sortby: sortby[k])
for row in sorted_elements:
    for element in row:
        print(element, end=' ')
    print('')



