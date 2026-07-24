# 📅 Day 13 — Apply Function (Pandas)

---

## 🎯 Objective

- Pandas এর `apply()` function শেখা
- custom logic dataset এ apply করা
- lambda function ব্যবহার করা
- row-wise এবং column-wise transformation বোঝা
- real-world feature engineering শুরু করা

---

## 📚 Topics Covered

- apply() function
- lambda function
- row-wise apply (axis=1)
- column-wise apply (axis=0)
- apply vs vectorization
- conditional feature creation

---

## 📁 Project Structure

```id="d13proj"
day-13/
│── 01_apply_basic.py
│── 02_lambda_function.py
│── 03_apply_column_wise.py
│── 04_apply_row_wise.py
│── 05_apply_vs_vectorization.py
│── 06_real_world_apply.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset used for transformation & feature engineering

- **Columns:**
  - Name → employee name
  - Age → age of employee
  - Salary → monthly salary
  - Marks → performance score

👉 এই dataset ব্যবহার করে custom transformation করা হবে

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. `01_apply_basic.py`

### 🔹 Purpose

- basic `apply()` usage বোঝা

### 🧾 Code

```python id="d13c1"
df['Age_plus_1'] = df['Age'].apply(lambda x: x + 1)
```

### 🧠 Explanation

- `apply()` → প্রতিটি value এ function apply করে
- `lambda x` → ছোট anonymous function
- Age এর প্রতিটি value +1 করা হয়েছে

---

## 📄 2. `02_lambda_function.py`

### 🔹 Purpose

- conditional logic তৈরি করা

### 🧾 Code

```python id="d13c2"
df['Salary_Category'] = df['Salary'].apply(
    lambda x: "High" if x > 35000 else "Low"
)
```

### 🧠 Explanation

- salary based classification
- condition ব্যবহার করে category তৈরি করা

---

## 📄 3. `03_apply_column_wise.py`

### 🔹 Purpose

- column-wise operation বোঝা

### 🧾 Code

```python id="d13c3"
df[['Age', 'Salary', 'Marks']].apply(lambda x: x.mean())
```

### 🧠 Explanation

- প্রতিটি column আলাদাভাবে process হয়
- axis=0 (default) → column-wise

---

## 📄 4. `04_apply_row_wise.py`

### 🔹 Purpose

- row-wise logic apply করা

### 🧾 Code

```python id="d13c4"
df.apply(grade, axis=1)
```

### 🧠 Explanation

- `axis=1` → row-wise operation
- পুরো row access করা যায়
- conditional grading system তৈরি করা হয়েছে

---

## 📄 5. `05_apply_vs_vectorization.py`

### 🔹 Purpose

- performance comparison শেখা

### 🧾 Code

```python id="d13c5"
df['Salary'] * 2
df['Salary'].apply(lambda x: x * 2)
```

### 🧠 Explanation

- vectorization (direct operation) faster
- apply slower কিন্তু flexible

---

## 📄 6. `06_real_world_apply.py`

### 🔹 Purpose

- real-world feature engineering

### 🧾 Code

```python id="d13c6"
df['Tax'] = df['Salary'].apply(lambda x: x * 0.10)
df['Net_Salary'] = df['Salary'] - df['Tax']
```

### 🧠 Explanation

- tax calculation system
- performance labeling system
- business logic apply করা হয়েছে

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- apply() ব্যবহার করে transformation করা হয়েছে
- lambda function দিয়ে custom logic লেখা হয়েছে
- row-wise & column-wise processing করা হয়েছে
- real-world features তৈরি করা হয়েছে

---

## 📈 Output / Result

- age updated dataset তৈরি হয়েছে
- salary category তৈরি হয়েছে
- grade system তৈরি হয়েছে
- tax & net salary calculation হয়েছে

---

## 🚀 What I Learned

- apply() = flexible transformation tool
- lambda = quick function writing
- axis=0 vs axis=1 difference
- vectorization faster than apply
- real-world feature engineering শুরু

---

## 🧠 Key Concepts (Quick Revision)

- `apply()` → function apply tool
- `lambda` → small anonymous function
- `axis=0` → column-wise
- `axis=1` → row-wise
- vectorization → fastest operation

---

## 📝 Notes

- apply() powerful but slow for big data
- vectorized operations prefer করা উচিত
- lambda = quick logic writing

---

## 📌 Next Day Preview

👉 Day 14 — Feature Engineering Basics

- new column creation
- arithmetic transformations
- derived features
- real-world data preparation

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- salary grading system
- performance scoring engine

### 🧪 Practice Ideas

- নিজের dataset এ apply() try করো
- custom grading system বানাও
