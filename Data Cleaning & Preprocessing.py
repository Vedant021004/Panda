import pandas as pd
df = pd.read_csv("data_cleaning_sample.csv")
print(df)
# print(df.isnull())
# print(df.isnull().sum())
# print(df.dropna())              # Drop rows with *any* missing values
# print(df.dropna(axis=1))      # Drop columns with missing values
# print(df.fillna(1))
print(df.duplicated())         # True for duplicates
print(df.drop_duplicates())     # Remove duplicate rows)