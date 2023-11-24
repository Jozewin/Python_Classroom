import numpy as np

np.random.seed(0)

num1 = np.random.randint(30, size=6)

print("num 1 :-")
print(num1)

# Index accessing using one-dimensional array
# Syntax => arrayName[index]
print("num1[0] :-", num1[0])
print('num1[5] :-', num1[5])

# to index from the end of the array, you can use negative indices:

print("num1[-1] :-", num1[-1])
print('num1[-2] :-', num1[-2])

num2 = np.random.randint(30, size=(3, 3))
print("\nnum 2 :-")
print(num2)
# Index accessing using two-dimensional array
# Syntax => arrayName[row][column]

print("num2[0][0] :-", num2[0][0])
print('num2[1][2] :-', num2[1][2])

# Changing values using index
num2[0, 0] = 99
print("\nnum 2 :-")
print(num2)
