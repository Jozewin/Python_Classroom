import numpy as np

np.random.seed(0)
x2 = np.random.randint(10, size=(3, 4))

print(x2)

# Creating 2x2 matrix from x2
x2Sub = x2[:2, :2]
print(x2Sub)

# Now if we modify this subarray, we'll see that the original array is changed! Observe:
x2Sub[0, 0] = 99
print(x2Sub)

#Value will be changed in x2 also
print(x2)

'''
This default behavior is actually quite useful: 
it means that when we work with large datasets,
we can access and process pieces of these datasets without the need to copy the underlying data buffer.
'''