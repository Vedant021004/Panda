# Pandas: Complete Data Analysis and Manipulation Guide

## What is Pandas?

**Pandas** is an open-source Python library used for:

* Data Cleaning
* Data Manipulation
* Data Analysis
* Data Transformation
* Data Aggregation
* Data Visualization Preparation
* Machine Learning Data Preprocessing

Think of Pandas as Excel on steroids.

### Without Pandas

```python
data = [
    ["Vedant",20,85],
    ["Rahul",21,90]
]
```

Finding averages, filtering, sorting becomes difficult.

### With Pandas

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df["marks"].mean())
```

One line of code.

---

# Why Pandas Exists

Most real-world data comes from:

* CSV files
* Excel sheets
* Databases
* APIs
* JSON files
* Logs

Before analysis, data is usually:

* Missing values
* Duplicate rows
* Wrong formats
* Inconsistent text
* Spread across multiple files

Pandas helps solve these problems efficiently.

---

# Core Data Structures

## Series

A Series is a one-dimensional labeled array.

```python
import pandas as pd

s = pd.Series([10,20,30,40])
print(s)
```

Output:

```text
0    10
1    20
2    30
3    40
```

### Characteristics

* Single column
* Has index
* Similar to NumPy array but with labels

### Use Cases

* Storing one variable
* Feature vectors
* Statistical operations

---

## DataFrame

Most important Pandas object.

```python
df = pd.DataFrame({
    "Name":["Vedant","Rahul"],
    "Marks":[85,90]
})
```

Output:

| Name   | Marks |
| ------ | ----- |
| Vedant | 85    |
| Rahul  | 90    |

### Characteristics

* Rows and columns
* Similar to SQL table
* Similar to Excel sheet

---

# Reading Data

## CSV

```python
df = pd.read_csv("students.csv")
```

Most common operation in Data Science.

### Important Parameters

```python
pd.read_csv(
    "students.csv",
    nrows=100,
    usecols=["name","marks"]
)
```

---

## Excel

```python
df = pd.read_excel("students.xlsx")
```

---

## JSON

```python
df = pd.read_json("data.json")
```

Common when working with APIs.

---

# Understanding Data

Before analysis:

```python
df.head()
```

Shows first five rows.

---

```python
df.tail()
```

Shows last five rows.

---

```python
df.shape
```

Returns:

```python
(rows, columns)
```

---

```python
df.columns
```

Shows column names.

---

```python
df.info()
```

Most important diagnostic function.

Shows:

* Column names
* Datatypes
* Missing values
* Memory usage

---

```python
df.describe()
```

Provides statistics:

* Mean
* Median
* Standard deviation
* Min
* Max

---

# Data Selection

## Single Column

```python
df["marks"]
```

Returns Series.

---

## Multiple Columns

```python
df[["name","marks"]]
```

Returns DataFrame.

---

# Row Selection

## loc

Label-based indexing.

```python
df.loc[5]
```

Uses actual index labels.

---

## iloc

Position-based indexing.

```python
df.iloc[5]
```

Uses row position.

---

# Filtering Data

Example:

Students scoring above 80.

```python
df[df["marks"] > 80]
```

---

Multiple conditions:

```python
df[
    (df["marks"] > 80)
    &
    (df["age"] > 20)
]
```

---

# Sorting

## Ascending

```python
df.sort_values("marks")
```

---

## Descending

```python
df.sort_values(
    "marks",
    ascending=False
)
```

Common interview question.

---

# Handling Missing Values

Real-world data always contains missing values.

Example:

| Name   | Marks |
| ------ | ----- |
| Vedant | 85    |
| Rahul  | NaN   |

---

Check missing values:

```python
df.isnull().sum()
```

---

Remove missing rows:

```python
df.dropna()
```

---

Replace missing values:

```python
df.fillna(0)
```

or

```python
df.fillna(df["marks"].mean())
```

---

# Duplicate Records

Find duplicates:

```python
df.duplicated()
```

Remove duplicates:

```python
df.drop_duplicates()
```

---

# GroupBy

One of the most important Pandas features.

### Example

Course Revenue

```python
df.groupby("course")["price"].sum()
```

Meaning:

1. Group rows by course
2. Sum price for each course

---

Multiple Aggregations

```python
df.groupby("course")["price"].agg([
    "sum",
    "mean",
    "max"
])
```

Output:

| Course | Sum | Mean | Max |
| ------ | --- | ---- | --- |

---

# Aggregation Functions

## Sum

```python
df["price"].sum()
```

---

## Mean

```python
df["price"].mean()
```

---

## Max

```python
df["price"].max()
```

---

## Min

```python
df["price"].min()
```

---

## Count

```python
df["price"].count()
```

---

# Merge

Most important topic for interviews.

Real-world data is split across tables.

### Students

| student_id | name |

### Marks

| student_id | marks |

Merge:

```python
students.merge(
    marks,
    on="student_id"
)
```

---

## Join Types

### Inner Join

Only matches.

```python
how="inner"
```

---

### Left Join

All left rows.

```python
how="left"
```

---

### Right Join

All right rows.

```python
how="right"
```

---

### Outer Join

Everything.

```python
how="outer"
```

---

### Cross Join

Cartesian product.

```python
how="cross"
```

---

### Self Join

Table joined with itself.

Used in:

* Employee hierarchy
* Manager relationships

---

# Concat

Combine DataFrames vertically or horizontally.

```python
pd.concat([df1,df2])
```

---

Rows:

```python
axis=0
```

---

Columns:

```python
axis=1
```

---

# Pivot Tables

Excel-style summaries.

```python
pd.pivot_table(
    df,
    values="sales",
    index="city",
    aggfunc="sum"
)
```

---

# Apply Functions

Custom logic.

```python
df["marks"].apply(
    lambda x: x + 5
)
```

---

# String Operations

```python
df["name"].str.upper()
```

```python
df["name"].str.lower()
```

```python
df["email"].str.contains("@")
```

---

# DateTime Operations

Convert string to date:

```python
pd.to_datetime(
    df["date"]
)
```

Extract year:

```python
df["date"].dt.year
```

Extract month:

```python
df["date"].dt.month
```

---

# Visualization

Line Plot:

```python
df.plot()
```

Bar Chart:

```python
df.plot(kind="bar")
```

Histogram:

```python
df.plot(kind="hist")
```

Scatter Plot:

```python
df.plot(kind="scatter")
```

---

# Pandas in Machine Learning

Before Scikit-Learn:

1. Read Data
2. Clean Data
3. Handle Missing Values
4. Encode Features
5. Merge Datasets
6. Prepare Features

Only then:

```python
from sklearn.linear_model import LinearRegression
```

---

# Real Project Applications

### E-Commerce

* Customer Analysis
* Revenue Analysis
* Product Analysis

### IPL

* Orange Cap
* Purple Cap
* Strike Rate
* Venue Performance

### Education

* Student Performance
* Course Revenue
* Attendance Tracking

### Finance

* Stock Analysis
* Profit Reports
* Risk Analysis

---

# Most Asked Interview Questions

1. Difference between Series and DataFrame?
2. Difference between loc and iloc?
3. Difference between merge and join?
4. Difference between concat and merge?
5. What is GroupBy?
6. What is Pivot Table?
7. How do you handle missing values?
8. Difference between apply and map?
9. What is vectorization?
10. Why is Pandas faster than Python loops?

---

# Pandas Mastery Checklist

Before moving to Scikit-Learn, ensure you can confidently use:

✅ read_csv()
✅ head()
✅ info()
✅ describe()
✅ loc / iloc
✅ filtering
✅ sorting
✅ fillna()
✅ dropna()
✅ drop_duplicates()
✅ groupby()
✅ agg()
✅ merge()
✅ join()
✅ concat()
✅ pivot_table()
✅ apply()
✅ string methods
✅ datetime methods
✅ plotting

If you can do all of these without looking at notes, you're ready to start building ML datasets with Scikit-Learn and move toward your ML → RAG → LLM roadmap.
