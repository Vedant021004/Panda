# 📊 Creating a DataFrame

A **DataFrame** is a 2-dimensional labeled data structure — like a table with rows and columns. It's the core data structure in libraries like **pandas** (Python) and **data.frame** (R).

---

## 🐍 Python (pandas)

### Installation

```bash
pip install pandas
```

### Import

```python
import pandas as pd
```

---

### 1. From a Dictionary

The most common way — keys become column names, values become column data.

```python
data = {
    "Name":   ["Alice", "Bob", "Charlie"],
    "Age":    [25, 30, 35],
    "City":   ["Mumbai", "Delhi", "Pune"]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**
```
      Name  Age     City
0    Alice   25   Mumbai
1      Bob   30    Delhi
2  Charlie   35     Pune
```

---

### 2. From a List of Dictionaries

Each dictionary represents one row.

```python
rows = [
    {"Name": "Alice", "Age": 25},
    {"Name": "Bob",   "Age": 30},
]

df = pd.DataFrame(rows)
```

---

### 3. From a List of Lists

Pass column names separately.

```python
data = [
    ["Alice", 25, "Mumbai"],
    ["Bob",   30, "Delhi"],
]

df = pd.DataFrame(data, columns=["Name", "Age", "City"])
```

---

### 4. From a CSV File

```python
df = pd.read_csv("data.csv")
```

### 5. From an Excel File

```python
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
```

### 6. Empty DataFrame (define schema first)

```python
df = pd.DataFrame(columns=["Name", "Age", "City"])
```

---

## 🔍 Inspecting a DataFrame

| Method / Property | Description |
|---|---|
| `df.head(5)` | First 5 rows |
| `df.tail(5)` | Last 5 rows |
| `df.shape` | (rows, columns) |
| `df.info()` | Column types & nulls |
| `df.describe()` | Summary statistics |
| `df.columns` | Column names |
| `df.dtypes` | Data types per column |

---

## ✏️ Common Operations

### Select a Column

```python
df["Name"]          # Returns a Series
df[["Name", "Age"]] # Returns a DataFrame
```

### Filter Rows

```python
df[df["Age"] > 28]
```

### Add a New Column

```python
df["Seniority"] = df["Age"].apply(lambda x: "Senior" if x >= 30 else "Junior")
```

### Drop a Column

```python
df = df.drop(columns=["City"])
```

### Rename Columns

```python
df = df.rename(columns={"Name": "Full Name"})
```

### Handle Missing Values

```python
df.isnull().sum()       # Count nulls per column
df.dropna()             # Drop rows with any null
df.fillna(0)            # Fill nulls with 0
```

### Sort

```python
df = df.sort_values("Age", ascending=False)
```

### Reset Index

```python
df = df.reset_index(drop=True)
```

---

## 💾 Saving a DataFrame

```python
df.to_csv("output.csv", index=False)       # CSV
df.to_excel("output.xlsx", index=False)    # Excel
df.to_json("output.json", orient="records") # JSON
```

---

## R Language

```r
# From vectors
df <- data.frame(
  Name = c("Alice", "Bob", "Charlie"),
  Age  = c(25, 30, 35),
  City = c("Mumbai", "Delhi", "Pune")
)

# From CSV
df <- read.csv("data.csv")

# View
head(df)
str(df)
summary(df)
```

---

## ⚡ Quick Reference (pandas)

```python
import pandas as pd

# Create
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

# Inspect
df.shape       # (2, 2)
df.head()

# Select
df["A"]
df[["A", "B"]]

# Filter
df[df["A"] > 1]

# Save
df.to_csv("out.csv", index=False)
```

---

## 📚 Further Reading

- [pandas Documentation](https://pandas.pydata.org/docs/)
- [pandas Getting Started](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)
- [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)