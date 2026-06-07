# Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
import pandas as pd
arr = pd.Series([1,2,3,4,5,])
print(arr)

# Write a Pandas program to convert a Panda module Series to Python list and it's type.
import pandas as pd
arr = pd.Series([12,34,21,42])
print(arr)
print(arr.tolist())

# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
import pandas as pd
def add():
    arr = pd.Series([2,4,6,8])
    arr1 = pd.Series([1,3,5,7,9])
    return arr+arr1
result = add()
print(result)

# Write a Pandas program to compare the elements of the two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
import pandas as pd
arr1 = pd.Series([2,4,6,8,10])
brr = pd.Series([1,3,5,7,10])
print(arr1==brr)
print(arr1<brr)
print(arr1>brr)

# Write a Pandas program to convert a dictionary to a Pandas series.
import pandas as pd
arr = {
    'a':100,
    'b':200,
    'c':300,
    'd':400,
    'e':500
}
print(pd.Series(arr))


# Write a Pandas program to convert a NumPy array to a Pandas series.
import pandas as pd
arr = [10,20,30,40,50]
print(pd.Series(arr))

# Write a Pandas program to convert the first column of a DataFrame as a Series.
import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)

print("Original DataFrame")
print(df)

# Using iloc
s1 = df.iloc[:, 0]

# Alternatively, you can directly reference the column by name
#s1 = df['col1']

print("\n1st column as a Series:")
print(s1)
print(type(s1)) 

# Write a Pandas program to convert a given Series to an array.
import pandas as pd
import numpy as np
arr = pd.Series([100,200,"python",300.12,400])
print(arr)
print(np.array(arr))

# Write a Pandas program to convert Series of lists to one Series.
import pandas as pd
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print("Original Series of list")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s)


# Write a Pandas program to sort a given Series.
import pandas as pd
arr = pd.Series(['100','200',"python",'300.12','400'])
print(pd.Series(arr).sort_values())
print(arr)

# Write a Pandas program to add some data to an existing Series.
import pandas as pd  
arr = pd.Series(['100','200',"python",'300.12','400'])

arr = pd.concat([arr, pd.Series(['500',"php"])])
print(arr)


import pandas as pd
s = pd.Series([0,1,2,3,4,5,6,7,8,9,10])
print("Original Data Series:")
print(s)
print("\nSubset of the above Data Series:")
n = 6
new_s = s[s < n]
print(new_s)


# Write a Pandas program to create the mean and standard deviation of the data of a given Series.
import pandas as pd
arr = pd.Series(['1','2','3','8','9','5','3'], dtype=int)
print(arr.mean())
print(arr.std())

# Write a Pandas program to get the items of a given series not present in another given series.
import pandas as pd
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
result = [x for x in sr1 if x not in sr2] #IT CHECKS ONLY INDEXING 

print(result) #IT WILL PRINT WHICH INDEX IS NOT PRESENT INSIDE THE SR1 AND SR2
result1 = [x for x in sr1 if x not in sr2.values]

print(result1)  #THE PRINTED RESULT IS IN THE ARRAY
print(pd.Series(result1))

print(sr1.isin(sr2))
print(~sr1.isin(sr2))
result2 = sr1[~sr1.isin(sr2)]
print(result2)

# Write a Pandas program to get the items which are not common of two given series.
import pandas as pd
arr = pd.Series([1,2,3,4,5])
arr1 = pd.Series([2,4,6,8,10])
result = [x for x in arr if x not in arr1.values] + [x for x in arr1 if x not in arr.values]
print(result)

# Write a Pandas program to get the items which are not common of two given series.
import pandas as pd
arr = pd.Series([1,2,3,4,5,6,10])
result = [x for x in arr if x%5==0]
result1 = arr[arr%5==0]
print(result)
print(result1)


# Write a Pandas program to extract items at given positions of a given series.
import pandas as pd
num_series = pd.Series(list('2390238923902390239023'))
element_pos = [0, 2, 6, 11, 21]
print("Original Series:")
print(num_series)
result = num_series.take(element_pos)
print("\nExtract items at given positions of the said series:")
print(result)



import pandas as pd
data = pd.Series([10, 20, 30, 40, 50, 60, 70])

print("Original Series:")
print(data)

positions = [0, 3, 5]

result = data.iloc[positions]
result2 = data.loc[positions]

print("\nItems at given positions:")
print(result)
print(result2)

s = pd.Series([10,20,30,40,50])

print(
    s.where(s.isin([20,40]))
)

# Write a Pandas program to convert year-month string to dates adding a specified day of the month.
import pandas as pd
from dateutil.parser import parse
date_series = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
print("Original Series:")
print(date_series)
print("\nNew dates:")
result = date_series.map(lambda d: parse('11 ' + d))
print(result)
result1 = pd.to_datetime(date_series) + pd.offsets.Day(10)
print(result1)
