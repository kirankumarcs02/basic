import numpy as np

a = np.random.randn(4, 3)
b = np.random.randn(3, 2)
c = np.dot(a,b)

print(c.shape)

aa = np.random.randn(4, 3) # a.shape = (4, 3)
bb = np.random.randn(3, 2) # b.shape = (3, 2)
# cc = aa*bb 

ab = np.random.randn(2, 3) # a.shape = (2, 3)
bc = np.random.randn(2, 1) # b.shape = (2, 1)
ca = ab + bc

print(ca.shape)