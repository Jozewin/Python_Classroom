'                                                                   UFuncs -> Universal Functions                                                   '
import numpy as np

np.random.seed(0)


def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output


values = np.random.randint(1, 10, size=5)
print("Array is ", values)
print(compute_reciprocals(values))
print(1.0 / values)


big_array = np.random.randint(1, 100, size=1000000)
print(compute_reciprocals(big_array))
print(1.0 / big_array)
#%timeit compute_reciprocals(big_array)
#%timeit (1.0 / big_array)


'''
Operation between two array is also possible
'''

print("Operation between two array :- ",np.arange(5) / np.arange(1, 6))


'''
ufunc operations are not limited to one-dimensional arrays–they can also act on multi-dimensional arrays as well
'''