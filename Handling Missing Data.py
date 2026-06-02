import pandas as pd
import numpy as np

# Create DataFrame with missing values
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None, 'David', 'Eve', 'Frank'],
    'Age': [25, 30, np.nan, 28, np.nan, 35],
    'Salary': [70000, np.nan, 75000, 65000, 90000, None],
    'Department': ['IT', 'HR', 'IT', None, 'HR', 'Finance'],
    'Experience': [2, 5, np.nan, 3, 7, 10]
})

# print("DataFrame with Missing Values:\n", df)

# # === DETECTING MISSING VALUES ===
# print("\n1. Check for null values (boolean):")
# print(df.isnull())

# print("\n2. Check for NOT null values:")
# print(df.notnull())

# print("\n3. Count missing values per column:")
# print(df.isnull().sum())

# print("\n4. Total missing values:")
# print(df.isnull().sum().sum())

# print("\n5. Percentage of missing values:")
# print((df.isnull().sum() / len(df)) * 100)

# print("\n6. Rows with any missing value:")
# print(df[df.isnull().any(axis=1)])

# print("\n7. Info about missing data:")
# print(df.info())

# # === DROPPING MISSING VALUES ===
# print("\n8. Drop rows with ANY missing value:")
# print(df.dropna())

# print("\n9. Drop rows where ALL values are missing:")
# df_test = df.copy()
# df_test.loc[6] = [None, None, None, None, None]
# print(df_test.dropna(how='all'))

# print("\n10. Drop rows with missing values in specific column:")
# print(df.dropna(subset=['Age']))

# print("\n11. Drop columns with any missing value:")
# print(df.dropna(axis=1))

# print("\n12. Drop rows with at least 2 missing values:")
# print(df.dropna(thresh=4))  # Keep rows with at least 4 non-null values

# # === FILLING MISSING VALUES ===
# print("\n13. Fill all missing with 0:")
# print(df.fillna(0))

# print("\n14. Fill with specific value per column:")
# print(df.fillna({'Age': 0, 'Salary': 50000, 'Name': 'Unknown'}))

# print("\n15. Fill with mean (numeric columns):")
# print(df['Age'].fillna(df['Age'].mean()))

# print("\n16. Fill with median:")
# print(df['Salary'].fillna(df['Salary'].median()))

# print("\n17. Fill with mode (most frequent):")
# print(df['Department'].fillna(df['Department'].mode()[0]))

# print("\n18. Forward fill (use previous value):")
# print(df.fillna(method='ffill'))

# print("\n19. Backward fill (use next value):")
# print(df.fillna(method='bfill'))

# print("\n20. Interpolate (for numerical data):")
# print(df['Age'].interpolate())

# print("\n21. Fill with a calculated value:")
# df['Salary'].fillna(df['Salary'].mean() * 0.8, inplace=True)
# print(df)

# # === REPLACING VALUES ===
# print("\n22. Replace specific values:")
# df_copy = df.copy()
# df_copy.replace(np.nan, 'MISSING', inplace=True)
# print(df_copy)

# print("\n23. Replace in specific column:")
# df['Department'].replace(np.nan, 'Unassigned', inplace=True)
# print(df)

# # === ADVANCED TECHNIQUES ===
# print("\n24. Fill missing values using groupby:")
# df_advanced = pd.DataFrame({
#     'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
#     'Salary': [70000, np.nan, 75000, 65000, np.nan]
# })
# df_advanced['Salary'] = df_advanced.groupby('Department')['Salary'].transform(
#     lambda x: x.fillna(x.mean())
# )
# print(df_advanced)

# Q56. Detect all missing values in a DataFrame.
# import pandas as pd
# missing = df.isnull()
# print(missing)

# # Q57. Count the total number of missing values in each column.
# import pandas as pd
# miss = df.isnull().sum()
# print(miss)

# # Q58. Find the percentage of missing values per column.
# import pandas as pdd
# per = (df.isnull().sum() /len(df))*100
# print(per)

# # Q59. Drop all rows that contain any missing value.
# import pandas as pd
# dfg = df.dropna()
# print(dfg)

# # Q60. Drop rows where 'Age' column is missing.
# import pandas as pd
# missi = df.dropna(subset=['Age'])
# print(missi)

# # Q61. Drop columns that have more than 50% missing values.
# missing_percent = df.isnull().mean() * 100
# print(missing_percent)

# # Q62. Fill all missing values with 0.
# import pandas as pd
# missu = df.fillna(0)
# print(missu)

# # Q63. Fill missing values in 'Age' column with the mean age.
# import pandas as pd
# fill = df['Age'].fillna(df['Age'].mean())
# print(fill)

# Q66. Use forward fill to fill missing values.
import pandas as pd
fg = df.ffill()
print(fg)
gf = df.bfill()
print(gf)