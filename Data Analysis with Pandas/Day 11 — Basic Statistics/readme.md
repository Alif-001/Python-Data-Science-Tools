# 📅 Day 11 — Basic Statistics

---

## 🎯 Objective

- Pandas দিয়ে basic statistical analysis করা শেখা
- dataset থেকে insights বের করা শেখা
- mean, median, mode বুঝা ও ব্যবহার করা
- real-world numeric analysis practice করা

---

## 📚 Topics Covered

- mean(), median(), mode()
- min(), max(), sum()
- std() (standard deviation)
- describe() full summary
- multi-column statistics

---

## 📁 Project Structure

```id="d11proj"
day-11/
│── 01_mean_median_mode.py
│── 02_min_max_sum.py
│── 03_std_variation.py
│── 04_multiple_columns_stats.py
│── 05_describe_summary.py
│── 06_real_world_analysis.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset with numeric fields for statistical analysis

- **Columns:**
  - Name → employee name
  - Age → age of employee
  - Salary → monthly salary
  - Marks → performance score

👉 clean numeric dataset used for statistics practice

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_mean_median_mode.py

### 🔹 Purpose

- central tendency measure করা

### 🧾 Code

```python id="d11c1"
import pandas as pd

df = pd.read_csv("data.csv")

print("Mean Age:", df['Age'].mean())
print("Median Salary:", df['Salary'].median())
print("Mode Marks:", df['Marks'].mode())
```

### 🧠 Explanation

- `mean()` → average value
- `median()` → middle value
- `mode()` → most frequent value

👉 data distribution understanding starts here

---

## 📄 2. 02_min_max_sum.py

### 🔹 Purpose

- basic numeric aggregation

### 🧾 Code

```python id="d11c2"
import pandas as pd

df = pd.read_csv("data.csv")

print(df['Age'].min())
print(df['Salary'].max())
print(df['Salary'].sum())
```

### 🧠 Explanation

- `min()` → smallest value
- `max()` → largest value
- `sum()` → total value

👉 basic descriptive stats

---

## 📄 3. 03_std_variation.py

### 🔹 Purpose

- data spread analysis

### 🧾 Code

```python id="d11c3"
import pandas as pd

df = pd.read_csv("data.csv")

print(df['Salary'].std())
```

### 🧠 Explanation

- `std()` → data কতটা spread তা দেখায়
- high std → inconsistent data
- low std → consistent data

👉 variability measurement

---

## 📄 4. 04_multiple_columns_stats.py

### 🔹 Purpose

- multi-column analysis

### 🧾 Code

```python id="d11c4"
import pandas as pd

df = pd.read_csv("data.csv")

print(df[['Age', 'Salary', 'Marks']].mean())
print(df[['Age', 'Salary', 'Marks']].sum())
```

### 🧠 Explanation

- multiple columns একসাথে analyze করা যায়
- group analysis সহজ হয়

👉 batch statistics processing

---

## 📄 5. 05_describe_summary.py

### 🔹 Purpose

- full statistical summary

### 🧾 Code

```python id="d11c5"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.describe())
print(df.describe(include='all'))
```

### 🧠 Explanation

- `describe()` → full stats report
- count, mean, std, min, max সব একসাথে

👉 fastest data overview tool

---

## 📄 6. 06_real_world_analysis.py

### 🔹 Purpose

- real-world insights extraction

### 🧾 Code

```python id="d11c6"
import pandas as pd

df = pd.read_csv("data.csv")

avg_salary = df['Salary'].mean()
max_marks = df['Marks'].max()
min_age = df['Age'].min()
total_salary = df['Salary'].sum()

print(avg_salary, max_marks, min_age, total_salary)
```

### 🧠 Explanation

- business insights generate করা
- KPI extraction (salary, marks, age)
- decision making support

👉 analytics mindset starts here

---

# ⚙️ Implementation Flow

1. dataset load করা হয়েছে
2. basic statistics applied করা হয়েছে
3. aggregation functions ব্যবহার করা হয়েছে
4. multi-column analysis করা হয়েছে
5. full summary report তৈরি করা হয়েছে
6. insights extract করা হয়েছে

---

## 📈 Output / Result

- employee performance analysis হয়েছে
- salary distribution বোঝা গেছে
- dataset summary তৈরি হয়েছে
- business insights পাওয়া গেছে

---

## 🚀 What I Learned

- statistics = data analysis foundation
- mean/median/mode = central tendency
- std = variability measurement
- describe = quick dataset overview

---

## 🧠 Key Concepts (Quick Revision)

- `mean()` → average
- `median()` → middle value
- `mode()` → most frequent
- `min/max` → range
- `std()` → spread
- `describe()` → full summary

---

## 📝 Notes

- outliers mean heavily affect করে
- median is more robust than mean
- statistics = decision making tool

---

## 📌 Next Day Preview

👉 Day 12 — Sorting & Ranking

- sort_values()
- sort_index()
- rank()
- performance ranking system

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- employee ranking system বানানো
- salary vs performance correlation analysis

## 🧪 Practice Ideas

- নিজের dataset এ `.describe()` try করো
- mean vs median compare করো
