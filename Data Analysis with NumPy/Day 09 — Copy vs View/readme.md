# 📅 Day 9 — Copy vs View

## 🎯 Objective

- NumPy-তে copy vs view concept clear করা
- shallow copy vs deep copy বোঝা
- memory sharing behavior বুঝা
- ML pipeline-এ safe data handling শেখা

---

## 📚 Topics Covered

- reference behavior (Python list vs NumPy)
- view concept (shared memory)
- .copy() method (deep copy)
- reshape view behavior
- ML real-world safe data usage

---

## 📁 Project Structure

```bash
day-9/
│── 01_reference_problem.py
│── 02_numpy_view_basic.py
│── 03_copy_method.py
│── 04_view_vs_copy_demo.py
│── 05_shape_view_behavior.py
│── 06_real_world_ml_example.py
│── 07_summary.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, সবকিছু copy vs view behavior understanding এর জন্য manually তৈরি করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_reference_problem.py

#### 🔹 Purpose

- Python list reference behavior বোঝা

#### 🧾 Code

```python id="a9m1qp"
a = [1, 2, 3]
b = a

b[0] = 100

print(a)
print(b)
```

#### 🧠 Explanation

- Line 1 → list তৈরি
- Line 2 → same memory reference
- Line 4 → change করলে দুইটাই পরিবর্তন হয়
- Logic → Python list = reference-based (dangerous)

---

### 📄 2. 02_numpy_view_basic.py

#### 🔹 Purpose

- NumPy view concept বোঝা

#### 🧾 Code

```python id="b9n2rq"
arr = np.array([1, 2, 3, 4, 5])

view_arr = arr[1:4]

view_arr[0] = 999

print(arr)
print(view_arr)
```

#### 🧠 Explanation

- Line 3 → array তৈরি
- Line 5 → slicing = view তৈরি
- Line 7 → change করলে original affect হয়
- Logic → view = shared memory

---

### 📄 3. 03_copy_method.py

#### 🔹 Purpose

- deep copy concept বোঝা

#### 🧾 Code

```python id="c9p3sw"
arr = np.array([10, 20, 30, 40])

copied = arr.copy()

copied[0] = 999

print(arr)
print(copied)
```

#### 🧠 Explanation

- Line 1 → array তৈরি
- Line 3 → independent memory copy
- Line 5 → change করলে original unaffected
- Logic → copy = safe data handling

---

### 📄 4. 04_view_vs_copy_demo.py

#### 🔹 Purpose

- view vs copy comparison

#### 🧾 Code

```python id="d1q4tx"
arr = np.array([1, 2, 3, 4, 5])

view_arr = arr[1:4]
copy_arr = arr[1:4].copy()

view_arr[0] = 111
copy_arr[0] = 222

print(arr)
```

#### 🧠 Explanation

- view → shared memory
- copy → independent memory
- Logic → behavior difference clearly visible

---

### 📄 5. 05_shape_view_behavior.py

#### 🔹 Purpose

- reshape view behavior বোঝা

#### 🧾 Code

```python id="e2r5uv"
arr = np.arange(1, 7)

reshaped = arr.reshape(2, 3)

reshaped[0][0] = 999

print(arr)
```

#### 🧠 Explanation

- reshape → often view তৈরি করে
- change করলে original array change হয়
- Logic → memory sharing concept deep understanding

---

### 📄 6. 06_real_world_ml_example.py

#### 🔹 Purpose

- ML pipeline-এ safe copy usage

#### 🧾 Code

```python id="f3s6wx"
data = np.array([10, 20, 30, 40, 50])

train_data = data.copy()

train_data = train_data / 10

print(data)
print(train_data)
```

#### 🧠 Explanation

- Line 1 → dataset তৈরি
- Line 3 → safe copy নেওয়া
- Line 5 → normalization করা হয়েছে
- Logic → original dataset protect করা গুরুত্বপূর্ণ

---

### 📄 7. 07_summary.py

#### 🔹 Purpose

- full concept summary practice

#### 🧾 Code

```python id="g4t7yx"
arr = np.array([1, 2, 3, 4, 5])

view = arr[1:4]
copy = arr.copy()

view[0] = 999
copy[0] = 888

print(arr)
print(view)
print(copy)
```

#### 🧠 Explanation

- view → original affect করে
- copy → independent থাকে
- Logic → final concept reinforcement

---

## ⚙️ Implementation Flow

- Python reference behavior বোঝা হয়েছে
- NumPy view concept শেখা হয়েছে
- deep copy (.copy()) ব্যবহার করা হয়েছে
- reshape behavior observe করা হয়েছে
- ML safe data handling practice করা হয়েছে

---

## 📈 Output / Result

- memory sharing concept clear হয়েছে
- view vs copy difference clear হয়েছে
- ML pipeline safety concept এসেছে
- NumPy behavior deeply understood হয়েছে

---

## 🚀 What I Learned

- Python list = reference based
- NumPy slicing = view
- .copy() = independent memory
- reshape often = view
- ML-এ copy use করা safe

---

## 🧠 Key Concepts (Quick Revision)

- view → shared memory
- copy → separate memory
- slicing → view তৈরি করে
- reshape → often view
- ML pipeline → always copy recommended

---

## 📝 Notes

- view fast but risky
- copy safe but memory heavy
- ML dataset modify করার আগে copy করা best practice

---

## 📌 Next Day Preview

- indexing deep dive
- fancy indexing
- boolean indexing
- advanced slicing patterns

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- memory tracker tool বানানো যায়
- view vs copy visualizer বানানো যায়

### 🧪 Practice Ideas

- view modify করে observe করো
- copy modify করে compare করো
- reshape behavior test করো
