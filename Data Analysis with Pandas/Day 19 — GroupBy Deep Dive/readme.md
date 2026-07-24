# 📅 Day 19 — GroupBy Deep Dive (Pandas)

---

## 🎯 Objective

- GroupBy এর advanced behavior বোঝা
- group iteration করা শেখা
- `transform()` ব্যবহার করে row-level analysis করা
- `filter()` দিয়ে group-level filtering শেখা
- real-world HR analytics logic তৈরি করা

---

## 📚 Topics Covered

- group iteration
- transform() (row-wise group mapping)
- custom transform logic
- filter() (group-level filtering)
- group size filtering
- group-based feature engineering
- real-world analysis pipeline

---

## 📁 Project Structure

```id="d19proj"
day-19/
│── 01_group_iteration.py
│── 02_transform_basic.py
│── 03_transform_custom.py
│── 04_group_filter.py
│── 05_group_size_filter.py
│── 06_real_world_group_analysis.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset used for deep group analysis

- **Columns:**
  - Name → employee name
  - Department → work department
  - City → location
  - Age → age of employee
  - Salary → monthly income

👉 group-level + row-level analysis করা হবে

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. `01_group_iteration.py`

### 🔹 Purpose

- প্রতিটি group manually iterate করা শেখা

### 🧾 Code

```python id="d19c1"
for dept, group in df.groupby('Department'):
    print(dept)
    print(group)
```

### 🧠 Explanation

- dept → group name
- group → সেই department এর data
- debugging + understanding group structure

---

## 📄 2. `02_transform_basic.py`

### 🔹 Purpose

- transform() শেখা

### 🧾 Code

```python id="d19c2"
df['Dept_Avg_Salary'] = df.groupby('Department')['Salary'].transform('mean')
```

### 🧠 Explanation

- group value প্রতিটি row তে বসে
- output size same থাকে as original

---

## 📄 3. `03_transform_custom.py`

### 🔹 Purpose

- custom row-level transformation

### 🧾 Code

```python id="d19c3"
df['Salary'] - df.groupby('Department')['Salary'].transform('mean')
```

### 🧠 Explanation

- প্রতিটি employee তার department avg থেকে কত দূরে
- deviation analysis করা হয়

---

## 📄 4. `04_group_filter.py`

### 🔹 Purpose

- group-level filtering শেখা

### 🧾 Code

```python id="d19c4"
df.groupby('Department').filter(lambda x: x['Salary'].mean() > 30000)
```

### 🧠 Explanation

- condition group level এ apply হয়
- শুধু valid group retain হয়

---

## 📄 5. `05_group_size_filter.py`

### 🔹 Purpose

- group size filtering

### 🧾 Code

```python id="d19c5"
df.groupby('Department').filter(lambda x: len(x) > 2)
```

### 🧠 Explanation

- minimum employee condition check
- HR analytics use-case

---

## 📄 6. `06_real_world_group_analysis.py`

### 🔹 Purpose

- real-world HR analytics pipeline

### 🧾 Code

```python id="d19c6"
df['High_Earner'] = df['Salary'] > df['Dept_Avg']
```

### 🧠 Explanation

- department average salary calculate
- high earner flag তৈরি
- business insight extraction

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- group iteration করা হয়েছে
- transform দিয়ে row-level features তৈরি করা হয়েছে
- filter দিয়ে group selection করা হয়েছে
- HR insights generate করা হয়েছে

---

## 📈 Output / Result

- department-wise salary analysis হয়েছে
- average salary based feature তৈরি হয়েছে
- high earner identification হয়েছে
- filtered departments পাওয়া গেছে

---

## 🚀 What I Learned

- transform = row-level group mapping
- filter = group-level selection
- iteration = group structure understanding
- group analytics = HR/business intelligence
- advanced pandas = real-world data skill

---

## 🧠 Key Concepts (Quick Revision)

- `groupby()` → grouping
- iteration → manual group access
- `transform()` → same-size output
- `filter()` → group selection
- group logic → business insights

---

## 📝 Notes

- transform is powerful for feature engineering
- filter is useful for segmentation
- group-level thinking = data science mindset

---

## 📌 Next Day Preview

👉 Day 20 — Pivot Table

- pivot_table basics
- multi-dimensional summarization
- reshape data
- advanced aggregation view

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- HR performance dashboard
- salary deviation tracker

### 🧪 Practice Ideas

- নিজের dataset এ transform + filter try করো
- high earner system বানাও
