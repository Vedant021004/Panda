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
