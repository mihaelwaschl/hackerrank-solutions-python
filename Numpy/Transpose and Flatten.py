import numpy

n, m = input().strip().split(' ')
array = [input().split(' ') for _ in range(int(n))]
numpy_array = numpy.array(array, int)
trans_array = numpy.transpose(numpy_array)
flatten_array = numpy_array.flatten()
print(trans_array)
print(flatten_array)