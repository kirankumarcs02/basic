import numpy as np
from numpy.random import randint
from numpy import argmax
from keras.utils.np_utils import to_categorical

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

z = np.zeros((360, 1232))
print(z)


k = 8
n = 20
x = randint(0, k, (n,))
print(x)
print((to_categorical(x, k)))