# 📅 Day 16 — Binning (Pandas)

---

## 🎯 Objective

- Continuous numeric data কে category তে convert করা শেখা
- `cut()` এবং `qcut()` বুঝা এবং ব্যবহার করা
- equal width vs equal frequency difference শেখা
- real-world grouping system তৈরি করা
- data discretization practice করা

---

## 📚 Topics Covered

- cut() (Equal Width Binning)
- qcut() (Equal Frequency Binning)
- custom bins & labels
- categorical feature creation
- numeric → categorical transformation
- real-world grouping system

---

## 📁 Project Structure

```id="d16proj"
day-16/
│── 01_cut_basic.py
│── 02_cut_with_labels.py
│── 03_qcut_basic.py
│── 04_qcut_labels.py
│── 05_categorical_grouping.py
│── 06_real_world_binning.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset used for binning & categorization

- **Columns:**
  - Name → employee name
  - Age → age
  - Salary → monthly income
  - Marks → performance score

👉 continuous numeric data → category conversion করা হবে

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. `01_cut_basic.py`

### 🔹 Purpose

- equal width binning শেখা

### 🧾 Code

```python id="d16c1"
pd.cut(df['Age'], bins=3)
```

### 🧠 Explanation

- data কে equal range এ ভাগ করে
- continuous → categorical conversion

---

## 📄 2. `02_cut_with_labels.py`

### 🔹 Purpose

- custom labels ব্যবহার করা

### 🧾 Code

```python id="d16c2"
pd.cut(df['Age'], bins=[20, 25, 30, 35], labels=['Young', 'Adult', 'Senior'])
```

### 🧠 Explanation

- user-defined categories তৈরি
- age grouping system

---

## 📄 3. `03_qcut_basic.py`

### 🔹 Purpose

- equal frequency binning শেখা

### 🧾 Code

```python id="d16c3"
pd.qcut(df['Salary'], q=3)
```

### 🧠 Explanation

- প্রতিটি group এ equal number of data
- distribution balanced থাকে

---

## 📄 4. `04_qcut_labels.py`

### 🔹 Purpose

- qcut with labels

### 🧾 Code

```python id="d16c4"
pd.qcut(df['Salary'], q=3, labels=['Low', 'Medium', 'High'])
```

### 🧠 Explanation

- salary based classification
- easy interpretation

---

## 📄 5. `05_categorical_grouping.py`

### 🔹 Purpose

- marks → grade conversion

### 🧾 Code

```python id="d16c5"
pd.cut(df['Marks'], bins=[70, 80, 90, 100], labels=['C', 'B', 'A'])
```

### 🧠 Explanation

- academic grading system তৈরি
- performance categorization

---

## 📄 6. `06_real_world_binning.py`

### 🔹 Purpose

- full real-world binning pipeline

### 🧾 Code

```python id="d16c6"
Age → Young/Adult/Senior
Salary → Low/Medium/High
Marks → A/B/C
```

### 🧠 Explanation

- multiple features categorize করা হয়েছে
- business-ready dataset তৈরি

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- numeric values binning করা হয়েছে
- custom labels ব্যবহার করা হয়েছে
- qcut দিয়ে balanced grouping করা হয়েছে
- final categorical dataset তৈরি হয়েছে

---

## 📈 Output / Result

- age groups তৈরি হয়েছে (Young/Adult/Senior)
- salary levels তৈরি হয়েছে (Low/Medium/High)
- marks grading system তৈরি হয়েছে
- dataset fully categorized হয়েছে

---

## 🚀 What I Learned

- binning = continuous → categorical conversion
- cut() = equal width grouping
- qcut() = equal frequency grouping
- labels = readable categories
- feature engineering improvement technique

---

## 🧠 Key Concepts (Quick Revision)

- `cut()` → range-based grouping
- `qcut()` → frequency-based grouping
- bins → interval definition
- labels → category names
- discretization → ML preprocessing step

---

## 📝 Notes

- binning helps simplify complex numeric data
- qcut better for balanced distribution
- cut better for fixed range problems

---

## 📌 Next Day Preview

👉 Day 17 — GroupBy Basics

- groupby concept
- aggregation (mean, sum, count)
- grouped analysis
- data summarization

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- salary segmentation system
- student grading automation tool

### 🧪 Practice Ideas

- নিজের dataset এ cut/qcut try করো
- different bin sizes experiment করো
