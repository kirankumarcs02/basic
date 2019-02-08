import numpy as np

np.random.seed(1)
a = np.random.randn(2, 3)
np.random.seed(0)
b = np.random.randn(2, 3)
np.random.seed(2)
c = np.random.randn(12)*0.01

print('a',a)
print('b', b)
print('c', c)


np.random.seed(1)
d = np.random.randn(2, 3)
np.random.seed(0)
e = np.random.randn(2, 3)
np.random.seed(2)
f = np.random.randn(2, 3)

print('d', d)
print('e', e)
print('f', f)

