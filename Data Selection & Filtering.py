import pandas as pd
df = pd.read_excel("beta.xlsx")
print(df)
print(df[['Name', 'Price']])
print(df.loc[1])
print(df.iat[0,0])
print(df[(df['Year']>2016) & (df['Price']>12)])
print(df[df['Price']>1]['Name'])
print(df.query("Year > 2012"))
print(df['Name'],['Price'])

import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['NYC', 'LA', 'Chicago', 'NYC', 'Boston'],
    'Salary': [70000, 80000, 75000, 65000, 90000],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR']
})

# print("Original DataFrame:\n", df)

# # === COLUMN SELECTION ===
# print("\n1. Single Column (Series):")
# print(df['Name'])

# print("\n2. Multiple Columns (DataFrame):")
# print(df[['Name', 'Age']])

# # === ROW SELECTION ===
# print("\n3. First 3 rows:")
# print(df.head(3))

# print("\n4. Last 2 rows:")
# print(df.tail(2))

# print("\n5. Rows by position (iloc):")
# print(df.iloc[1:4])  # Rows 1, 2, 3

# print("\n6. Rows by label (loc):")
# print(df.loc[0:2])  # Rows 0, 1, 2 (inclusive)

# # === CONDITIONAL SELECTION ===
# print("\n7. Age > 28:")
# print(df[df['Age'] > 28])

# print("\n8. City is NYC:")
# print(df[df['City'] == 'NYC'])

# print("\n9. Multiple conditions (AND):")
# print(df[(df['Age'] > 28) & (df['Department'] == 'IT')])

# print("\n10. Multiple conditions (OR):")
# print(df[(df['City'] == 'NYC') | (df['City'] == 'LA')])

# print("\n11. NOT condition:")
# print(df[~(df['City'] == 'NYC')])  # ~ is NOT operator

# print("\n12. Using isin():")
# print(df[df['City'].isin(['NYC', 'LA'])])

# # === ADVANCED SELECTION ===
# print("\n13. Select specific rows and columns with loc:")
# print(df.loc[0:2, ['Name', 'Salary']])

# print("\n14. Select with iloc (position-based):")
# print(df.iloc[0:3, 0:2])  # First 3 rows, first 2 columns

# print("\n15. Select single cell:")
# print(df.loc[0, 'Name'])  # Using label
# print(df.iloc[0, 0])      # Using position

# print("\n16. Select where Salary is maximum:")
# print(df[df['Salary'] == df['Salary'].max()])

# print("\n17. Select using query():")
# print(df.query('Age > 28 and Department == "IT"'))

# print("\n18. Boolean indexing with multiple conditions:")
# mask = (df['Age'] > 28) & (df['Salary'] > 70000)
# print(df[mask])

# Q16. Select the 'Name' column from a DataFrame.
import pandas as pd
print(df['Name'])

print(df[['Name','Age']])

# Q18. Select the first 5 rows of a DataFrame.
import pandas as pd
df1 = df.head(5)
print(df1)

# Q19. Select rows from index 2 to 5 using iloc.
import pandas as pd
brr = df.iloc[2:5]
print(brr)

# Q20. Select rows where Age is greater than 25.
import pandas as pd
greater = df[df['Age']>25]
print(greater)

# Q21. Select rows where City is 'NYC' and Age > 30.
import pandas as pd
sel = df[(df['City']=='NYC') & (df['Age']>30)]
print(sel)

# Q22. Select rows where Department is either 'IT' or 'HR'.
import pandas as pd 
dep = (df['Department']=='IT') | (df['Department']=='HR')
print(dep)


# Q23. Select all rows where Salary is NOT equal to 70000.
import pandas as pd
salary = [df[~df['Salary']==70000]]
print(salary)

# Q24. Select the 3rd row and 2nd column value using iloc.
import pandas as pd
row = df.iloc[0:3,0:2]
print(row)

# Q25. Select rows 1-3 and columns 'Name' and 'Salary' using loc.
import pandas as pd
roow = df.loc[1:3,['Name','Salary']]
print(roow)

# Q26. Select all rows where Name starts with 'A'.
import pandas as pd
we = df[df["Name"].str.startswith("A")]
print(we)

# Q27. Select rows where Age is between 25 and 30 (inclusive).
import pandas as pd
umr = df[(df['Age']>=25 ) & (df['Age']<=30)]
print("umr is ",umr)

# Q28. Select the row with the maximum Salary.
import pandas as pd
maas = df[(df['Salary'])==(df['Salary'].max())]
print(maas)

# Q29. Select the last 3 rows and first 2 columns.
import pandas as pd
last = df.iloc[-3:, :2]

# Q30. Select rows where City is in the list ['NYC', 'LA', 'Boston'].
import pandas as pd
foud = df["City"].isin(["NYC", "LA", "Boston"])
print(foud)

# Q31. Select all rows except where Department is 'HR'.
import pandas as pd
select = df[df["Department"] != "HR"]
print(select)