# 📅 Day 23 — Join & Concat

---

## 🎯 Objective

- Pandas এ `join()` এবং `concat()` বুঝা ও ব্যবহার করা
- index-based vs column-based merging পার্থক্য শেখা
- multiple dataset একসাথে combine করা
- real-world data pipeline তৈরি করা
- salary + bonus based compensation analysis করা

---

## 📚 Topics Covered

- `join()` (index-based merging)
- `concat()` (row-wise & column-wise)
- `axis=0` vs `axis=1`
- multiple dataset stacking
- merge vs join vs concat difference
- real-world data combining

---

## 📁 Project Structure

```id="d23proj"
day-23/
│── 01_join_basic.py
│── 02_concat_row_wise.py
│── 03_concat_column_wise.py
│── 04_concat_multiple_files.py
│── 05_concat_row_multiple.py
│── 06_real_world_combine.py
│── employees.csv
│── salary.csv
│── bonus.csv
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

- **Description:** Salary dataset

- **Columns:**
  - EmpID → employee ID
  - Salary → monthly salary

---

### 📄 File Name: bonus.csv

- **Description:** Bonus dataset

- **Columns:**
  - EmpID → employee ID
  - Bonus → performance bonus

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry File)

### 🔹 Purpose

- day setup / concept introduction

### 🧾 Code

```python id="c23main"
print("Day 23 - Join & Concat Learning")
```

### 🧠 Explanation

- learning module initialization file

---

## 📄 2. 01_join_basic.py

### 🔹 Purpose

- index-based dataset join করা

### 🧾 Code

```python id="j23a"
df = emp.join(sal)
```

### 🧠 Explanation

- `join()` index ভিত্তিতে কাজ করে
- EmpID কে index বানাতে হয়
- fast and simple merging

---

## 📄 3. 02_concat_row_wise.py

### 🔹 Purpose

- dataset vertically stack করা

### 🧾 Code

```python id="j23b"
df = pd.concat([emp, emp], axis=0)
```

### 🧠 Explanation

- `axis=0` → নিচে নিচে add হয়
- data duplication / stacking এর মতো কাজ

---

## 📄 4. 03_concat_column_wise.py

### 🔹 Purpose

- dataset horizontally combine করা

### 🧾 Code

```python id="j23c"
df = pd.concat([emp, sal], axis=1)
```

### 🧠 Explanation

- `axis=1` → পাশে পাশে যুক্ত হয়
- column expansion করে

---

## 📄 5. 04_concat_multiple_files.py

### 🔹 Purpose

- multiple dataset একসাথে merge করা

### 🧾 Code

```python id="j23d"
df = pd.concat([emp, sal, bonus], axis=1)
```

### 🧠 Explanation

- multiple sources combine
- full table build করা

---

## 📄 6. 05_concat_row_multiple.py

### 🔹 Purpose

- dataset stacking simulation

### 🧾 Code

```python id="j23e"
df = pd.concat([emp, emp, emp], axis=0)
```

### 🧠 Explanation

- same data repeat করে stacking
- data augmentation concept

---

## 📄 7. 06_real_world_combine.py

### 🔹 Purpose

- real-world HR compensation system

### 🧾 Code

```python id="j23f"
df = pd.merge(emp, sal, on='EmpID', how='left')
df = pd.merge(df, bonus, on='EmpID', how='left')
df['Total_Pay'] = df['Salary'] + df['Bonus']
```

### 🧠 Explanation

- step-by-step pipeline
- salary + bonus combine
- total compensation calculation

👉 real business analytics flow

---

## ⚙️ Implementation Flow

- employee dataset load করা হয়েছে
- salary dataset merge করা হয়েছে
- bonus dataset যুক্ত করা হয়েছে
- concat & join techniques applied হয়েছে
- final compensation calculation করা হয়েছে

---

## 📈 Output / Result

- employee full compensation dataset তৈরি হয়েছে
- salary + bonus combined analysis হয়েছে
- multiple dataset integration সফলভাবে করা হয়েছে
- real-world HR reporting simulation হয়েছে

---

## 🚀 What I Learned

- `join()` = index-based merge
- `concat()` = simple stacking tool
- `axis=0` → vertical combine
- `axis=1` → horizontal combine
- real-world pipelines multiple step data integration হয়

---

## 🧠 Key Concepts (Quick Revision)

- `join()` → index-based merge
- `concat(axis=0)` → row-wise stacking
- `concat(axis=1)` → column-wise merge
- merge vs join vs concat difference
- multi-source data integration

---

## 📝 Notes

- join works only on index
- concat does not require key column
- real-world systems often use all three
- careful with NaN after horizontal concat

---

## 📌 Next Day Preview

👉 Day 24 — Reshaping Data

- melt
- stack
- unstack
- wide vs long format conversion
- data restructuring techniques

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- salary dashboard with bonus tracking
- department-wise total compensation analysis

### 🧪 Practice Ideas

- add new dataset (tax, allowance)
- build full payroll system using merge + concat
