import numpy as np

a = np.zeros((2,2))
print("Zeros array a = ",a)

b = np.ones((1,2))
print("Ones Array b = ",b)
c = np.full((2,2), 7)
print("Full array of size (2,2) with 7 c = ",c)

d = np.eye(2)
print("Identity/eye d =",d)

e = np.random.random((2,2))
print("Random array e = ",e)

f = np.arange(10)
print("Arrange array f = ", f)

g = np.linspace(0, 10, 5)
print("G = ",g)