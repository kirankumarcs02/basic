import numpy as np

D1 = np.array([1,2,3,4,5,6,7,8,9])

print('even num =',D1[D1%2 ==0])


a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx = (a > 2)
print('bool_idx = ',bool_idx)
print('a[bool_idx',a[bool_idx])
print('a[a > 2]',a[a > 2])