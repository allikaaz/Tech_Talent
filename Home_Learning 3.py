import numpy as np
#Q1
array_1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(array_1)
#Q2
c = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]], dtype='b')
print(c)
#Q3
array_2 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array_2[::2])
#Q5
d = np.array([1,2,3,4,5,6])
e = d.reshape(2,3)
print(e)
#Q6
a = np.array([2,4,5])
b = np.array([6,7,8])
f = np.dot(a, b)
print(f)
g = np.sum(f)
print(g)