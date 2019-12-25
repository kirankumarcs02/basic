import numpy as np

# /Create a 1D array of numbers from 0 to 9

arr = np.arange(10)

print(arr)


# Q. Create a 3×3 numpy array of all True’s

print('3×3 numpy array',np.full((3, 3), True, dtype=bool))

# Alternate method:
print('3×3 numpy array',np.ones((3,3), dtype=bool))


# Q. Extract all odd numbers from arr

# Input
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Solution
print(arr[arr % 2 == 1])
#> array([1, 3, 5, 7, 9])



# Q. Replace all odd numbers in arr with -1

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 == 1] = -1

print('odd number replace with -1', arr)

# Q. Replace all odd numbers in arr with -1 without changing arr

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print('arr', arr)
print('out', out)

# https://www.machinelearningplus.com/python/101-numpy-exercises-python/

