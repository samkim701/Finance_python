import numpy as np 
a = np.array([1,2,3], dtype='int32')
print(a)
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
# Get Dimension
print(a.ndim)
# Get Shape
print(b.shape)
# Get DataType
print(a.dtype)
# Get Size of Item
print(a.itemsize)
# Get Total Bytes
print(a.nbytes)


c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)
# Get specific element
print(c[0,3])
print(c[1,3])
# Get specific row
print(c[0, :])
# Get specific column
print(c[:, 0])
# Fancy find [startindex:endindex:stepsize]
print(c[0, 1:6:2])
# Assign element
# c[:,2] = 5
print(c)
# 3-D examples
d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)
# get specific element
print(d[:,1,:])

# Initializing Different Types of Arrays
# All 0s matrix
e = np.zeros((2,3,3))
print(e)
# All 1s matrix
f = np.ones((2,3,3), dtype='int32')
print(f)
# Any other number (full like) - mimics same shape and dtype as a
g = np.full_like(a,4)
print(g)
# Identity matrix
h = np.identity(3)
print(h)
# Repeat array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print(r1)
# Task: let's make some cool matrix
output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
output[1:4,1:4] = z
print(output)

# copy array
a_1 = np.array([1,2,3])
b_1 = a_1.copy()  # not just b_1= a_1
b_1[0] = 100
print(a_1)
