import numpy as np

a = np.arange(10)
print(np.clip(a, 1, 8))
print(a)
print(np.clip(a, 3, 6, out=a))
a = np.arange(10)
print(a)
print( np.clip(a, [4,5, 1, 1, 1, 8, 4, 4, 4, 4], 8))