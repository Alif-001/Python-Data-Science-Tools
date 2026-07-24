# 📅 Day 17 — GroupBy Basics (Pandas)

---

## 🎯 Objective

- GroupBy concept বুঝা এবং ব্যবহার করা
- category অনুযায়ী data group করা শেখা
- aggregation (mean, sum, count) করা শেখা
- real-world departmental analysis করা
- grouped data থেকে insights বের করা

---

## 📚 Topics Covered

- groupby() concept
- count per group
- mean per group
- sum per group
- aggregation (agg)
- multi-statistics analysis
- real-world grouping insights

---

## 📁 Project Structure

```id="d17proj"
day-17/
│── 01_groupby_intro.py
│── 02_groupby_count.py
│── 03_groupby_mean.py
│── 04_groupby_sum.py
│── 05_groupby_multiple_stats.py
│── 06_real_world_groupby.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset grouped by Department

- **Columns:**
  - Name → employee name
  - Department → work department
  - Age → age of employee
  - Salary → monthly income

👉 Department based analysis করা হবে

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. `01_groupby_intro.py`

### 🔹 Purpose

- groupby concept বোঝা

### 🧾 Code

```python id="d17c1"
df.groupby('Department')
```

### 🧠 Explanation

- same category অনুযায়ী grouping হয়
- এটি একটি group object তৈরি করে
- actual result পেতে aggregation দরকার

---

## 📄 2. `02_groupby_count.py`

### 🔹 Purpose

- প্রতি group এ count বের করা

### 🧾 Code

```python id="d17c2"
df.groupby('Department')['Name'].count()
```

### 🧠 Explanation

- প্রতিটি department এ কতজন employee আছে
- frequency analysis করা হয়

---

## 📄 3. `03_groupby_mean.py`

### 🔹 Purpose

- average calculation per group

### 🧾 Code

```python id="d17c3"
df.groupby('Department')['Salary'].mean()
```

### 🧠 Explanation

- department-wise average salary
- central tendency analysis

---

## 📄 4. `04_groupby_sum.py`

### 🔹 Purpose

- total calculation per group

### 🧾 Code

```python id="d17c4"
df.groupby('Department')['Salary'].sum()
```

### 🧠 Explanation

- total salary per department
- business level aggregation

---

## 📄 5. `05_groupby_multiple_stats.py`

### 🔹 Purpose

- multiple statistics একসাথে বের করা

### 🧾 Code

```python id="d17c5"
df.groupby('Department')['Salary'].agg(['mean', 'sum', 'max', 'min'])
```

### 🧠 Explanation

- একসাথে multiple metrics
- data summary report তৈরি

---

## 📄 6. `06_real_world_groupby.py`

### 🔹 Purpose

- real-world analysis

### 🧾 Code

```python id="d17c6"
group['Age'].mean()
group['Salary'].max()
```

### 🧠 Explanation

- department-wise insights
- highest paid department identify করা

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- department অনুযায়ী grouping করা হয়েছে
- count, mean, sum apply করা হয়েছে
- multiple aggregation ব্যবহার করা হয়েছে
- insights extract করা হয়েছে

---

## 📈 Output / Result

- প্রতিটি department এ employee count পাওয়া গেছে
- average salary per department বের হয়েছে
- total salary calculation হয়েছে
- highest paid department identify করা হয়েছে

---

## 🚀 What I Learned

- groupby = category-based analysis
- aggregation = summary statistics
- count = frequency analysis
- mean/sum = business insights
- group analysis = real-world data skill

---

## 🧠 Key Concepts (Quick Revision)

- `groupby()` → grouping data
- `count()` → frequency
- `mean()` → average
- `sum()` → total
- `agg()` → multiple stats

---

## 📝 Notes

- groupby is most powerful analysis tool in Pandas
- business insights mostly come from grouping
- aggregation = decision making support

---

## 📌 Next Day Preview

👉 Day 18 — GroupBy Advanced

- multiple column grouping
- transform vs aggregate
- filter in groups
- advanced group analysis

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- department salary dashboard
- HR analytics system

### 🧪 Practice Ideas

- নিজের dataset group করে analysis করো
- different aggregation try করো
