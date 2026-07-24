# 📅 Day 15 — Scaling & Transformation (Pandas)

---

## 🎯 Objective

- Numeric data scale করা শেখা
- Min-Max Scaling বুঝা এবং apply করা
- Z-score Normalization শেখা
- multiple column scaling practice করা
- ML-ready dataset প্রস্তুত করা

---

## 📚 Topics Covered

- Min-Max Scaling (0 to 1 range)
- Z-score Normalization
- multiple column scaling
- rounding scaled values
- apply() দিয়ে scaling
- real-world data transformation

---

## 📁 Project Structure

```id="d15proj"
day-15/
│── 01_min_max_scaling.py
│── 02_normalization.py
│── 03_multiple_column_scaling.py
│── 04_rounding_values.py
│── 05_apply_scaling.py
│── 06_real_world_scaling.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee numeric dataset used for scaling & normalization

- **Columns:**
  - Name → employee name
  - Age → age
  - Salary → monthly income
  - Marks → performance score

👉 সব values numeric, scaling এর জন্য perfect dataset

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. `01_min_max_scaling.py`

### 🔹 Purpose

- Min-Max scaling শেখা

### 🧾 Code

```python id="d15c1"
(df['Salary'] - min) / (max - min)
```

### 🧠 Explanation

- data 0 থেকে 1 range এ আনা হয়
- ML model এর জন্য standardized input তৈরি হয়

---

## 📄 2. `02_normalization.py`

### 🔹 Purpose

- Z-score normalization শেখা

### 🧾 Code

```python id="d15c2"
(df['Salary'] - mean) / std
```

### 🧠 Explanation

- mean = 0 centered data
- distribution standardized হয়

---

## 📄 3. `03_multiple_column_scaling.py`

### 🔹 Purpose

- multiple column scaling

### 🧾 Code

```python id="d15c3"
df[['Age', 'Salary', 'Marks']].apply(min_max)
```

### 🧠 Explanation

- একসাথে multiple features scale করা যায়
- ML preprocessing faster হয়

---

## 📄 4. `04_rounding_values.py`

### 🔹 Purpose

- clean output তৈরি করা

### 🧾 Code

```python id="d15c4"
df['Salary_scaled'].round(2)
```

### 🧠 Explanation

- floating values readable করা
- precision control করা হয়

---

## 📄 5. `05_apply_scaling.py`

### 🔹 Purpose

- reusable scaling function

### 🧾 Code

```python id="d15c5"
def min_max(col):
    return (col - col.min()) / (col.max() - col.min())
```

### 🧠 Explanation

- function reuse করা যায়
- multiple dataset এ apply করা সহজ

---

## 📄 6. `06_real_world_scaling.py`

### 🔹 Purpose

- real-world ML preprocessing pipeline

### 🧾 Code

```python id="d15c6"
df['Salary_scaled']
df['Salary_norm']
```

### 🧠 Explanation

- scaling + normalization একসাথে
- ML model ready dataset তৈরি

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- Min-Max scaling apply করা হয়েছে
- Z-score normalization করা হয়েছে
- multiple columns scale করা হয়েছে
- final ML-ready dataset তৈরি হয়েছে

---

## 📈 Output / Result

- salary scaled (0–1 range)
- normalized salary (mean=0)
- age & marks scaled
- clean ML-ready dataset তৈরি হয়েছে

---

## 🚀 What I Learned

- scaling = data range fix করা
- normalization = distribution standard করা
- ML models sensitive to scale
- feature transformation = model performance improve করে
- preprocessing = ML pipeline foundation

---

## 🧠 Key Concepts (Quick Revision)

- Min-Max Scaling → 0 to 1 range
- Z-score → mean centered data
- apply() → reusable transformation
- rounding → clean output
- scaling → ML preprocessing step

---

## 📝 Notes

- scaling না করলে ML model biased হতে পারে
- normalization better for statistical models
- feature scaling = mandatory in ML pipeline

---

## 📌 Next Day Preview

👉 Day 16 — Binning & Categorization

- cut()
- qcut()
- numeric → categorical conversion
- data grouping techniques

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- salary prediction preprocessing pipeline
- ML dataset builder tool

### 🧪 Practice Ideas

- নিজের dataset scale করে try করো
- salary vs marks normalized compare করো
