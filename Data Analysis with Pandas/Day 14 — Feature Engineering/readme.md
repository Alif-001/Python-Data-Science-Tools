# 📅 Day 14 — Feature Engineering (Pandas)

---

## 🎯 Objective

- Raw dataset থেকে নতুন meaningful features তৈরি করা
- arithmetic operations ব্যবহার করে derived column বানানো
- conditional feature engineering শেখা
- real-world ML-ready dataset প্রস্তুত করা
- data transformation বুঝা

---

## 📚 Topics Covered

- new column creation
- arithmetic operations on columns
- column transformation
- conditional feature engineering
- multiple feature generation
- real-world feature engineering pipeline

---

## 📁 Project Structure

```id="d14proj"
day-14/
│── 01_new_column_basic.py
│── 02_arithmetic_operations.py
│── 03_column_transformation.py
│── 04_conditional_feature.py
│── 05_multiple_features.py
│── 06_real_world_feature_engineering.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset used for feature engineering practice

- **Columns:**
  - Name → employee name
  - Age → age of employee
  - Salary → monthly salary
  - Marks → performance score

👉 এই raw data থেকে নতুন features তৈরি করা হবে

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. `01_new_column_basic.py`

### 🔹 Purpose

- নতুন column তৈরি করা

### 🧾 Code

```python id="d14c1"
df['Bonus'] = df['Salary'] * 0.10
```

### 🧠 Explanation

- existing column থেকে new feature তৈরি
- Salary এর 10% bonus হিসাব করা হয়েছে

---

## 📄 2. `02_arithmetic_operations.py`

### 🔹 Purpose

- multiple column থেকে নতুন feature তৈরি

### 🧾 Code

```python id="d14c2"
df['Total_Income'] = df['Salary'] + df['Bonus']
```

### 🧠 Explanation

- Salary + Bonus = Total Income
- arithmetic operations used (+, -, \*, /)

---

## 📄 3. `03_column_transformation.py`

### 🔹 Purpose

- data transformation শেখা

### 🧾 Code

```python id="d14c3"
df['Salary_K'] = df['Salary'] / 1000
```

### 🧠 Explanation

- salary scaling করা হয়েছে
- readable format তৈরি

---

## 📄 4. `04_conditional_feature.py`

### 🔹 Purpose

- condition-based feature creation

### 🧾 Code

```python id="d14c4"
df['Performance'] = df['Marks'].apply(
    lambda x: "Excellent" if x >= 90 else "Good"
)
```

### 🧠 Explanation

- marks অনুযায়ী category তৈরি
- real-world grading system

---

## 📄 5. `05_multiple_features.py`

### 🔹 Purpose

- multiple features একসাথে তৈরি করা

### 🧾 Code

```python id="d14c5"
df['Tax'] = df['Salary'] * 0.05
df['Net_Salary'] = df['Salary'] - df['Tax']
```

### 🧠 Explanation

- multiple derived columns
- salary calculation system

---

## 📄 6. `06_real_world_feature_engineering.py`

### 🔹 Purpose

- full feature engineering pipeline

### 🧾 Code

```python id="d14c6"
df['Salary_Category'] = df['Salary'].apply(lambda x: "High" if x > 40000 else "Low")
df['Grade'] = df['Marks'].apply(lambda x: "A" if x >= 90 else "B")
```

### 🧠 Explanation

- salary segmentation
- performance grading
- ML-ready dataset তৈরি

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- new columns তৈরি করা হয়েছে
- arithmetic transformation applied হয়েছে
- conditional features তৈরি করা হয়েছে
- final enriched dataset তৈরি হয়েছে

---

## 📈 Output / Result

- bonus column তৈরি হয়েছে
- net salary calculated হয়েছে
- performance grading system তৈরি হয়েছে
- salary category তৈরি হয়েছে
- ML-ready dataset প্রস্তুত হয়েছে

---

## 🚀 What I Learned

- feature engineering = raw data → meaningful data
- new column = new insight
- transformation = data scaling & modification
- conditional logic = smart categorization
- multiple features improve ML model quality

---

## 🧠 Key Concepts (Quick Revision)

- new column → feature creation
- arithmetic ops → derived values
- apply + lambda → conditional features
- transformation → data modification
- feature engineering → ML foundation

---

## 📝 Notes

- feature engineering is most important step in ML pipeline
- better features = better model accuracy
- real-world data always needs transformation

---

## 📌 Next Day Preview

👉 Day 15 — Scaling & Normalization

- min-max scaling
- normalization
- data standardization concept
- numeric transformation techniques

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- salary prediction features
- performance scoring system
- employee ranking system

### 🧪 Practice Ideas

- নিজের dataset এ feature create করো
- salary + tax + bonus system বানাও
