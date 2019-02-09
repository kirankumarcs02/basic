import numpy as np

a = np.array([1, 2, 3])
print("typr(a)", type(a))
print("a.shape",a.shape)
print("a = ",a[0], a[1], a[2])
a[0] = 5
print("a",a)
b = np.array([[1,2,3],[4,5,6]])
print("b.shape = ",b.shape)
print("b = ",b[0, 0], b[0, 1], b[1, 0])   