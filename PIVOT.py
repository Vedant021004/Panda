import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("expense_data.csv")
arr = pd.read_csv("titanic.csv")


# df = sns.load_dataset('tips')
# df.head()
# arr = df.pivot_table(index='sex',columns='smoker',values='total_bill', aggfunc='std')
# # print(arr)x

# brr = df.pivot_table(index = ['sex','smoker'], columns = 'day', values = 'total_bill')
# print(brr)

print(df)
df['Date'] = pd.to_datetime(df['Date'])
df['month'] = df['Date'].dt.month_name()
df.head().plot(kind = 'bar')
plt.show()