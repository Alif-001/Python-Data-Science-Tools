# 📅 Day 1 — Pandas Introduction & Setup

---

## 🎯 Objective

- Pandas কী এবং কেন ব্যবহার করা হয় বুঝা
- Pandas install ও import করা
- Series এবং DataFrame এর basic ধারণা নেওয়া
- DataFrame structure (rows, columns, index) বোঝা

---

## 📚 Topics Covered

- Pandas Introduction
- Installation & Import
- Series Basics
- DataFrame Basics
- DataFrame Structure

---

## 📁 Project Structure

```
day-1/
│── 01_install_and_import.py
│── 02_series_basics.py
│── 03_dataframe_basics.py
│── 04_dataframe_structure.py
│── README.md
```

---

## 📊 Dataset

- ❌ No dataset used (basic concept learning day)

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_install_and_import.py

### 🔹 Purpose

- Pandas install করা এবং project এ import করা
- Pandas version check করা

### 🧾 Code

```python
# ================================
# Pandas Installation & Import
# ================================

# pip install pandas

import pandas as pd

print(pd.__version__)
```

### 🧠 Explanation

- `pip install pandas` → Pandas install করার command
- `import pandas as pd` → Pandas library import (pd alias ব্যবহার করা হয়)
- `pd.__version__` → installed version check করার জন্য

---

## 📄 2. 02_series_basics.py

### 🔹 Purpose

- Pandas Series (1D data structure) বোঝা
- Series create ও access করা

### 🧾 Code

```python
import pandas as pd

data = [10, 20, 30, 40]

s = pd.Series(data)
print(s)

s2 = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s2)

print(s2['a'])
```

### 🧠 Explanation

- `pd.Series(data)` → list থেকে Series তৈরি
- default index → 0,1,2,3
- custom index → 'a','b','c','d'
- `s2['a']` → specific value access

👉 Series = single column data (1D)

---

## 📄 3. 03_dataframe_basics.py

### 🔹 Purpose

- DataFrame (2D table structure) তৈরি ও ব্যবহার শেখা

### 🧾 Code

```python
import pandas as pd

data = {
    'Name': ['Rahim', 'Karim', 'Sakib'],
    'Age': [20, 22, 25],
    'City': ['Dhaka', 'Sylhet', 'Chittagong']
}

df = pd.DataFrame(data)

print(df)

print(df['Name'])

print(df[['Name', 'Age']])
```

### 🧠 Explanation

- dictionary → DataFrame এ convert করা হয়েছে
- rows = data entries
- columns = Name, Age, City
- `df['Name']` → single column
- `df[['Name','Age']]` → multiple columns

👉 DataFrame = table (2D structure)

---

## 📄 4. 04_dataframe_structure.py

### 🔹 Purpose

- DataFrame এর internal structure বোঝা

### 🧾 Code

```python
import pandas as pd

data = {
    'Name': ['A', 'B', 'C'],
    'Marks': [80, 90, 85]
}

df = pd.DataFrame(data)

print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
```

### 🧠 Explanation

- `df.shape` → (rows, columns)
- `df.columns` → column names
- `df.index` → row labels
- `df.dtypes` → data type (int, object etc.)

👉 Structure বোঝা future analysis এর জন্য খুব important

---

# ⚙️ Implementation Flow

1. Pandas install ও import করা হয়েছে
2. Series তৈরি করে basic understanding নেওয়া হয়েছে
3. DataFrame তৈরি করে table structure শেখা হয়েছে
4. DataFrame এর structure (shape, columns, index) analyze করা হয়েছে

---

## 📈 Output / Result

- Successfully Pandas setup করা হয়েছে
- Series ও DataFrame তৈরি করা হয়েছে
- DataFrame structure clearly বোঝা গেছে

---

## 🚀 What I Learned

- Pandas = powerful data analysis tool
- Series = 1D data
- DataFrame = 2D table
- Basic structure না বুঝলে আগানো কঠিন

---

## 🧠 Key Concepts (Quick Revision)

- Series → single column
- DataFrame → rows + columns
- index → row label
- columns → feature নাম

---

## 📝 Notes

- সবসময় `import pandas as pd` use করা best practice
- beginner stage এ structure ভালোভাবে বুঝা জরুরি
- DataFrame concept clear না হলে GroupBy/Merge কঠিন হবে

---

## 📌 Next Day Preview

👉 Day 2 — Data Loading & Inspection

- CSV file load করা
- head(), tail()
- info(), describe()
- shape, columns

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- real dataset ব্যবহার করা (CSV)
- print এর বদলে notebook use করা

## 🧪 Practice Ideas

- নিজের নাম/age দিয়ে DataFrame বানাও
- custom index দিয়ে Series তৈরি করো
