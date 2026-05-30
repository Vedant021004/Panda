import pandas as pd
df = pd.read_excel("beta.xlsx")
# print(df)
print(df[['Name', 'Price']])