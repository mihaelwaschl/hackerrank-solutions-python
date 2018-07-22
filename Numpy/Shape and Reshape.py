import numpy

array = input().strip().split(' ')
num_array = numpy.array(array, int)
num_array.shape = (3,3)
print(num_array)