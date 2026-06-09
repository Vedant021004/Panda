# Create a sample DataFrame with combined data in one column
import pandas as pd
df = pd.DataFrame({
    'Full_Name': ['Artair Mpho', 'Pompiliu Ukko', 'Gerry Sigismund']
})

# Split the 'Full_Name' column into 'First_Name' and 'Last_Name'
df[['First_Name', 'Last_Name']] = df['Full_Name'].str.split(' ', expand=True)

# Output the result
print(df)
