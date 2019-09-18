#This script will introduce us to Numpy, a library useful for working with n-dimensional data.
import numpy as np

empty = np.empty(2,2)
print(empty)
print(empty.shape)

filled = np.array([1,2,3,4,5])
print(filled)
print(filled.shape)

zeros = np.zeros((2,2))
identity = np.eye(2)
ones = np.ones((2,2))
constants = np.full((2,2),4)

print(ones[:,0])
print(constants[1,1])
print(constants > 5)

np.add(zeros,ones)
np.subtract(ones,zeros)
ones * zeros
ones / zeros
np.dot(identity,constants)
np.multiply(identity,constants)
np.sqrt(ones)


np.reshape(ones,(-1))
np.tile(ones,4)
np.stack((ones,constants),axis=0)
