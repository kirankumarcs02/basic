import numpy as np

my_array = np.array([1,2,3,4,5,6,7,8,9,10])
# reverse
print(my_array[::-1])

print(my_array[::2])

print(my_array[1::2])

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

b = a[:2, 1:3]
print()
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Pr
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print('col_r1',col_r1, col_r1.shape)
print('col_r2',col_r2, col_r2.shape)

D2 = np.array([[1,2], [3, 4], [5, 6]])
print('D2 = ',D2)
print('D2[[0, 1, 2], [0, 1, 0]] = ',D2[[0, 1, 2], [0, 1, 0]])
print('np.array([D2[0, 0], D2[1, 1], D2[2, 0]]) = ', np.array([D2[0, 0], D2[1, 1], D2[2, 0]]))
print('D2[[0, 0], [1, 1]] = ', D2[[0, 0], [1, 1]])
print('np.array([D2[0, 1], D2[0, 1]]) = ',np.array([D2[0, 1], D2[0, 1]]))