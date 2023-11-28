import array as arr
import numpy as np

# Fixed-Type Arrays in Python

L = arr.array('i', [1, 2, 3, 4, 5, 6])  # 'i' is a type code indicating the contents are integers.
print(L)

# Fixed-Types Arrays using numPY

n1 = np.array([10, 20, 30, 40, 50])
print(n1)

n3 = np.array(["Hello", "Hi", "Hey", "Hola"], dtype=str)
print(n3.dtype)

'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
'''

#______________________________________

n2 = np.array([ 1, 2, 3, 4, 5, 6])
print("Heterogeneous List :-", n2.dtype)

'''
NumPy is constrained to arrays that all contain the same type. If types do not match, NumPy will upcast if possible
here, integers are up-cast to floating point:
'''


n5 = np.array([3.14, 4, 2, 3])
print("Type Casting :-", n5)


# MultiDimensional Array
n6 = np.array([[2, 3, 4],
               [4, 5, 6],
               [6, 7, 8]])
print("MultiDimensional Array :- ")
print(n6)
