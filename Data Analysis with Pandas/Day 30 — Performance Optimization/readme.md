# 📅 Day 30 — Performance Optimization

---

## 🎯 Objective

- Pandas কোডকে fast এবং efficient করা শেখা
- `apply()` vs vectorization পার্থক্য বোঝা
- memory usage optimize করা
- large dataset handling mindset তৈরি করা
- production-level performance thinking develop করা

---

## 📚 Topics Covered

- `apply()` function performance
- vectorization (fast computation)
- direct column operations
- execution speed comparison
- memory optimization (`astype`)
- categorical data optimization
- when to use apply vs vectorization

---

## 📁 Project Structure

```id="d30proj"
day-30/
│── 01_apply_vs_vectorization.py
│── 02_speed_comparison.py
│── 03_direct_operations.py
│── 04_apply_when_needed.py
│── 05_memory_optimization.py
│── 06_category_type_optimization.py
│── 07_real_world_optimization.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

### 📄 File Name: data.csv

- **Description:** Simple numeric dataset used for performance testing

- **Columns:**
  - Value → numeric values for computation

👉 purpose: slow vs fast operation comparison understanding

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Starter)

### 🔹 Purpose

- performance optimization topic start point

### 🧾 Code

```python id="p30main"
print("Day 30 - Performance Optimization")
```

### 🧠 Explanation

- simple entry point
- module initialization

---

## 📄 2. 01_apply_vs_vectorization.py

### 🔹 Purpose

- slow vs fast computation comparison

### 🧾 Code

```python id="p30a"
df['Square_apply'] = df['Value'].apply(lambda x: x * x)
df['Square_vector'] = df['Value'] * df['Value']
```

### 🧠 Explanation

- `apply()` → row-by-row processing (slow)
- vectorization → full column operation (fast)
- vectorization uses optimized C-level execution

---

## 📄 3. 02_speed_comparison.py

### 🔹 Purpose

- execution speed measure করা

### 🧾 Code

```python id="p30b"
df['A'] = df['Value'].apply(lambda x: x + 10)
df['B'] = df['Value'] + 10
```

### 🧠 Explanation

- apply = Python-level loop
- vectorized operation = optimized internal engine
- performance difference measurable

---

## 📄 4. 03_direct_operations.py

### 🔹 Purpose

- fast mathematical operations

### 🧾 Code

```python id="p30c"
df['Add'] = df['Value'] + 5
df['Multiply'] = df['Value'] * 2
df['Divide'] = df['Value'] / 2
```

### 🧠 Explanation

- pandas internally optimized array computation
- no Python loop required
- fastest approach for numeric data

---

## 📄 5. 04_apply_when_needed.py

### 🔹 Purpose

- when apply is actually useful

### 🧾 Code

```python id="p30d"
df['Category'] = df['Value'].apply(
    lambda x: 'High' if x > 50 else 'Low'
)
```

### 🧠 Explanation

- complex conditional logic → apply needed
- simple math → avoid apply
- decision-based transformation

---

## 📄 6. 05_memory_optimization.py

### 🔹 Purpose

- memory usage reduce করা

### 🧾 Code

```python id="p30e"
df['Value'] = df['Value'].astype('int32')
```

### 🧠 Explanation

- int64 → int32 conversion
- memory usage significantly reduce হয়
- large dataset optimization technique

---

## 📄 7. 06_category_type_optimization.py

### 🔹 Purpose

- categorical optimization

### 🧾 Code

```python id="p30f"
df['Value_cat'] = df['Value'].astype('category')
```

### 🧠 Explanation

- repeated values store efficiently
- memory saving technique
- performance improvement in grouping

---

## 📄 8. 07_real_world_optimization.py

### 🔹 Purpose

- full optimization pipeline

### 🧾 Code

```python id="p30g"
df['Square'] = df['Value'] * df['Value']

df['Label'] = df['Value'].apply(
    lambda x: 'Even' if x % 2 == 0 else 'Odd'
)

df['Value'] = df['Value'].astype('int32')
```

### 🧠 Explanation

- vectorization + apply + memory optimization combined
- real-world balanced approach
- production-level data processing mindset

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- vectorized operations applied করা হয়েছে
- apply vs vectorization comparison করা হয়েছে
- memory optimization করা হয়েছে
- categorical optimization tested করা হয়েছে
- final optimized dataset তৈরি করা হয়েছে

---

## 📈 Output / Result

- fast computation achieved using vectorization
- apply vs vectorized performance difference observed
- memory usage reduced
- optimized dataset ready for large-scale processing

---

## 🚀 What I Learned

- vectorization = fastest Pandas operation
- apply = flexible but slow
- memory optimization improves scalability
- dtype conversion saves RAM
- performance thinking is crucial in real projects

---

## 🧠 Key Concepts (Quick Revision)

- `apply()` → flexible but slow
- vectorization → fast column operation
- `astype()` → memory optimization
- `category` → repeated value optimization
- avoid loops in Pandas whenever possible

---

## 📝 Notes

- performance matters in large datasets
- always prefer vectorization
- apply only for complex logic
- memory optimization = production skill

---

## 📌 Next Day Preview

👉 Day 31 — Real Project (Practice Day)

- full dataset cleaning
- feature engineering
- EDA (exploratory data analysis)
- groupby + insights
- real-world mini project

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- benchmark large dataset performance
- build optimization checklist tool

### 🧪 Practice Ideas

- rewrite all apply operations into vectorized form
- test memory usage before/after optimization
- create performance comparison notebook
