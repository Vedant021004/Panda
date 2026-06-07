import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
arr = pd.DataFrame(exam_data)
print(len(arr.iloc[:,0]))
print(len(arr.iloc[0,:]))
print(len(arr.axes[0]))
print(len(arr.axes[1]))
print(arr.shape[1])
print(arr[arr['score'].isnull()])
print(arr[(arr['score']>=15) & (arr['score']<=20)])
print(arr[arr['score'].between(15,20)])