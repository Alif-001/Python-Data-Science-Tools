# 📅 Day 20 — Pivot Table (Pandas)

---

## 🎯 Objective

- Pivot Table concept বোঝা
- Excel-style data summary তৈরি করা শেখা
- multi-dimensional aggregation করা
- row + column based analysis করা
- real-world business reporting তৈরি করা

---

## 📚 Topics Covered

- pivot_table() basics
- mean/sum/max aggregation
- multi-index pivoting
- column-based grouping
- fill_value handling
- multiple values & aggregations
- real-world pivot analysis

---

## 📁 Project Structure

```id="d20proj"
day-20/
│── 01_pivot_basic.py
│── 02_pivot_multiple_agg.py
│── 03_pivot_columns.py
│── 04_pivot_fillna.py
│── 05_pivot_multiple_values.py
│── 06_real_world_pivot.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset used for pivot table analysis

- **Columns:**
  - Name → employee name
  - Department → work department
  - City → location
  - Salary → monthly income

👉 multi-dimensional summary তৈরি করা হবে

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. `01_pivot_basic.py`

### 🔹 Purpose

- basic pivot table তৈরি করা

### 🧾 Code

```python id="d20c1"
pd.pivot_table(df, values='Salary', index='Department', aggfunc='mean')
```

### 🧠 Explanation

- department-wise average salary
- Excel pivot table এর মতো summary

---

## 📄 2. `02_pivot_multiple_agg.py`

### 🔹 Purpose

- multiple aggregation শেখা

### 🧾 Code

```python id="d20c2"
aggfunc=['mean', 'sum', 'max']
```

### 🧠 Explanation

- একসাথে multiple statistics
- business report তৈরি সহজ হয়

---

## 📄 3. `03_pivot_columns.py`

### 🔹 Purpose

- row + column grouping শেখা

### 🧾 Code

```python id="d20c3"
index='Department',
columns='City'
```

### 🧠 Explanation

- 2D summary table তৈরি হয়
- department vs city analysis

---

## 📄 4. `04_pivot_fillna.py`

### 🔹 Purpose

- missing value handling

### 🧾 Code

```python id="d20c4"
fill_value=0
```

### 🧠 Explanation

- NaN value replace করা হয়
- clean output পাওয়া যায়

---

## 📄 5. `05_pivot_multiple_values.py`

### 🔹 Purpose

- multiple values + aggregation

### 🧾 Code

```python id="d20c5"
values=['Salary']
aggfunc=['mean', 'sum']
```

### 🧠 Explanation

- complex summary report তৈরি
- multiple metrics একসাথে পাওয়া যায়

---

## 📄 6. `06_real_world_pivot.py`

### 🔹 Purpose

- real-world business reporting

### 🧾 Code

```python id="d20c6"
pivot['mean'].mean(axis=1).idxmax()
```

### 🧠 Explanation

- highest average salary department খুঁজে বের করা
- decision making insight

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- pivot table তৈরি করা হয়েছে
- row + column grouping করা হয়েছে
- multiple aggregation applied হয়েছে
- business insight extract করা হয়েছে

---

## 📈 Output / Result

- department-wise salary report তৈরি হয়েছে
- city-based salary comparison হয়েছে
- clean summary table পাওয়া গেছে
- highest salary department identify হয়েছে

---

## 🚀 What I Learned

- pivot table = advanced summary tool
- multi-dimensional analysis possible
- Excel-like reporting in Pandas
- aggregation = business intelligence
- data summarization = decision making support

---

## 🧠 Key Concepts (Quick Revision)

- `pivot_table()` → summary generator
- index → row grouping
- columns → column grouping
- aggfunc → calculation method
- fill_value → missing data handling

---

## 📝 Notes

- pivot table is most used in reporting
- helps convert raw data → business insight
- very useful in analytics dashboards

---

## 📌 Next Day Preview

👉 Day 21 — Crosstab Analysis

- frequency table
- categorical comparison
- normalized tables
- advanced summary views

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- HR salary dashboard
- city vs department salary analyzer

### 🧪 Practice Ideas

- নিজের dataset pivot করে try করো
- multiple aggregation experiment করো
