# 📅 Day 9 — Data Type Handling

---

## 🎯 Objective

- Pandas এ data type identify করা শেখা
- string → numeric conversion করা
- date/time format handle করা
- real-world messy dataset clean করা
- proper data type optimization করা

---

## 📚 Topics Covered

- df.dtypes check করা
- astype() ব্যবহার
- to_numeric() safe conversion
- to_datetime() date conversion
- mixed data cleaning strategy

---

## 📁 Project Structure

```id="d9proj"
day-9/
│── 01_check_dtypes.py
│── 02_astype_conversion.py
│── 03_numeric_conversion.py
│── 04_datetime_conversion.py
│── 05_mixed_cleaning.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset with mixed data types (string-formatted numeric & dates)

- **Columns:**
  - Name → employee name
  - Age → age (string format)
  - Salary → salary (string format)
  - JoinDate → joining date (string format)

👉 সব numeric data শুরুতে string হিসেবে আছে (real-world issue)

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_check_dtypes.py

### 🔹 Purpose

- dataset এর data type check করা

### 🧾 Code

```python id="d9c1"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.dtypes)
```

### 🧠 Explanation

- `object` = string type
- `int/float` = numeric type
- type mismatch detect করা cleaning এর first step

👉 data understanding = first step of ML pipeline

---

## 📄 2. 02_astype_conversion.py

### 🔹 Purpose

- manual type conversion

### 🧾 Code

```python id="d9c2"
import pandas as pd

df = pd.read_csv("data.csv")

df['Age'] = df['Age'].astype(int)
df['Salary'] = df['Salary'].astype(int)

print(df.dtypes)
```

### 🧠 Explanation

- `astype()` → direct conversion
- string → integer conversion
- fast but strict method

👉 manual but powerful conversion tool

---

## 📄 3. 03_numeric_conversion.py

### 🔹 Purpose

- safe numeric conversion

### 🧾 Code

```python id="d9c3"
import pandas as pd

df = pd.read_csv("data.csv")

df['Age'] = pd.to_numeric(df['Age'])
df['Salary'] = pd.to_numeric(df['Salary'])

print(df.dtypes)
```

### 🧠 Explanation

- `to_numeric()` → safer conversion
- errors handle করা যায় (`coerce`)
- messy data cleaning এর জন্য best

👉 production-level safe method

---

## 📄 4. 04_datetime_conversion.py

### 🔹 Purpose

- date conversion & time analysis

### 🧾 Code

```python id="d9c4"
import pandas as pd

df = pd.read_csv("data.csv")

df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print(df.dtypes)

print(df['JoinDate'].dt.year)
print(df['JoinDate'].dt.month)
print(df['JoinDate'].dt.day)
```

### 🧠 Explanation

- string → datetime conversion
- `.dt` accessor দিয়ে date breakdown করা যায়
- time-based analysis possible

👉 time series analysis foundation

---

## 📄 5. 05_mixed_cleaning.py

### 🔹 Purpose

- full real-world cleaning pipeline

### 🧾 Code

```python id="d9c5"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.dtypes)

df['Age'] = pd.to_numeric(df['Age'])
df['Salary'] = pd.to_numeric(df['Salary'])
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print(df.dtypes)
print(df.head())
```

### 🧠 Explanation

- step 1 → inspect types
- step 2 → numeric conversion
- step 3 → datetime conversion
- step 4 → verify cleaned dataset

👉 full pipeline = industry standard workflow

---

# ⚙️ Implementation Flow

1. dataset load করা হয়েছে
2. data types check করা হয়েছে
3. numeric conversion করা হয়েছে
4. datetime conversion করা হয়েছে
5. final cleaned dataset verified করা হয়েছে

---

## 📈 Output / Result

- messy string data → clean numeric data
- date column → proper datetime format
- analysis-ready dataset তৈরি হয়েছে

---

## 🚀 What I Learned

- data type mismatch is very common
- string numeric data must be converted
- datetime is crucial for time analysis
- cleaning pipeline must include type fixing

---

## 🧠 Key Concepts (Quick Revision)

- `astype()` → direct conversion
- `to_numeric()` → safe numeric conversion
- `to_datetime()` → date conversion
- `object` → string type in pandas
- `.dt` → datetime operations

---

## 📝 Notes

- wrong conversion করলে data loss হতে পারে
- always check df.dtypes before analysis
- real datasets almost always need type cleaning

---

## 📌 Next Day Preview

👉 Day 10 — String Operations

- lower(), upper()
- contains()
- split()
- replace()
- text cleaning tricks

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- large dataset type optimization
- memory usage reduce করা

## 🧪 Practice Ideas

- নিজের dataset এ string → numeric conversion try করো
- date column থেকে year-wise analysis করো
