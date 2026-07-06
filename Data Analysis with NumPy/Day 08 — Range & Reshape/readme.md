# 📅 Day 8 — Range & Reshape

## 🎯 Objective

- আজকে NumPy-এর data generation techniques শেখা
- structured numerical data তৈরি করা
- array reshape এবং memory behavior বোঝা
- flatten vs ravel difference clear করা

---

## 📚 Topics Covered

- np.arange (sequence generation)
- np.linspace (equal interval data)
- np.logspace (log scale data)
- reshape (shape transformation)
- flatten vs ravel (memory behavior)

---

## 📁 Project Structure

```bash
day-8/
│── 01_arange.py
│── 02_linspace.py
│── 03_logspace.py
│── 04_reshape.py
│── 05_flatten_vs_ravel.py
│── 06_practice_combined.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, সবকিছু NumPy range, reshape এবং transformation practice এর জন্য তৈরি করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_arange.py

#### 🔹 Purpose

- sequence-based array তৈরি করা (Python range-এর মতো)

#### 🧾 Code

```python id="a8m1qp"
import numpy as np

arr = np.arange(1, 11, 1)
arr2 = np.arange(0, 20, 2)
arr3 = np.arange(0, 5, 0.5)

print(arr)
print(arr2)
print(arr3)
```

#### 🧠 Explanation

- Line 3 → 1 থেকে 10 পর্যন্ত সংখ্যা তৈরি
- Line 4 → step 2 করে sequence
- Line 5 → float step support
- Logic → controlled sequence generation

---

### 📄 2. 02_linspace.py

#### 🔹 Purpose

- equal interval data তৈরি করা

#### 🧾 Code

```python id="b9n2rq"
import numpy as np

arr = np.linspace(0, 10, 5)
arr2 = np.linspace(0, 1, 10)
x = np.linspace(-5, 5, 100)

print(arr)
print(arr2)
print(x[:10])
```

#### 🧠 Explanation

- Line 3 → 0 থেকে 10 পর্যন্ত equal spacing
- Line 4 → smooth data generation
- Line 5 → graph plotting style data
- Logic → ML + visualization এর জন্য খুব useful

---

### 📄 3. 03_logspace.py

#### 🔹 Purpose

- exponential / logarithmic scale data তৈরি করা

#### 🧾 Code

```python id="c1p3sw"
import numpy as np

arr = np.logspace(1, 3, 5)
arr2 = np.logspace(0, 4, 5, base=2)

print(arr)
print(arr2)
```

#### 🧠 Explanation

- Line 3 → 10^1 to 10^3 scale data
- Line 4 → base 2 exponential growth
- Logic → ML learning rate, scaling problems

---

### 📄 4. 04_reshape.py

#### 🔹 Purpose

- array shape change করা (without changing data)

#### 🧾 Code

```python id="d2q4tx"
import numpy as np

arr = np.arange(1, 13)

mat = arr.reshape(3, 4)
tensor = arr.reshape(2, 2, 3)

print(mat)
print(tensor)
```

#### 🧠 Explanation

- Line 3 → 1D array তৈরি
- Line 5 → 2D matrix (3x4)
- Line 6 → 3D tensor (2x2x3)
- Logic → total elements must match

---

### 📄 5. 05_flatten_vs_ravel.py

#### 🔹 Purpose

- memory behavior difference বোঝা

#### 🧾 Code

```python id="e3r5uv"
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

flat = arr.flatten()
rav = arr.ravel()

flat[0] = 999
rav[0] = 888

print(flat)
print(rav)
print(arr)
```

#### 🧠 Explanation

- Line 3 → 2D array তৈরি
- Line 5 → flatten = copy (safe)
- Line 6 → ravel = view (linked memory)
- Line 8 → flatten change original affect করে না
- Line 9 → ravel change original affect করে
- Logic → memory sharing concept

---

### 📄 6. 06_practice_combined.py

#### 🔹 Purpose

- full workflow practice

#### 🧾 Code

```python id="f4s6wx"
import numpy as np

arr = np.arange(1, 13)
mat = arr.reshape(3, 4)

f = mat.flatten()
r = mat.ravel()

r[0] = 100

print(mat)
```

#### 🧠 Explanation

- Line 3 → range data তৈরি
- Line 4 → reshape করা হয়েছে
- Line 6 → flatten copy তৈরি
- Line 7 → ravel view তৈরি
- Line 9 → modify করলে original change হয়
- Logic → real-world transformation pipeline

---

## ⚙️ Implementation Flow

- sequence generation শেখা হয়েছে
- equal interval data তৈরি করা হয়েছে
- exponential scaling বোঝা হয়েছে
- reshape concept practice করা হয়েছে
- memory view vs copy difference clear হয়েছে

---

## 📈 Output / Result

- data generation techniques clear হয়েছে
- reshape logic strong হয়েছে
- ML-ready data shaping skill build হয়েছে
- memory behavior concept clear হয়েছে

---

## 🚀 What I Learned

- np.arange → step-based sequence
- np.linspace → equal spacing
- np.logspace → exponential scaling
- reshape → structure change
- flatten → copy
- ravel → view

---

## 🧠 Key Concepts (Quick Revision)

- arange → step control
- linspace → equal interval
- logspace → exponential scale
- reshape → shape transform
- flatten → independent copy
- ravel → memory-linked view

---

## 📝 Notes

- reshape করার সময় element count match করতে হবে
- ravel বেশি memory efficient
- flatten safe but slower (copy creation)

---

## 📌 Next Day Preview

- array indexing deep dive
- fancy indexing
- slicing advanced patterns

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- data generator tool বানানো যায়
- reshape validator tool বানানো যায়

### 🧪 Practice Ideas

- different shapes reshape করে দেখো
- flatten vs ravel experiment করো
- linspace graph data বানাও
