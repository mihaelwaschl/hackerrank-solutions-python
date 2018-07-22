import numpy

array = input().strip().split(' ')
def arrays(arr):
    convert_float = numpy.array(arr[::-1], float)
    return convert_float
print(arrays(array))