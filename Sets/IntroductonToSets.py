def average(array):
    setHeights = set(array)
    integers = 0
    for i in setHeights:
        integers += int(i)
    average = integers/len(setHeights)
    return average

numPlants = int(input())
heightsOfPlants = list(input().split())
x = average(heightsOfPlants)
print(x)
