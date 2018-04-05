sizeK = int(input())
roomNumbers =list(map(int, input().split()))
sumRomNumbers = sum(roomNumbers)
sumSetRoomNumbers = sum(set(roomNumbers))*sizeK
difference = sumSetRoomNumbers-sumRomNumbers
for i in roomNumbers:
    if difference == ((sizeK-1)*i):
        print(i)
        break
