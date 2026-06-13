import pandas as pd

courses = pd.read_csv('courses.csv')
students = pd.read_csv('students.csv')
nov = pd.read_csv('reg-month1.csv')
dec = pd.read_csv('reg-month2.csv')
matches = pd.read_csv('matches.csv')
delivery = pd.read_csv('deliveries.csv')

# pd.concat
multi = pd.concat([nov,dec],keys = ['nov','dec'])
# print(pd.concat([dec ,nov])) # to avoid the index problem use ignore_index = true

# print(pd.concat([dec,nov],ignore_index = True))
print(pd.concat([nov,dec],keys = ['nov','dec']))

# if we want the first person who applied in november
print(multi.loc[('nov',0)])