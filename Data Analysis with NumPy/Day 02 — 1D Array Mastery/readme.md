# 📅 Day 2 — 1D Array Mastery

## 🎯 Objective

- আজকে 1D NumPy array deepভাবে বুঝা
- indexing, slicing, iteration এবং modification শেখা
- real-life data manipulation practice করা

## 📚 Topics Covered

- 1D array creation
- indexing concept
- slicing technique
- iteration basics
- array modification

---

## 📁 Project Structure

```bash
day-2/
│── 01_1d_array_creation.py
│── 02_indexing.py
│── 03_slicing.py
│── 04_iteration.py
│── 05_modification.py
│── 06_real_life_use.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, সবকিছু NumPy array দিয়ে manually তৈরি করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_1d_array_creation.py

#### 🔹 Purpose

- 1D NumPy array তৈরি করা
- shape এবং dtype বোঝা

#### 🧾 Code

```python id="p1g6qm"
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Shape:", arr.shape)
print("Data type:", arr.dtype)
```

#### 🧠 Explanation

- Line 1 → NumPy import করা হয়েছে
- Line 3 → 1D array তৈরি করা হয়েছে
- Line 5 → পুরো array print করা হচ্ছে
- Line 8 → array-এর shape দেখা হচ্ছে (element count)
- Line 11 → data type check করা হচ্ছে
- Logic → array structure বোঝার foundation তৈরি করা হচ্ছে

---

### 📄 2. 02_indexing.py

#### 🔹 Purpose

- array indexing শেখা

#### 🧾 Code

```python id="z1f0xk"
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])
```

#### 🧠 Explanation

- Line 3 → array তৈরি করা হয়েছে
- Line 5 → first element access করা হচ্ছে
- Line 6 → third element access করা হচ্ছে
- Line 7 → last element access করা হচ্ছে
- Logic → indexing starts from 0 এবং negative index শেষ থেকে শুরু করে

---

### 📄 3. 03_slicing.py

#### 🔹 Purpose

- slicing concept বোঝা

#### 🧾 Code

```python id="8zq4hp"
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[:3])
print(arr[::2])
```

#### 🧠 Explanation

- Line 3 → array তৈরি করা হয়েছে
- Line 5 → index 1 থেকে 3 পর্যন্ত নেওয়া হয়েছে
- Line 6 → first 3 elements নেওয়া হয়েছে
- Line 7 → step slicing (every 2nd element)
- Logic → slicing মানে portion of array extract করা

---

### 📄 4. 04_iteration.py

#### 🔹 Purpose

- array iterate করা শেখা

#### 🧾 Code

```python id="6k2qyx"
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

for value in arr:
    print(value)
```

#### 🧠 Explanation

- Line 3 → array তৈরি করা হয়েছে
- Line 5 → loop দিয়ে প্রতিটি element print করা হচ্ছে
- Logic → NumPy array list-এর মতো iterate করা যায়

---

### 📄 5. 05_modification.py

#### 🔹 Purpose

- array element modify করা শেখা

#### 🧾 Code

```python id="3r8wzn"
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

arr[0] = 100

print("After change:", arr)

arr[1:3] = 999

print("After slicing change:", arr)
```

#### 🧠 Explanation

- Line 3 → array তৈরি করা হয়েছে
- Line 5 → first element পরিবর্তন করা হয়েছে
- Line 8 → slicing করে multiple elements update করা হয়েছে
- Logic → NumPy array mutable এবং fast update support করে

---

### 📄 6. 06_real_life_use.py

#### 🔹 Purpose

- real-life marks update system বোঝা

#### 🧾 Code

```python id="v7q2nm"
import numpy as np

marks = np.array([60, 70, 80, 90])

marks = marks + 5

print("Updated marks:", marks)

marks[1:3] = marks[1:3] + 10

print("Final marks:", marks)
```

#### 🧠 Explanation

- Line 3 → student marks array তৈরি করা হয়েছে
- Line 5 → সবাইকে bonus marks দেওয়া হয়েছে
- Line 8 → selected students-এর extra bonus দেওয়া হয়েছে
- Logic → real-world grading system easily simulate করা যায়

---

## ⚙️ Implementation Flow

- 1D array তৈরি করা হয়েছে
- indexing দিয়ে specific element access করা হয়েছে
- slicing দিয়ে sub-array নেওয়া হয়েছে
- loop দিয়ে iteration করা হয়েছে
- values modify করা হয়েছে
- real-life marks system simulate করা হয়েছে

---

## 📈 Output / Result

- 1D array fully understood
- indexing + slicing clear হয়েছে
- modification concept practice হয়েছে
- real-world data manipulation skill build হয়েছে

---

## 🚀 What I Learned

- NumPy array index-based access support করে
- slicing খুব powerful feature
- array easily modify করা যায়
- real-life problems NumPy দিয়ে model করা যায়

---

## 🧠 Key Concepts (Quick Revision)

- indexing → single element access
- slicing → multiple elements extract
- arr[start:end] → basic slicing rule
- arr[::step] → step slicing
- array mutable

---

## 📝 Notes

- index starts from 0
- negative indexing useful for last elements
- slicing original array modify করতে পারে

---

## 📌 Next Day Preview

- 2D array (matrix concept)
- row vs column understanding
- matrix indexing and slicing

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- marks system আরও advanced করা যায়
- average + grade system add করা যায়

### 🧪 Practice Ideas

- নিজের 10 numbers নিয়ে slicing practice করো
- even/odd filter তৈরি করো
- marks system modify করে try করো
