data_list = [
    [101, 'John', 'IT', 75000],
    [102, 'Sarah', 'HR', 65000],
    [103, 'Mike', 'IT', 80000]
]
df2 = pd.DataFrame(data_list, columns=['Employee_ID', 'Name', 'Department', 'Salary'])
print("\nMethod 2 - List of Lists:\n", df2)