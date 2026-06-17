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

print(geners.agg(['min','max']))


# for genre, group in geners:
#     print(type(group))

# for genre, group in geners:
#     print(group[group["Series_Title"].str.startswith("A")])

# print(type(geners.obj))

print(atr.groupby(['Star1','Genre'])['Metascore'].mean().reset_index())



import pandas as pd
ipl = pd.read_csv("deliveries.csv")
print(ipl)

# find the top 10 batsman in term of runs
IPL1 = ipl.groupby('batsman')['batsman_runs'].count().sort_values(ascending = False)
print(IPL1)

# find the batsman with max numbers of six
six = ipl[ipl['batsman_runs'] == 6].count()
print(six)

# find the batsman with most 4 and 6 in last 5 over
import pandas as pd
ipl = pd.read_csv("deliveries.csv")
most = ipl[((ipl['batsman_runs'] == 4 ) | (ipl['batsman_runs'] == 6)) & (ipl['over'] >= 16)]
print(most.groupby('batsman')['batsman'].count().sort_values(ascending = False))

# find virat kolhi's runs against all the teams
# we will going to use the filter 
import pandas as pd
ipl = pd.read_csv("deliveries.csv")
virat = ipl[ipl['batsman'] == "V Kohli"]
print(virat.groupby('bowling_team')['batsman_runs'].sum())


