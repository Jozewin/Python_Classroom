import numpy as np

'''
seed with a set value in order to ensure that the same random arrays are generated each time this code is run:
np.random.seed(0) will generate set of same random values everytime we run the code
changing the seed will change the output result but the output will be same for that respective seed
'''
np.random.seed(0)
random_array = np.random.rand(3,3)

print("random array:", random_array)


# randint(endPoint, size)  => random Integer
x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print("x1 :- ", x1)
print("x2 :- ", x2)
print("x3 :- ", x3)

'''
ndim => the number of dimensions
shape => the size of each dimension
size => the total size of the array
dtype => the data type of the array 
itemsize => which lists the size (in bytes)
nbytes => which lists the total size (in bytes) of the array:
'''

print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
print("dtype:", x3.dtype)
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")

