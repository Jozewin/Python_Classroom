#Exploring NumPy's UFuncs

'''
Ufuncs exist in two Types:
 -> unary ufuncs - which operate on a single input
 -> binary ufuncs, which operate on two inputs
'''

import numpy as np

np.random.seed(0)

' Basic Arithmetic Operations '
x = np.arange(4)

print("The array is ", x)
print("\n\nx + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)  # floor division


print("-x     = ", -x)
print("x ** 2 = ", x ** 2)

'''
Each of these arithmetic operations are simply convenient wrappers around specific functions built into NumPy;
for example, the + operator is a wrapper for the add function:
'''
print(np.add(x, 10))

#Arithmetic operations
'''
+ 	np.add 	            Addition (e.g., 1 + 1 = 2)
- 	np.subtract 	    Subtraction (e.g., 3 - 2 = 1)
- 	np.negative 	    Unary negation (e.g., -2)
* 	np.multiply     	Multiplication (e.g., 2 * 3 = 6)
/ 	np.divide   	    Division (e.g., 3 / 2 = 1.5)
// 	np.floor_divide 	Floor division (e.g., 3 // 2 = 1)
** 	np.power 	        Exponentiation (e.g., 2 ** 3 = 8)
% 	np.mod          	Modulus/remainder (e.g., 9 % 4 = 1)
'''

#Absolute value

'''Just as NumPy understands Python's built-in arithmetic operators, it also understands Python's built-in absolute 
value function:'''


x = np.array([-2, -1, 0, 1, 2])
print("\n\n",abs(x))
print(np.absolute(x))
print(np.abs(x))    # Those three functions does the same operations

'Trigonometric Operations'

theta = np.linspace(0, np.pi, 3)
print("\n\ntheta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

'''
The values are computed to within machine precision, which is why values that should be zero do not always hit 
exactly zero. Inverse trigonometric functions are also available:
'''

x = [-1, 0, 1]
print("x         = ", x)
print("\n\narcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("arctan(x) = ", np.arctan(x))


'       Exponents and logarithms       '

y = [1, 2, 3]
print("\n\nx     =", y)
print("e^x   =", np.exp(y))
print("2^x   =", np.exp2(y))
print("3^x   =", np.power(3, y))

x = [1, 2, 4, 10]
print("\n\nLog array x        =", x)
print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))


