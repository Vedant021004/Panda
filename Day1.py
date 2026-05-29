# first code of panda

import pandas as pd
s = pd.Series([12,34,56,], index=["a", "b", "c"])
print(s)
print(s['a'])

# dataframe
import pandas as pd
data = {
    "name" : ["riddhi", "keshu", "vedant"],
    "age" : [12,32,12],
    "city" : ["boisar", "mwaahpur", "jaipur"],
    "love" : ["vedantkapil","vedantkapil","riddhivermaji"]
}
s1 = pd.DataFrame(data)
print(s1)
print(s1.index)
print(s1.columns)


# DataFrame
import pandas as pd
Data = [['vedant',21],['hello',32]]
da = pd.DataFrame(Data, columns = ["name","marks"])
print(da)

#Reading excel file
import pandas as pd

read = pd.read_excel("code.xlsx") 

print(read)