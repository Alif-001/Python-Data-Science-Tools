# 📅 Day 14 — Vectorization

## 🎯 Objective

- আজকে NumPy vectorization concept শেখা
- array vs array operation বোঝা
- loop ব্যবহার না করে fast computation practice করা
- performance improvement concept clear করা

---

## 📚 Topics Covered

- element-wise operations
- array vs array operations
- scalar operations
- avoiding loops
- performance concept
- broadcasting basic idea

---

## 📁 Project Structure

```bash
day-14/
│── 01_element_wise_operations.py
│── 02_array_scalar_operations.py
│── 03_no_loop_vs_loop.py
│── 04_2d_vectorization.py
│── 05_broadcasting_concept.py
│── 06_performance_comparison.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, সবকিছু NumPy vectorization practice করার জন্য manually তৈরি করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_element_wise_operations.py

#### 🔹 Purpose

- দুইটা array-এর মধ্যে element-wise operations বোঝা
- addition, subtraction, multiplication, division practice করা

#### 🧾 Code

```python id="d14m1"
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)
print(a - b)
print(a * b)
print(b / a)
```

#### 🧠 Explanation

- Line 1 → NumPy import করা হয়েছে
- Line 3-4 → দুইটা 1D array তৈরি করা হয়েছে
- Line 6 → element-wise addition
- Line 7 → element-wise subtraction
- Line 8 → element-wise multiplication
- Line 9 → element-wise division
- Logic → একই position-এর element একসাথে operate হয়

---

### 📄 2. 02_array_scalar_operations.py

#### 🔹 Purpose

- array এর সাথে scalar operation শেখা
- one value দিয়ে পুরো array process করা

#### 🧾 Code

```python id="d14m2"
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr * 5)
print(arr + 2)
print(arr ** 2)
```

#### 🧠 Explanation

- Line 1 → NumPy import করা হয়েছে
- Line 3 → 1D array তৈরি করা হয়েছে
- Line 5 → scalar multiplication
- Line 6 → scalar addition
- Line 7 → power operation
- Logic → প্রতিটা element-এর উপর same operation apply হয়

---

### 📄 3. 03_no_loop_vs_loop.py

#### 🔹 Purpose

- Python loop vs NumPy vectorization compare করা
- কেন vectorization better তা বোঝা

#### 🧾 Code

```python id="d14m3"
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

result_loop = []

for x in arr:
    result_loop.append(x * 2)

print("Loop result:", result_loop)

result_numpy = arr * 2

print("NumPy result:", result_numpy)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → array তৈরি
- Line 5 → loop result store করার জন্য list
- Line 7-8 → loop দিয়ে manually multiply
- Line 12 → direct NumPy operation
- Logic → vectorization shorter, cleaner, faster

---

### 📄 4. 04_2d_vectorization.py

#### 🔹 Purpose

- 2D array-এর উপর vectorized operation বোঝা
- matrix operation practice করা

#### 🧾 Code

```python id="d14m4"
import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [10, 20],
    [30, 40]
])

print(a + b)
print(a * b)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-5 → first matrix
- Line 7-10 → second matrix
- Line 12 → matrix addition
- Line 13 → matrix multiplication
- Logic → একই shape হলে element-wise 2D operations হয়

---

### 📄 5. 05_broadcasting_concept.py

#### 🔹 Purpose

- broadcasting concept-এর basic idea বোঝা
- different shape array operation explore করা

#### 🧾 Code

```python id="d14m5"
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr + 10)

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

print(a + b)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → 1D array
- Line 5 → scalar broadcasting
- Line 7-9 → 2D array
- Line 11 → 1D array automatically expand হয়ে 2D-এর সাথে operate করছে
- Logic → broadcasting shape mismatch handle করতে সাহায্য করে

---

### 📄 6. 06_performance_comparison.py

#### 🔹 Purpose

- loop vs NumPy performance concept বোঝা
- কেন NumPy faster তা observe করা

#### 🧾 Code

```python id="d14m6"
import numpy as np
import time

arr = np.arange(1, 1000000)

start = time.time()

result = []
for x in arr:
    result.append(x * 2)

end = time.time()

print("Loop time:", end - start)

start = time.time()

result_np = arr * 2

end = time.time()

print("NumPy time:", end - start)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 2 → time measurement module import
- Line 4 → large array তৈরি
- Line 6-12 → loop timing
- Line 15-19 → NumPy vectorized timing
- Logic → NumPy compiled backend ব্যবহার করে, তাই loop-এর চেয়ে faster

---

## ⚙️ Implementation Flow

- element-wise operation শেখা হয়েছে
- scalar with array operation practice করা হয়েছে
- loop vs vectorization compare করা হয়েছে
- 2D matrix operation দেখা হয়েছে
- broadcasting concept এর basic idea এসেছে
- performance difference observe করা হয়েছে

---

## 📈 Output / Result

- vectorized code লেখা শিখা গেছে
- loop কমিয়ে faster approach বোঝা গেছে
- array operations cleaner হয়েছে
- performance awareness তৈরি হয়েছে

---

## 🚀 What I Learned

- array operations element-wise হয়
- scalar array-এর সব element-এর উপর কাজ করে
- loop ছাড়াই কাজ করা যায়
- NumPy অনেক বেশি efficient
- broadcasting automatic shape adjustment করে

---

## 🧠 Key Concepts (Quick Revision)

- element-wise operation → position অনুযায়ী operation
- vectorization → loop-free fast computation
- scalar operation → one value apply to full array
- broadcasting → shape adjustment
- NumPy backend fast কারণ compiled

---

## 📝 Notes

- same shape arrays সহজে operate করে
- broadcasting বুঝতে shape awareness দরকার
- বড় data-তে vectorization খুব useful
- loop-based solution usually slower

---

## 📌 Next Day Preview

- broadcasting deep master
- broadcasting rules
- row-column operation
- real-world preprocessing use case

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- loop vs vector benchmark tool বানানো যায়
- mini performance tester বানানো যায়

### 🧪 Practice Ideas

- নিজের array নিয়ে element-wise operation করো
- loop এবং vectorization time compare করো
- 2D matrix operation practice করো
