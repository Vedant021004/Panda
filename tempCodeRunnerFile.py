import pandas as pd
arr = pd.Series([1,2,3,4,5])
arr1 = pd.Series([2,4,6,8,10])
result = [x for x in arr if x not in arr1.values] + [x for x in arr1 if x not in arr.values]
print(result)