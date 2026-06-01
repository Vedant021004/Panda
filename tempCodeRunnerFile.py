import numpy as np
import pandas as pd
# arr1 = np.random(size=(4,3))
rng = np.random.default_rng()
arr = rng.integers(low=1, high=100, size=(3, 5))
print(arr)
df = pd.DataFrame(arr)
print(df)