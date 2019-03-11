import numpy as np


permutation = np.random.permutation(5)
print("permutation = ", permutation)

a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("a = ", a)
print("a[:,permutation] = ", a[:,permutation])

