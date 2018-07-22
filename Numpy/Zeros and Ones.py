import numpy

num = tuple(map(int,input().split()))
array_zeros = numpy.zeros((num), dtype=numpy.int)
array_ones = numpy.ones((num), dtype=numpy.int)
print(array_zeros)
print(array_ones)