def stringFormating(n):
    w = len(str(bin(n))[2:])
    for i in range(1, n+1):
        decimal = str(i)
        octa = str(oct(i))[2:]
        hexa = str(hex(i))[2:].upper()
        binary = str(bin(i))[2:]
        print('{:>{width}} {:>{width}} {:>{width}} {:>{width}}'.format(decimal, octa, hexa, binary, width = w))

n = int(input())
stringFormating(n)

