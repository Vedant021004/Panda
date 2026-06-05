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




