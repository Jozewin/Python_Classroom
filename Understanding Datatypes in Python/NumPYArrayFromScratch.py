import numpy as np
#                           Creating Arrays From Scratch

# Create a length-10 integer array filled with zeros
n1 = np.zeros(10, dtype=int)
print('n1 :- ', n1)


# Create a 3x5 floating-point array filled with ones
n2 = np.ones((3, 5), dtype=float)
print('n2 :- ', n2)


# Create a 3x5 array filled with 3.14
n3 = np.full((3, 5), 3.14)
print('n3 :- ', n3)


# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
n4 = np.arange(0, 20, 2)
print('n4 :- ', n4)


