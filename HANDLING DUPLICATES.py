import pandas as pd

# DataFrame with duplicates
df = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 101, 104, 102, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Bob', 'Eve'],
    'Department': ['IT', 'HR', 'IT', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [70000, 65000, 75000, 70000, 80000, 65000, 72000]
})

print("DataFrame with Duplicates:\n", df)

# === DETECTING DUPLICATES ===
print("\n1. Check for duplicate rows (boolean):")
print(df.duplicated())

print("\n2. Show duplicate rows:")
print(df[df.duplicated()])

print("\n3. Count total duplicates:")
print(df.duplicated().sum())

print("\n4. Check duplicates based on specific column:")
print(df.duplicated(subset=['Employee_ID']))

print("\n5. Check duplicates across multiple columns:")
print(df.duplicated(subset=['Name', 'Department']))

print("\n6. Mark all duplicates (keep=False):")
print(df.duplicated(keep=False))  # Marks all occurrences as True

print("\n7. Keep last occurrence instead of first:")
print(df.duplicated(keep='last'))

# === REMOVING DUPLICATES ===
print("\n8. Remove duplicate rows (keep first):")
print(df.drop_duplicates())

print("\n9. Remove duplicates based on Employee_ID:")
print(df.drop_duplicates(subset=['Employee_ID']))

print("\n10. Remove duplicates, keep last occurrence:")
print(df.drop_duplicates(keep='last'))

print("\n11. Remove duplicates based on multiple columns:")
print(df.drop_duplicates(subset=['Name', 'Department']))

print("\n12. Remove all duplicate occurrences (keep none):")
print(df.drop_duplicates(keep=False))

print("\n13. Inplace removal:")
df_copy = df.copy()
df_copy.drop_duplicates(inplace=True)
print(df_copy)

# === ADVANCED ===
print("\n14. Find rows that appear more than once:")
duplicate_ids = df[df.duplicated(subset=['Employee_ID'], keep=False)]
print(duplicate_ids)

print("\n15. Count occurrences of each duplicate:")
print(df['Employee_ID'].value_counts())

print("\n16. Keep row with highest salary when duplicates exist:")
df_no_dup = df.sort_values('Salary', ascending=False).drop_duplicates(subset=['Employee_ID'])
print(df_no_dup)