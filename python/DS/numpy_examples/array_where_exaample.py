import numpy as np


a = np.array([[1,0,0], [0,0,1], [1,0,0]])

print('a', a)
u, index = np.unique(a, axis=0)
print('u', u)
print('index',index)

print(a[np.where(np.unique(a, axis=0))])

mapping_number = {
    "0": 3,
    "1": 0,
    "2": 3,
    3: 3,
    4: 1,
    5: 3,
    6: 4,
    7: 3,
    8: 2,
    9: 5
}
index = 1;
print('mapping',mapping_number[str(index)])