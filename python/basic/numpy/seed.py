import numpy as np

np.random.seed(0)
a = np.random.randn(2, 3)
np.random.seed(0)
b = np.random.randn(2, 3)

print(a)
print('b', b)
