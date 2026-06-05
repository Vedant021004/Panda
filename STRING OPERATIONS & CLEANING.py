import pandas as pd

df = pd.DataFrame({
    'Name': ['  Alice  ', 'BOB', 'charlie', '  David', 'eve  '],
    'Email': ['alice@GMAIL.com', 'bob@yahoo.COM', 'charlie@GMAIL.com', 'invalid-email', 'eve@outlook.com'],
    'Phone': ['123-456-7890', '(234) 567-8901', '345.678.9012', '456-567-8923', 'N/A'],
    'Product': ['Laptop-Dell', 'Mouse_Logitech', 'Keyboard HP', 'Monitor-Samsung', 'Webcam_Logitech']
})

print("Original DataFrame:\n", df)

# === BASIC STRING OPERATIONS ===
print("\n1. Convert to lowercase:")
df['Name_Lower'] = df['Name'].str.lower()
print(df[['Name', 'Name_Lower']])

print("\n2. Convert to uppercase:")
df['Name_Upper'] = df['Name'].str.upper()
print(df[['Name', 'Name_Upper']])

print("\n3. Title case (first letter capital):")
df['Name_Title'] = df['Name'].str.title()
print(df[['Name', 'Name_Title']])

print("\n4. Remove leading/trailing whitespace:")
df['Name_Clean'] = df['Name'].str.strip()
print(df[['Name', 'Name_Clean']])

print("\n5. Remove only leading whitespace:")
df['Name'].str.lstrip()

print("\n6. Remove only trailing whitespace:")
df['Name'].str.rstrip()

# === STRING SEARCHING ===
print("\n7. Check if contains substring:")
df['Has_Gmail'] = df['Email'].str.contains('gmail', case=False)
print(df[['Email', 'Has_Gmail']])

print("\n8. Starts with:")
df['Starts_Alice'] = df['Name'].str.strip().str.startswith('Alice')
print(df[['Name', 'Starts_Alice']])

print("\n9. Ends with:")
df['Ends_Com'] = df['Email'].str.endswith('.com')
print(df[['Email', 'Ends_Com']])

print("\n10. Find position of substring:")
df['Position_at'] = df['Email'].str.find('@')
print(df[['Email', 'Position_at']])

# === STRING REPLACEMENT ===
print("\n11. Replace substring:")
df['Email_Clean'] = df['Email'].str.replace('GMAIL', 'gmail', case=False)
print(df[['Email', 'Email_Clean']])

print("\n12. Replace multiple characters:")
df['Phone_Clean'] = df['Phone'].str.replace('[-().]', '', regex=True)
print(df[['Phone', 'Phone_Clean']])

print("\n13. Remove specific characters:")
df['Product_Clean'] = df['Product'].str.replace('[-_]', ' ', regex=True)
print(df[['Product', 'Product_Clean']])

# === STRING SPLITTING ===
print("\n14. Split by delimiter:")
df['Email_Parts'] = df['Email'].str.split('@')
print(df['Email_Parts'])

print("\n15. Split and get specific part:")
df['Domain'] = df['Email'].str.split('@').str[1]
print(df[['Email', 'Domain']])

print("\n16. Split Product into Brand and Model:")
df[['Product_Type', 'Brand']] = df['Product'].str.split('[-_ ]', n=1, expand=True)
print(df[['Product', 'Product_Type', 'Brand']])

# === STRING LENGTH ===
print("\n17. Get string length:")
df['Name_Length'] = df['Name'].str.len()
print(df[['Name', 'Name_Length']])

# === ADVANCED ===
print("\n18. Extract using regex:")
df['Phone_Digits'] = df['Phone'].str.extract(r'(\d{3})')  # First 3 digits
print(df[['Phone', 'Phone_Digits']])

print("\n19. Pad strings:")
df['Name'].str.pad(10, fillchar='*')

print("\n20. Slice strings:")
df['Email_Start'] = df['Email'].str[:5]  # First 5 characters
print(df[['Email', 'Email_Start']])

print("\n21. Count occurrences:")
df['Count_e'] = df['Name'].str.count('e')
print(df[['Name', 'Count_e']])

print("\n22. Concatenate strings:")
df['Full_Info'] = df['Name'].str.strip() + ' - ' + df['Email']
print(df['Full_Info'])