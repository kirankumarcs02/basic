import numpy as np 
a = np.arange(8).reshape(2,4) 

print('The original array is:')
print(a)

print('After applying ravel function:' )
print(a.ravel())

print('Applying ravel function in F-style ordering:')
print(a.ravel(order = 'F'))

print('List',a.ravel().tolist())