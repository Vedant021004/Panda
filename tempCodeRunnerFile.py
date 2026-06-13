import pandas as pd

courses = pd.read_csv('courses.csv')
students = pd.read_csv('students.csv')
nov = pd.read_csv('reg-month1.csv')
dec = pd.read_csv('reg-month2.csv')
matches = pd.read_csv('matches.csv')
delivery = pd.read_csv('deliveries.csv')

# print(courses)
# print(students)
regs = pd.concat([dec,nov],ignore_index = True)
print(regs)


total = regs.merge(courses, how = 'inner', on = 'course_id')
print(total['price'].sum())

# find the month by month revenue
multi = pd.concat([nov,dec],keys = ['nov','dec']).reset_index()
print(multi)

total_by_month = multi.merge(courses, how = 'inner', on = 'course_id')[['level_0', 'price']]
print(total_by_month.groupby('level_0')['price'].sum())