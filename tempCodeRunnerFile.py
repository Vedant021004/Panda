import pandas as pd
import seaborn as sns

brr = pd.read_csv("expense_data.csv")
arr = pd.read_csv("titanic.csv")


df = sns.load_dataset('tips')
df.head()
data = pd.pivot(index = 'sex', columns= 'smoker', values = 'total_bill')
print(data)