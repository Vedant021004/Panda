import pandas as pd

data = {"a":[1,2,3,4,5,6,7,8,9], "b":[2,3,4,5,6,7,8,9,2]}
a = pd.DataFrame(data)
print(a)

# Dataframe from the numpy
import numpy as np
import pandas as pd

arr = np.array([[43,12,45],[45,12,22]])
df = pd.DataFrame(arr)
print(df)

# learning new concept reading the data from the excel sheet
import pandas as pd
Da = pd.read_excel("beta.xlsx")
print(Da)
print(Da.columns)