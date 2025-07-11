import numpy as np
#Linear Algebra
a = np.ones((2,3))
print(a)
b = np.full((3,2), 2)
print(b)
#a*b doesn't work
#Multiply
print(np.matmul(a,b))
#Find the determinant
c = np.identity(3)
print(np.linalg.det(c))

#Statistics
stats = np.array([[1,2,3],[4,5,6]])
print(stats)
print(np.min(stats))
print(np.min(stats, axis=1))
print(np.max(stats))
print(np.sum(stats, axis=0))

#Reorganizing Arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after = before.reshape((8,1))
print(after)

#Vertically Stacking Vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2,v1,v2]))
#Horizontally Stacking Vectors
print(np.hstack([v1,v2,v1,v2]))

#Miscellaneous
filedata = np.genfromtxt('data.txt', delimiter=',')
filedata.astype('int32')
print(filedata)