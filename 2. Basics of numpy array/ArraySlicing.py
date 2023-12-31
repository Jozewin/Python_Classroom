import numpy as np

# x[start:stop-1:step]

'''
start=0
stop=size of dimension
step=1
'''

x = np.arange(10)
print("x :-", x)

print("First five elements :-", x[:5])
print("Elements after index 5 :-", x[5:7])
print("Middle sub-array", x[1:4])
print("Step of 2 :-", x[::2])
print("Step of 2 but starting from 1 :-", x[0::2])

'         Reversing       '

print("To print reverse :-", x[::-1])

'''          Multi-dimensional subarray         '''

np.random.seed(0)
x2 = np.random.randint(10, size=(4, 4))

print("\n\nx2 :- ", x2)

print("     Array Slicing Operations        ")

print("Two rows and three columns :- ", x2[0:2,0:3])
print("All rows and step 2", x2[:3, ::2])
print("Reversing two dimensional array :- ", x2[::-1, ::-1])
