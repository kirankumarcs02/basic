import numpy as np
import pandas as pd

submission_new = pd.read_csv('submission_new.csv') # file name

submission_2 = pd.read_csv('submission_2.csv')

print(submission_new.head())
difference = 0
mergedStuff = pd.merge(submission_new, submission_2, on=['id'], how='inner')
print(mergedStuff.head())
print(mergedStuff['label_x'][0])
for i in range(5000):
    if mergedStuff['label_x'][i] != mergedStuff['label_y'][i] :
        print('ID', i)
        difference +=1

print(difference)
