import pandas as pd

atr = pd.read_csv('imdb-top-1000.csv')
print(atr)
# # print(atr.iloc[3])  #print by reference
# print(atr['Genre']) #print only Genre column
# print(atr.iloc[0 , :])  # Print only 1st row
# print(atr.iloc[:]) # It will print all the r and c
# print(atr.iloc[: , 0])  #printing the 1st column
# print(atr.iloc[1  , 1])
# print(atr.iloc[-1 , 0])
# print(atr.iloc[ 0 , -1])
# print(atr.iloc[: , -1])

geners = atr.groupby('Genre')

print(geners)

# print(geners.sum())


# print(atr.groupby('Genre').sum()['Gross'].sort_values(ascending = False).head(3))

print(atr.groupby('Director').sum()['No_of_Votes'].sort_values(ascending = False).head(1))

print(atr.groupby('Series_Title').sum()['IMDB_Rating'].sort_values(ascending = False))

print(atr.groupby('Star1')['Series_Title'].count())