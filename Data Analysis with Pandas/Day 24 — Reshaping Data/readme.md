# 📅 Day 24 — Reshaping Data

---

## 🎯 Objective

- Pandas এ data reshaping (structure change) শেখা
- wide format → long format convert করা
- `melt()`, `stack()`, `unstack()` ব্যবহার করা
- analysis-friendly data structure তৈরি করা
- real-world reporting + ML preprocessing practice করা

---

## 📚 Topics Covered

- `melt()` (wide → long format)
- `stack()` (columns → rows)
- `unstack()` (rows → columns)
- multi-index reshaping
- data transformation techniques
- group-based reshaping analysis

---

## 📁 Project Structure

```id="d24proj"
day-24/
│── 01_melt_basic.py
│── 02_melt_multiple_id.py
│── 03_stack_basic.py
│── 04_unstack_basic.py
│── 05_stack_unstack_group.py
│── 06_real_world_reshaping.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

### 📄 File Name: data.csv

- **Description:** Student marks dataset in wide format

- **Columns:**
  - Name → student name
  - Math → math marks
  - Science → science marks
  - English → english marks

👉 Note: This is **wide format dataset** (subjects as columns)

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry File)

### 🔹 Purpose

- reshaping concept introduction

### 🧾 Code

```python id="r24main"
print("Day 24 - Reshaping Data Learning")
```

### 🧠 Explanation

- learning module entry point
- no transformation logic here

---

## 📄 2. 01_melt_basic.py

### 🔹 Purpose

- wide format → long format convert করা

### 🧾 Code

```python id="r24a"
melted = pd.melt(
    df,
    id_vars=['Name'],
    var_name='Subject',
    value_name='Marks'
)
```

### 🧠 Explanation

- columns → rows convert করে
- analysis-friendly format তৈরি করে

👉 ML / visualization এর জন্য খুব important

---

## 📄 3. 02_melt_multiple_id.py

### 🔹 Purpose

- multiple identifier columns support করা

### 🧾 Code

```python id="r24b"
melted = pd.melt(
    df,
    id_vars=['Name', 'Age'],
    var_name='Subject',
    value_name='Marks'
)
```

### 🧠 Explanation

- একাধিক fixed column রাখা যায়
- student info + marks একসাথে reshape করা হয়

---

## 📄 4. 03_stack_basic.py

### 🔹 Purpose

- column data কে row structure এ convert করা

### 🧾 Code

```python id="r24c"
stacked = df.set_index('Name').stack()
```

### 🧠 Explanation

- columns → single column format
- multi-level index তৈরি হয়

---

## 📄 5. 04_unstack_basic.py

### 🔹 Purpose

- stacked data আবার original format এ আনা

### 🧾 Code

```python id="r24d"
unstacked = stacked.unstack()
```

### 🧠 Explanation

- stack এর reverse operation
- original table structure ফিরে আসে

---

## 📄 6. 05_stack_unstack_group.py

### 🔹 Purpose

- stack + unstack concept practice করা

### 🧾 Code

```python id="r24e"
stacked = df.set_index('Name').stack()
unstacked = stacked.unstack()
```

### 🧠 Explanation

- data structure transformation flow বোঝায়
- indexing behavior clear করে

---

## 📄 7. 06_real_world_reshaping.py

### 🔹 Purpose

- real-world analytics workflow

### 🧾 Code

```python id="r24f"
long_df = pd.melt(df, id_vars=['Name'], var_name='Subject', value_name='Marks')
avg_marks = long_df.groupby('Subject')['Marks'].mean()
```

### 🧠 Explanation

- melt → analysis-friendly format
- groupby → subject-wise average marks
- real data science pipeline

---

## ⚙️ Implementation Flow

- wide format dataset load করা হয়েছে
- melt ব্যবহার করে long format তৈরি করা হয়েছে
- stack/unstack দিয়ে structure পরিবর্তন করা হয়েছে
- groupby দিয়ে analysis করা হয়েছে
- final insights বের করা হয়েছে

---

## 📈 Output / Result

- wide → long conversion সফল হয়েছে
- subject-wise marks analysis হয়েছে
- reshaped dataset তৈরি হয়েছে
- average performance insights পাওয়া গেছে

---

## 🚀 What I Learned

- reshaping = data structure transformation
- wide format = columns-based data
- long format = analysis-friendly format
- melt = most important transformation tool
- stack/unstack = hierarchical reshaping tools

---

## 🧠 Key Concepts (Quick Revision)

- `melt()` → wide to long
- `stack()` → columns to rows
- `unstack()` → rows to columns
- `id_vars` → fixed columns
- `value_vars` → transformed columns

---

## 📝 Notes

- ML models often require long format data
- reshaping = preprocessing step
- stack creates MultiIndex structure
- melt is more flexible than stack

---

## 📌 Next Day Preview

👉 Day 25 — DateTime Basics

- to_datetime()
- dt.year, dt.month, dt.day
- time-based analysis
- date extraction techniques

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- student performance dashboard
- subject-wise ranking system

### 🧪 Practice Ideas

- new dataset add করে melt try করো
- stack vs melt output compare করো
