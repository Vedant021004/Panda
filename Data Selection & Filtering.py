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

print("Original DataFrame:\n", df)

# === COLUMN SELECTION ===
print("\n1. Single Column (Series):")
print(df['Name'])

print("\n2. Multiple Columns (DataFrame):")
print(df[['Name', 'Age']])

# === ROW SELECTION ===
print("\n3. First 3 rows:")
print(df.head(3))

print("\n4. Last 2 rows:")
print(df.tail(2))

print("\n5. Rows by position (iloc):")
print(df.iloc[1:4])  # Rows 1, 2, 3

print("\n6. Rows by label (loc):")
print(df.loc[0:2])  # Rows 0, 1, 2 (inclusive)

# === CONDITIONAL SELECTION ===
print("\n7. Age > 28:")
print(df[df['Age'] > 28])

print("\n8. City is NYC:")
print(df[df['City'] == 'NYC'])

print("\n9. Multiple conditions (AND):")
print(df[(df['Age'] > 28) & (df['Department'] == 'IT')])

print("\n10. Multiple conditions (OR):")
print(df[(df['City'] == 'NYC') | (df['City'] == 'LA')])

print("\n11. NOT condition:")
print(df[~(df['City'] == 'NYC')])  # ~ is NOT operator

print("\n12. Using isin():")
print(df[df['City'].isin(['NYC', 'LA'])])

# === ADVANCED SELECTION ===
print("\n13. Select specific rows and columns with loc:")
print(df.loc[0:2, ['Name', 'Salary']])

print("\n14. Select with iloc (position-based):")
print(df.iloc[0:3, 0:2])  # First 3 rows, first 2 columns

print("\n15. Select single cell:")
print(df.loc[0, 'Name'])  # Using label
print(df.iloc[0, 0])      # Using position

print("\n16. Select where Salary is maximum:")
print(df[df['Salary'] == df['Salary'].max()])

print("\n17. Select using query():")
print(df.query('Age > 28 and Department == "IT"'))

print("\n18. Boolean indexing with multiple conditions:")
mask = (df['Age'] > 28) & (df['Salary'] > 70000)
print(df[mask])