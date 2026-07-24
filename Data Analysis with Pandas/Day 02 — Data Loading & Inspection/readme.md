# 📅 Day 2 — Data Loading & Inspection

---

## 🎯 Objective

- CSV ও Excel file থেকে data load করা শেখা
- Dataset preview করা (head, tail)
- Dataset structure ও summary বোঝা
- Data size ও column information জানা

---

## 📚 Topics Covered

- CSV Loading (`read_csv`)
- Excel Loading (`read_excel`)
- Data Preview (`head`, `tail`)
- Data Info (`info`, `describe`)
- Dataset Shape & Columns

---

## 📁 Project Structure

```id="7rf4zq"
day-2/
│── 01_load_csv.py
│── 02_load_excel.py
│── 03_head_tail.py
│── 04_info_describe.py
│── 05_shape_columns.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`
- **Description:** Sample employee dataset for practice
- **Columns:**
  - Name → ব্যক্তির নাম
  - Age → বয়স
  - City → শহর
  - Salary → বেতন

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_load_csv.py

### 🔹 Purpose

- CSV file থেকে data load করা

### 🧾 Code

```python id="p6y4g2"
import pandas as pd

df = pd.read_csv("data.csv")

print(df)
```

### 🧠 Explanation

- `pd.read_csv("data.csv")` → CSV file থেকে data load করে DataFrame বানায়
- `df` → loaded dataset store করে
- `print(df)` → পুরো dataset দেখায়

👉 CSV = most commonly used data format

---

## 📄 2. 02_load_excel.py

### 🔹 Purpose

- Excel file load করা

### 🧾 Code

```python id="cll93v"
import pandas as pd

df = pd.read_excel("data.xlsx")

print(df)
```

### 🧠 Explanation

- `pd.read_excel()` → Excel file read করে
- Excel file পড়তে `openpyxl` লাগতে পারে
- multiple sheet থাকলে `sheet_name` ব্যবহার করা যায়

---

## 📄 3. 03_head_tail.py

### 🔹 Purpose

- dataset এর শুরু ও শেষ অংশ দেখা

### 🧾 Code

```python id="zb23xy"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.head(3))

print(df.tail())
print(df.tail(2))
```

### 🧠 Explanation

- `head()` → প্রথম 5টা row (default)
- `head(n)` → first n rows
- `tail()` → শেষের 5টা row
- `tail(n)` → last n rows

👉 বড় dataset এ full print না করে preview করা best practice

---

## 📄 4. 04_info_describe.py

### 🔹 Purpose

- dataset এর structure ও statistics বোঝা

### 🧾 Code

```python id="g3o4dr"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.info())
print(df.describe())
```

### 🧠 Explanation

- `info()` →
  - column name
  - data type
  - null values count

- `describe()` →
  - mean, min, max
  - standard deviation

👉 data বুঝার জন্য প্রথম step = info() + describe()

---

## 📄 5. 05_shape_columns.py

### 🔹 Purpose

- dataset size ও column name জানা

### 🧾 Code

```python id="r1a8wt"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.shape)

print(df.shape[0])
print(df.shape[1])

print(df.columns)

print(list(df.columns))
```

### 🧠 Explanation

- `df.shape` → (rows, columns)
- `df.shape[0]` → rows সংখ্যা
- `df.shape[1]` → columns সংখ্যা
- `df.columns` → column names

👉 dataset overview পাওয়ার জন্য খুব গুরুত্বপূর্ণ

---

# ⚙️ Implementation Flow

1. CSV ও Excel file load করা হয়েছে
2. head() ও tail() দিয়ে dataset preview করা হয়েছে
3. info() দিয়ে structure analyze করা হয়েছে
4. describe() দিয়ে statistical summary দেখা হয়েছে
5. shape ও columns দিয়ে dataset size বোঝা হয়েছে

---

## 📈 Output / Result

- Dataset successfully load করা হয়েছে
- Data preview করা হয়েছে
- Structure ও statistics বোঝা গেছে
- Dataset এর size ও column info clear হয়েছে

---

## 🚀 What I Learned

- Data load করা = first step of analysis
- head/tail দিয়ে দ্রুত data inspect করা যায়
- info() না দেখলে data বোঝা যায় না
- shape & columns = quick overview tool

---

## 🧠 Key Concepts (Quick Revision)

- `read_csv()` → CSV load
- `read_excel()` → Excel load
- `head()` → top rows
- `tail()` → bottom rows
- `info()` → structure
- `describe()` → statistics
- `shape` → size

---

## 📝 Notes

- বড় dataset হলে কখনো full print করো না
- সবসময় analysis শুরুর আগে `info()` দেখো
- Excel file পড়তে extra library লাগতে পারে
- dataset path ঠিক রাখা খুব important

---

## 📌 Next Day Preview

👉 Day 3 — Selection Basics

- single column select
- multiple column select
- row selection

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- real dataset (Kaggle) ব্যবহার করা
- notebook (Jupyter) ব্যবহার শুরু করা

## 🧪 Practice Ideas

- নিজে নতুন CSV file তৈরি করে load করো
- head(), tail(), info() practice করো
- different dataset দিয়ে test করো
