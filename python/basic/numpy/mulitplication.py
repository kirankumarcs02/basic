import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7, 8]])
print('input', a)
print('dot product', np.dot(a, a.T))
print('np.multiply ', np.multiply(a,a))

print('sum ', np.sum(np.multiply(a,a)) )
