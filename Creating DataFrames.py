# # import pandas as pd

# data = {"a":[1,2,3,4,5,6,7,8,9], "b":[2,3,4,5,6,7,8,9,2]}
# a = pd.DataFrame(data)
# print(a)

# # Dataframe from the numpy
# import numpy as np
# import pandas as pd

# arr = np.array([[43,12,45],[45,12,22]])
# df = pd.DataFrame(arr)
# print(df)

# #learning new concept reading the data from the excel sheet
# import pandas as pd
# Da = pd.read_excel("beta.xlsx")
# print(Da)
# print(Da.columns)

# import pandas as pd
# data = [['vedant',21],['mwaah',18]]
# de =pd.DataFrame(data, columns =["name","marks"])
# print(de)

# import pandas as pd
# df = pd.read_excel("beta.xlsx")
# # print(df)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.column())
# print(df.shape())

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

# Q1. Create a DataFrame with 3 students: names (Amy, Ben, Chris), ages (20, 22, 21), and grades (85, 90, 88).
import pandas as pd
kunji = [
    {'name':'Amy', 'age':20, 'grades':85},
    {'name':'Ben', 'age':22, 'grades':90},
    {'name':'chris', 'age':21, 'grades':88}
]
kashishkapil = pd.DataFrame(kunji)
print(kashishkapil)

# Q2. Create a DataFrame from a list of lists with products: [['Laptop', 1000], ['Mouse', 25], ['Keyboard', 75]] with columns 'Product' and 'Price'.
import pandas as pd
data = [['Laptop', 1000], 
        ['Mouse', 25],
        ['Keyboard', 75]] 

df = pd.DataFrame(data)
print(df)

# Q3. Create an empty DataFrame and then add columns 'City' and 'Population' with 3 cities of your choice
import pandas as pd
data = []
df = pd.DataFrame()
df['name'] = ['a','b']
df['age'] = [21,22]
print(df)

# Q4. Create a DataFrame from this dictionary: {'A': [1, 2, 3], 'B': [4, 5, 6]} with custom index ['x', 'y', 'z'].

import pandas as pd
data = {
    'A': [1,2,3],
    'B': [4,5,6]
}
df = pd.DataFrame(data, index=['X','Y','Z'])
print(df)

# Q5. Create a DataFrame from a NumPy array of shape (4, 3) with random integers between 1-100
import numpy as np
import pandas as pd
# arr1 = np.random(size=(4,3))
rng = np.random.default_rng()
arr = rng.integers(low=1, high=100, size=(3, 5))
print(arr)
df = pd.DataFrame(arr)
print(df)


import pandas as pd
fruits = {
    'Apples':[35,21],
    'Bananas':[45,24],
    
    
}
q1 = pd.DataFrame(fruits,index=["2017 Sales","2018 Sales"])
print(q1)


