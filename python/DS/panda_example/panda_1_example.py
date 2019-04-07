import pandas as pd
import numpy as np

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(data)
print(s)
print('-------------------------------')
s_index =  pd.Series(data,index=[100,101,102,103])

print(s_index)

print('--------------------------------')
print('dict :')
dict = {'a' : 0., 'b' : 1., 'c' : 2.}
s_dict = pd.Series(dict)

print(s_dict)
print('----------------------------------')

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)
print('------------------------------------')

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print('first element: s[0] = ', s[0])
print('first 3 element: s[:3] = ', s[:3])
print('last 3 element: s[-3:]', s[-3:])
print('s[''a''] = ' , s['a'])
