# 📅 Day 3 — Selection Basics

---

## 🎯 Objective

- DataFrame থেকে single ও multiple column select করা শেখা
- Row selection (basic indexing) বোঝা
- iloc ব্যবহার করে row/column access করা
- pandas indexing concept strong করা

---

## 📚 Topics Covered

- Single Column Selection
- Multiple Column Selection
- Row Selection (iloc)
- Row + Column Selection

---

## 📁 Project Structure

```id="xq9d2a"
day-3/
│── 01_single_column.py
│── 02_multiple_columns.py
│── 03_row_selection_basic.py
│── 04_column_and_row_together.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Simple employee dataset for selection practice

- **Columns:**
  - Name → Employee name
  - Age → Employee age
  - City → Location
  - Salary → Monthly salary

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_single_column.py

### 🔹 Purpose

- একটি single column select করা

### 🧾 Code

```python id="s1v8mk"
import pandas as pd

df = pd.read_csv("data.csv")

name_column = df['Name']
print(name_column)

print(type(name_column))

print(df['Age'])
```

### 🧠 Explanation

- `df['Name']` → একটি column select করে
- এটা **Series (1D data)** return করে
- single column = always Series

👉 Single column access = fastest way to extract feature

---

## 📄 2. 02_multiple_columns.py

### 🔹 Purpose

- multiple columns একসাথে select করা

### 🧾 Code

```python id="q9k3lm"
import pandas as pd

df = pd.read_csv("data.csv")

subset = df[['Name', 'Salary']]
print(subset)

print(type(subset))

print(df[['Name', 'Age', 'City']])
```

### 🧠 Explanation

- `df[['A','B']]` → multiple column select
- এটা **DataFrame (2D)** return করে
- double bracket mandatory

👉 multiple column = subset of dataset

---

## 📄 3. 03_row_selection_basic.py

### 🔹 Purpose

- row select করা using index position

### 🧾 Code

```python id="z8p1tw"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.iloc[0])
print(df.iloc[1])

print(df.iloc[0:3])

print(df.iloc[[0, 2, 4]])
```

### 🧠 Explanation

- `iloc[]` → position-based indexing
- `0` → first row
- `0:3` → range (0,1,2)
- list `[0,2,4]` → specific rows

👉 iloc = index-based row access

---

## 📄 4. 04_column_and_row_together.py

### 🔹 Purpose

- row + column একসাথে select করা

### 🧾 Code

```python id="k2m7qv"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.iloc[0, 0])

print(df.iloc[0:3, 0:2])
```

### 🧠 Explanation

- `iloc[row, column]` → 2D selection
- `[0,0]` → first row first column
- `[0:3, 0:2]` → subset of dataset

👉 powerful slicing technique

---

# ⚙️ Implementation Flow

1. Dataset load করা হয়েছে
2. Single column extract করা হয়েছে
3. Multiple columns extract করা হয়েছে
4. Row selection (iloc) ব্যবহার করা হয়েছে
5. Row + column slicing করা হয়েছে

---

## 📈 Output / Result

- Columns successfully extracted
- Rows successfully selected
- Dataset slicing concept clear হয়েছে
- pandas indexing basics mastered

---

## 🚀 What I Learned

- Single column → Series return করে
- Multiple column → DataFrame return করে
- iloc = position-based selection
- Data slicing is very powerful for analysis

---

## 🧠 Key Concepts (Quick Revision)

- `df['col']` → Series
- `df[['col1','col2']]` → DataFrame
- `iloc[row]` → row selection
- `iloc[row, col]` → 2D selection

---

## 📝 Notes

- single bracket → Series
- double bracket → DataFrame
- iloc always uses index position (not name)
- slicing excludes last index

---

## 📌 Next Day Preview

👉 Day 4 — Advanced Indexing

- loc vs iloc
- label based selection
- slicing deep dive

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- real dataset try করা
- row filtering add করা

## 🧪 Practice Ideas

- নিজের dataset এ columns select করে practice করো
- iloc দিয়ে different slicing try করো
