# 📅 Day 7 — Array Creation Methods (Full)

## 🎯 Objective

- আজকে NumPy-এর বিভিন্ন array creation methods শেখা
- structured data তৈরি করার different ways বোঝা
- real-world matrix generation practice করা

---

## 📚 Topics Covered

- np.array (basic array creation)
- zeros, ones, empty, full
- \_like functions (zeros_like, ones_like, full_like)
- identity matrix (eye)
- diagonal matrix (diag)

---

## 📁 Project Structure

```bash
day-7/
│── 01_np_array_basic.py
│── 02_zeros_ones.py
│── 03_empty_full.py
│── 04_like_functions.py
│── 05_identity_matrix_eye.py
│── 06_diagonal_matrix_diag.py
│── 07_practice_summary.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, সবকিছু NumPy array creation methods practice করার জন্য manually তৈরি করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_np_array_basic.py

#### 🔹 Purpose

- basic np.array() দিয়ে array তৈরি করা
- 1D এবং 2D structure বোঝা

#### 🧾 Code

```python id="a7m1qp"
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print("dtype:", arr.dtype)
print("shape:", arr.shape)

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("\n2D Array:\n", arr2)
print("shape:", arr2.shape)
print("ndim:", arr2.ndim)
```

#### 🧠 Explanation

- Line 3 → 1D array তৈরি করা হয়েছে
- Line 6 → dtype দেখা হচ্ছে
- Line 7 → shape check করা হচ্ছে
- Line 9 → 2D matrix তৈরি করা হয়েছে
- Line 14 → matrix structure print করা হয়েছে
- Logic → np.array() হলো basic building block

---

### 📄 2. 02_zeros_ones.py

#### 🔹 Purpose

- zeros এবং ones array তৈরি করা শেখা

#### 🧾 Code

```python id="b8n2rq"
import numpy as np

arr_zero = np.zeros((3, 4))
print("Zeros Array:\n", arr_zero)

arr_one = np.ones((2, 3))
print("\nOnes Array:\n", arr_one)
```

#### 🧠 Explanation

- Line 3 → সব 0 দিয়ে matrix তৈরি করা হয়েছে
- Line 6 → shape (3x4) structure
- Line 9 → সব 1 দিয়ে matrix তৈরি
- Logic → initialization tasks-এর জন্য খুব useful

---

### 📄 3. 03_empty_full.py

#### 🔹 Purpose

- empty এবং full array বোঝা

#### 🧾 Code

```python id="c9p3sw"
import numpy as np

arr_empty = np.empty((3, 3))
print("Empty Array:\n", arr_empty)

arr_full = np.full((2, 4), 7)
print("\nFull Array:\n", arr_full)
```

#### 🧠 Explanation

- Line 3 → uninitialized memory array তৈরি
- Line 6 → garbage values থাকতে পারে
- Line 9 → সব elements 7 দিয়ে fill করা হয়েছে
- Logic → empty = fast but unsafe, full = controlled

---

### 📄 4. 04_like_functions.py

#### 🔹 Purpose

- existing array থেকে shape copy করা শেখা

#### 🧾 Code

```python id="d1q4tx"
import numpy as np

base = np.array([[1, 2, 3],
                 [4, 5, 6]])

z = np.zeros_like(base)
o = np.ones_like(base)
f = np.full_like(base, 9)

print(base)
print(z)
print(o)
print(f)
```

#### 🧠 Explanation

- Line 3 → base matrix তৈরি
- Line 6 → same shape, সব 0
- Line 7 → same shape, সব 1
- Line 8 → same shape, custom value
- Logic → shape reuse করে fast array generation

---

### 📄 5. 05_identity_matrix_eye.py

#### 🔹 Purpose

- identity matrix এবং diagonal shift বোঝা

#### 🧾 Code

```python id="e2r5uv"
import numpy as np

I = np.eye(4)
I2 = np.eye(3, 5)
I3 = np.eye(4, k=1)

print(I)
print(I2)
print(I3)
```

#### 🧠 Explanation

- Line 3 → 4x4 identity matrix
- Line 4 → rectangular identity matrix
- Line 5 → diagonal shift (k=1)
- Logic → identity matrix ML এবং linear algebra-এ খুব important

---

### 📄 6. 06_diagonal_matrix_diag.py

#### 🔹 Purpose

- diagonal matrix তৈরি এবং extract করা

#### 🧾 Code

```python id="f3s6wx"
import numpy as np

arr = np.diag([1, 2, 3, 4])

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

diag_values = np.diag(matrix)

print(arr)
print(diag_values)
```

#### 🧠 Explanation

- Line 3 → 1D থেকে diagonal matrix তৈরি
- Line 6 → 3x3 matrix তৈরি
- Line 10 → diagonal values extract করা হয়েছে
- Logic → diag() দুইভাবে কাজ করে (create + extract)

---

### 📄 7. 07_practice_summary.py

#### 🔹 Purpose

- সব methods একসাথে practice করা

#### 🧾 Code

```python id="g4t7yx"
import numpy as np

base = np.array([1, 2, 3])

a = np.zeros_like(base)
b = np.ones_like(base)
c = np.full_like(base, 5)

eye = np.eye(3)
diag = np.diag([10, 20, 30])

print(base, a, b, c)
print(eye)
print(diag)
```

#### 🧠 Explanation

- Line 3 → base array তৈরি
- Line 5 → different shape-based arrays
- Line 9 → identity matrix
- Line 10 → diagonal matrix
- Logic → all creation methods practice summary

---

## ⚙️ Implementation Flow

- basic array creation শেখা হয়েছে
- zeros/ones/full ব্যবহার করা হয়েছে
- like-functions দিয়ে shape reuse করা হয়েছে
- identity matrix তৈরি করা হয়েছে
- diagonal matrix practice করা হয়েছে

---

## 📈 Output / Result

- array generation methods clear হয়েছে
- matrix initialization skills build হয়েছে
- ML-friendly initialization idea এসেছে

---

## 🚀 What I Learned

- np.array → basic building block
- zeros/ones → initialization
- empty → fast but unsafe
- full → controlled fill
- eye → identity matrix
- diag → diagonal operations

---

## 🧠 Key Concepts (Quick Revision)

- np.zeros((m,n)) → all 0
- np.ones((m,n)) → all 1
- np.empty() → uninitialized memory
- np.full() → custom value fill
- np.eye() → identity matrix
- np.diag() → diagonal create/extract

---

## 📝 Notes

- empty array avoid in production
- eye matrix linear algebra core concept
- like functions reduce repetition
- dtype default float in most cases

---

## 📌 Next Day Preview

- array reshape & range functions
- arange, linspace, logspace
- flatten vs ravel

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- matrix generator tool বানানো যায়
- identity checker utility বানানো যায়

### 🧪 Practice Ideas

- different shape matrix create করো
- identity matrix experiment করো
- diagonal extract practice করো
