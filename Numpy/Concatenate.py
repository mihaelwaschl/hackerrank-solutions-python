import numpy

N, M, P = map(int, input().strip().split(' '))
array1 = [input().strip().split(' ') for _ in range(N)]
array2 = [input().strip().split(' ') for _ in range(M)]
num_arr1 = numpy.array(array1, int)
num_arr2 = numpy.array(array2, int)
result = numpy.concatenate((num_arr1, num_arr2), axis=0)
print(result)