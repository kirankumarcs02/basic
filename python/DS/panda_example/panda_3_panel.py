import pandas as pd
import numpy as np

print('--------Create Panel--------')
data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)

print('---------From dict of DataFrame Objects---------------')

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)

print('--------Selecting the Data from Panel Using Items---------')
print('Item1')
print(p['Item1'])
print('Item2')
print(p['Item2'])

print('-----------Using major_axis---------------')
print(p.major_xs(1))

print('----------Using minor_axis -----------------')
print(p.minor_xs(1))
