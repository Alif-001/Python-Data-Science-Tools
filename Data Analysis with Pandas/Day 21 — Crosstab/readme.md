# 📅 Day 21 — Crosstab

---

## 🎯 Objective

- Crosstab (cross tabulation) কীভাবে কাজ করে তা শেখা
- categorical data থেকে frequency table তৈরি করা
- group-wise comparison করা
- real-world reporting style analysis শেখা

---

## 📚 Topics Covered

- `pd.crosstab()` basics
- frequency table creation
- values with aggregation (`sum`, `mean`)
- normalization (row-wise, column-wise)
- business reporting style analysis

---

## 📁 Project Structure

```
day-21/
│── 01_crosstab_basic.py
│── 02_crosstab_with_values.py
│── 03_crosstab_mean.py
│── 04_crosstab_normalized.py
│── 05_crosstab_all.py
│── 06_real_world_crosstab.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset with department, city, and salary information

- **Columns:**
  - Name → employee name
  - Department → department (IT, HR, Finance)
  - City → work location
  - Salary → monthly salary

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_crosstab_basic.py

### 🔹 Purpose

- basic frequency table তৈরি করা

### 🧾 Code

```python
import pandas as pd

df = pd.read_csv("data.csv")

ct = pd.crosstab(df['Department'], df['City'])

print(ct)
```

### 🧠 Explanation

- department vs city count বের করে
- কতজন কোন category তে আছে তা দেখায়

---

## 📄 2. 02_crosstab_with_values.py

### 🔹 Purpose

- numeric value (salary) দিয়ে analysis

### 🧾 Code

```python
ct = pd.crosstab(
    df['Department'],
    df['City'],
    values=df['Salary'],
    aggfunc='sum'
)
```

### 🧠 Explanation

- শুধু count না, salary যোগ করে দেখায়
- group-wise total income analysis

---

## 📄 3. 03_crosstab_mean.py

### 🔹 Purpose

- average salary analysis

### 🧾 Code

```python
ct = pd.crosstab(
    df['Department'],
    df['City'],
    values=df['Salary'],
    aggfunc='mean'
)
```

### 🧠 Explanation

- প্রতিটি group এর average salary বের করে
- performance comparison সহজ হয়

---

## 📄 4. 04_crosstab_normalized.py

### 🔹 Purpose

- percentage distribution analysis

### 🧾 Code

```python
ct = pd.crosstab(
    df['Department'],
    df['City'],
    normalize='index'
)
```

### 🧠 Explanation

- row-wise percentage দেখায়
- data distribution বুঝতে সাহায্য করে

---

## 📄 5. 05_crosstab_all.py

### 🔹 Purpose

- full analysis (frequency + percentage)

### 🧾 Code

```python
print(pd.crosstab(df['Department'], df['City']))
print(pd.crosstab(df['Department'], df['City'], normalize='index'))
print(pd.crosstab(df['Department'], df['City'], normalize='columns'))
```

### 🧠 Explanation

- full comparison view
- row + column percentage analysis

---

## 📄 6. 06_real_world_crosstab.py

### 🔹 Purpose

- real-world insight extraction

### 🧾 Code

```python
freq = pd.crosstab(df['Department'], df['City'])
percent = pd.crosstab(df['Department'], df['City'], normalize='index')

print(freq)
print(percent)

print(freq.stack().idxmax())
```

### 🧠 Explanation

- most active department-city combination বের করে
- business reporting style insight তৈরি করে

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- categorical relationship তৈরি করা হয়েছে
- frequency table বানানো হয়েছে
- aggregation (sum/mean) করা হয়েছে
- percentage distribution বের করা হয়েছে
- final insight generate করা হয়েছে

---

## 📈 Output / Result

- department vs city distribution পাওয়া গেছে
- salary-based group analysis হয়েছে
- percentage-wise data breakdown হয়েছে
- most active group identify করা গেছে

---

## 🚀 What I Learned

- crosstab = powerful reporting tool
- categorical data analysis সহজ হয়
- aggregation + grouping একসাথে করা যায়
- business insights বের করা সম্ভব

---

## 🧠 Key Concepts (Quick Revision)

- `crosstab()` → frequency table
- `aggfunc='sum'` → total value
- `aggfunc='mean'` → average value
- `normalize='index'` → row percentage
- `normalize='columns'` → column percentage

---

## 📝 Notes

- crosstab = pivot table এর lightweight version
- real-world reporting এ খুব বেশি ব্যবহার হয়
- categorical comparison analysis সহজ করে

---

## 📌 Next Day Preview

👉 Day 22 — Merge (Very Important)

- inner join
- left join
- right join
- outer join
- multiple dataset combine করা

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- department performance dashboard বানানো
- salary vs location analysis extend করা

### 🧪 Practice Ideas

- নিজের dataset এ crosstab try করো
- different aggfunc দিয়ে experiment করো
