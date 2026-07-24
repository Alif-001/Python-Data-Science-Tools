# 📅 Day 22 — Merge (Very Important)

---

## 🎯 Objective

- Pandas এ dataset merge করার ধারণা শেখা
- SQL-style join বুঝা (inner, left, right, outer)
- multiple dataset একসাথে combine করা
- missing data handling (NaN) বোঝা
- real-world database joining logic practice করা

---

## 📚 Topics Covered

- `pd.merge()` basics
- inner join
- left join
- right join
- outer join
- multi-table merge
- missing value handling after join

---

## 📁 Project Structure

```id="d22proj"
day-22/
│── 01_inner_join.py
│── 02_left_join.py
│── 03_right_join.py
│── 04_outer_join.py
│── 05_merge_multiple_keys.py
│── 06_real_world_merge.py
│── employees.csv
│── salary.csv
│── README.md
```

---

## 📊 Dataset

### 📄 File Name: employees.csv

- **Description:** Employee information dataset

- **Columns:**
  - EmpID → unique employee ID
  - Name → employee name
  - Department → department name

---

### 📄 File Name: salary.csv

- **Description:** Employee salary dataset

- **Columns:**
  - EmpID → employee ID (join key)
  - Salary → monthly salary

👉 Note: EmpID = 6 only exists in salary file (important join case)

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry File)

### 🔹 Purpose

- merge concept overview file (optional entry point)

### 🧾 Code

```python id="m22main"
import pandas as pd

print("Day 22 - Merge Concept Learning")
```

### 🧠 Explanation

- project start indicator file
- concept initialization

---

## 📄 2. 01_inner_join.py

### 🔹 Purpose

- common records only extract করা

### 🧾 Code

```python id="m22i"
merged = pd.merge(emp, sal, on='EmpID', how='inner')
```

### 🧠 Explanation

- দুই table এর common data রাখে
- EmpID: 1,2,3,4 only
- unmatched data remove হয়

---

## 📄 3. 02_left_join.py

### 🔹 Purpose

- left dataset fully preserve করা

### 🧾 Code

```python id="m22l"
merged = pd.merge(emp, sal, on='EmpID', how='left')
```

### 🧠 Explanation

- employees table full থাকবে
- missing salary → NaN

---

## 📄 4. 03_right_join.py

### 🔹 Purpose

- right dataset fully preserve করা

### 🧾 Code

```python id="m22r"
merged = pd.merge(emp, sal, on='EmpID', how='right')
```

### 🧠 Explanation

- salary table full থাকবে
- EmpID=6 থাকবে কিন্তু employee info NaN

---

## 📄 5. 04_outer_join.py

### 🔹 Purpose

- সব data combine করা

### 🧾 Code

```python id="m22o"
merged = pd.merge(emp, sal, on='EmpID', how='outer')
```

### 🧠 Explanation

- সব records রাখা হয়
- missing জায়গায় NaN fill হয়

---

## 📄 6. 05_merge_multiple_keys.py

### 🔹 Purpose

- multiple dataset merge practice

### 🧾 Code

```python id="m22m"
merged = pd.merge(emp, dept_info, on='Department', how='left')
```

### 🧠 Explanation

- department ভিত্তিতে extra info যোগ হয়
- real-world enrichment step

---

## 📄 7. 06_real_world_merge.py

### 🔹 Purpose

- real business analysis flow

### 🧾 Code

```python id="m22rw"
df = pd.merge(emp, sal, on='EmpID', how='left')
df['Salary'] = df['Salary'].fillna(0)
total_salary = df['Salary'].sum()
```

### 🧠 Explanation

- dataset merge করা
- missing salary handle করা
- total payroll calculation

👉 real HR analytics workflow

---

## ⚙️ Implementation Flow

- employee dataset load করা হয়েছে
- salary dataset load করা হয়েছে
- different join types applied করা হয়েছে
- missing data handle করা হয়েছে
- final business metric (salary sum) বের করা হয়েছে

---

## 📈 Output / Result

- combined employee-salary dataset তৈরি হয়েছে
- missing data identified হয়েছে
- full HR payroll analysis হয়েছে
- join concepts clearly understood হয়েছে

---

## 🚀 What I Learned

- merge = database join concept
- inner join = intersection
- left join = full left table
- right join = full right table
- outer join = full union
- real-world data integration possible

---

## 🧠 Key Concepts (Quick Revision)

- `inner join` → common records only
- `left join` → left table full
- `right join` → right table full
- `outer join` → all data
- `NaN` → missing join data

---

## 📝 Notes

- join mismatch = very common real-world problem
- always check key column before merging
- NaN handling is critical after merge

---

## 📌 Next Day Preview

👉 Day 23 — Join & Concat

- join vs merge difference
- concat row-wise
- concat column-wise
- dataset stacking techniques

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- salary report dashboard তৈরি করা
- department-wise payroll analysis

### 🧪 Practice Ideas

- new dataset add করে merge try করো
- different join type change করে output compare করো
