# import pandas as pd

data = {"a":[1,2,3,4,5,6,7,8,9], "b":[2,3,4,5,6,7,8,9,2]}
a = pd.DataFrame(data)
print(a)

# Dataframe from the numpy
import numpy as np
import pandas as pd

arr = np.array([[43,12,45],[45,12,22]])
df = pd.DataFrame(arr)
print(df)

#learning new concept reading the data from the excel sheet
import pandas as pd
Da = pd.read_excel("beta.xlsx")
print(Da)
print(Da.columns)

import pandas as pd
data = [['vedant',21],['mwaah',18]]
de =pd.DataFrame(data, columns =["name","marks"])
print(de)

import pandas as pd
df = pd.read_excel("beta.xlsx")
# print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.column())
print(df.shape())

import pandas as pd
import numpy as np

# Method 1: From Dictionary
data = {
    'Employee_ID': [101, 102, 103, 104],
    'Name': ['John', 'Sarah', 'Mike', 'Emma'],
    'Department': ['IT', 'HR', 'IT', 'Finance'],
    'Salary': [75000, 65000, 80000, 70000]
}
df1 = pd.DataFrame(data)
print("Method 1 - Dictionary:\n", df1)

# Method 2: From List of Lists
data_list = [
    [101, 'John', 'IT', 75000],
    [102, 'Sarah', 'HR', 65000],
    [103, 'Mike', 'IT', 80000]
]
df2 = pd.DataFrame(data_list, columns=['Employee_ID', 'Name', 'Department', 'Salary'])
print("\nMethod 2 - List of Lists:\n", df2)

# Method 3: From List of Dictionaries
data_dict_list = [
    {'Employee_ID': 101, 'Name': 'John', 'Department': 'IT'},
    {'Employee_ID': 102, 'Name': 'Sarah', 'Department': 'HR'},
]
df3 = pd.DataFrame(data_dict_list)
print("\nMethod 3 - List of Dictionaries:\n", df3)

# Method 4: Empty DataFrame then add columns
df4 = pd.DataFrame()
df4['Name'] = ['Alice', 'Bob']
df4['Age'] = [25, 30]
print("\nMethod 4 - Empty then Add:\n", df4)

# Method 5: From NumPy Array
arr = np.array([[1, 2, 3], [4, 5, 6]])
df5 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print("\nMethod 5 - NumPy:\n", df5)

# Method 6: With Custom Index
df6 = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print("\nMethod 6 - Custom Index:\n", df6)