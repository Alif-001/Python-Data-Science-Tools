# 📅 Day 16 — Aggregation & Statistics

## 🎯 Objective

- আজকে NumPy aggregation functions শেখা
- data summary (mean, sum, min, max) বোঝা
- variability (std, var) concept clear করা
- axis-wise computation practice করা
- cumulative functions (cumsum, cumprod) শেখা

---

## 📚 Topics Covered

- sum, mean, min, max
- variance & standard deviation
- axis concept (row vs column)
- cumulative sum (cumsum)
- cumulative product (cumprod)
- real-world statistics usage

---

## 📁 Project Structure

```bash
day-16/
│── 01_basic_aggregation.py
│── 02_std_var.py
│── 03_axis_concept_1d.py
│── 04_axis_2d_basic.py
│── 05_axis_deep_understanding.py
│── 06_cumulative_functions.py
│── 07_2d_cumulative_axis.py
│── 08_real_world_stats.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি। সব statistics concept NumPy array দিয়ে manually practice করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_basic_aggregation.py

#### 🔹 Purpose

- basic statistical aggregation শেখা
- sum, mean, min, max বুঝা

#### 🧾 Code

```python id="d16m1"
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → array তৈরি
- Line 5 → total sum বের করা
- Line 6 → average calculation
- Line 7 → minimum value
- Line 8 → maximum value
- Logic → dataset summary statistics দেয়

---

### 📄 2. 02_std_var.py

#### 🔹 Purpose

- variance এবং standard deviation বোঝা

#### 🧾 Code

```python id="d16m2"
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(np.var(arr))
print(np.std(arr))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → dataset
- Line 5 → variance (data spread measure)
- Line 6 → standard deviation (spread intensity)
- Logic → data কতটা spread তা বোঝায়

---

### 📄 3. 03_axis_concept_1d.py

#### 🔹 Purpose

- 1D array-এ axis concept বোঝা

#### 🧾 Code

```python id="d16m3"
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))
print(np.mean(arr))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → 1D array
- Line 5 → sum (axis concept simple)
- Line 6 → mean
- Logic → 1D array এ axis আলাদা effect নেই

---

### 📄 4. 04_axis_2d_basic.py

#### 🔹 Purpose

- 2D array axis concept শেখা
- row-wise এবং column-wise operation বোঝা

#### 🧾 Code

```python id="d16m4"
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))
print(np.mean(arr, axis=1))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-6 → matrix
- axis=0 → column-wise operation
- axis=1 → row-wise operation
- Logic → axis direction determine করে operation

---

### 📄 5. 05_axis_deep_understanding.py

#### 🔹 Purpose

- axis concept deep understanding
- row vs column behavior analyze করা

#### 🧾 Code

```python id="d16m5"
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))
print(np.min(arr, axis=0))
print(np.max(arr, axis=1))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-6 → dataset
- axis=0 → column operation
- axis=1 → row operation
- Logic → aggregation direction control করে axis

---

### 📄 6. 06_cumulative_functions.py

#### 🔹 Purpose

- cumulative sum এবং product শেখা

#### 🧾 Code

```python id="d16m6"
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(np.cumsum(arr))
print(np.cumprod(arr))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → array
- Line 5 → running total (cumsum)
- Line 6 → running multiplication (cumprod)
- Logic → step-by-step accumulation

---

### 📄 7. 07_2d_cumulative_axis.py

#### 🔹 Purpose

- 2D cumulative operations বোঝা
- axis-wise cumulative calculation

#### 🧾 Code

```python id="d16m7"
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.cumsum(arr, axis=0))
print(np.cumsum(arr, axis=1))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-6 → matrix
- axis=0 → column-wise cumulative
- axis=1 → row-wise cumulative
- Logic → running sum direction অনুযায়ী পরিবর্তন হয়

---

### 📄 8. 08_real_world_stats.py

#### 🔹 Purpose

- real-world statistics usage বোঝা
- marks dataset analysis করা

#### 🧾 Code

```python id="d16m8"
import numpy as np

marks = np.array([45, 55, 60, 35, 80, 90])

print("Mean:", np.mean(marks))
print("Max:", np.max(marks))
print("Min:", np.min(marks))
print("Std deviation:", np.std(marks))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → marks dataset
- Line 5 → average performance
- Line 6 → best score
- Line 7 → worst score
- Line 8 → consistency check
- Logic → data analysis in real-life scenarios

---

## ⚙️ Implementation Flow

- basic aggregation শেখা হয়েছে
- statistical measures (mean, var, std) বোঝা হয়েছে
- axis concept clear হয়েছে
- cumulative functions practice করা হয়েছে
- real-world dataset analysis করা হয়েছে

---

## 📈 Output / Result

- dataset summary করতে পারা যাচ্ছে
- data spread measure বোঝা যাচ্ছে
- row/column-wise analysis clear হয়েছে
- running total concept শেখা গেছে

---

## 🚀 What I Learned

- aggregation data summarize করে
- variance data spread measure করে
- std consistency বোঝায়
- axis operation direction control করে
- cumsum/cumprod running calculation দেয়

---

## 🧠 Key Concepts (Quick Revision)

- sum → total value
- mean → average
- var → spread
- std → deviation
- axis=0 → column-wise
- axis=1 → row-wise
- cumsum → running sum
- cumprod → running product

---

## 📝 Notes

- axis বুঝা খুব গুরুত্বপূর্ণ
- std বেশি হলে data inconsistent
- cumulative functions ML feature engineering এ use হয়
- statistics ML foundation

---

## 📌 Next Day Preview

- advanced statistical analysis
- correlation concept
- covariance
- real ML feature statistics

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- stats calculator tool বানানো যায়
- dataset analyzer project বানানো যায়

### 🧪 Practice Ideas

- নিজের dataset দিয়ে mean/std বের করো
- axis-based sum practice করো
- cumsum দিয়ে pattern analyze করো
