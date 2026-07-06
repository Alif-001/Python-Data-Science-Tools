# 📅 Day 10 — Indexing (Deep)

## 🎯 Objective

- NumPy indexing concept deepভাবে বোঝা
- 1D, 2D array access practice করা
- multi/fancy indexing শেখা
- array modify করার skill build করা

---

## 📚 Topics Covered

- 1D indexing (positive & negative)
- 2D indexing (row, column access)
- row/column slicing
- multi indexing (fancy indexing)
- modifying elements (update operations)

---

## 📁 Project Structure

```bash
day-10/
│── 01_1d_indexing.py
│── 02_2d_indexing.py
│── 03_row_column_access.py
│── 04_multi_indexing.py
│── 05_modifying_elements.py
│── 06_practice_combined.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, সবকিছু NumPy indexing practice করার জন্য manually তৈরি করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_1d_indexing.py

#### 🔹 Purpose

- 1D array indexing শেখা
- positive & negative indexing বোঝা

#### 🧾 Code

```python id="a10m1qp"
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])
print(arr[-2])
```

#### 🧠 Explanation

- Line 1 → 1D array তৈরি
- Line 3 → প্রথম element access
- Line 4 → third element
- Line 5 → last element (negative indexing)
- Line 6 → second last element
- Logic → indexing = position-based access

---

### 📄 2. 02_2d_indexing.py

#### 🔹 Purpose

- 2D matrix indexing শেখা

#### 🧾 Code

```python id="b10n2rq"
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr[0][0])
print(arr[1, 2])
print(arr[2, 1])
```

#### 🧠 Explanation

- Line 1 → 2D matrix তৈরি
- Line 5 → row-column access
- Line 6 → alternative indexing method
- Logic → (row, col) format standard

---

### 📄 3. 03_row_column_access.py

#### 🔹 Purpose

- full row & column access শেখা

#### 🧾 Code

```python id="c10p3sw"
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[0])
print(arr[:, 0])
```

#### 🧠 Explanation

- Line 1 → matrix তৈরি
- Line 5 → full row access
- Line 6 → full column access
- Logic → ":" means all elements

---

### 📄 4. 04_multi_indexing.py

#### 🔹 Purpose

- fancy / multi indexing শেখা

#### 🧾 Code

```python id="d10q4tx"
arr = np.array([100, 200, 300, 400, 500])

print(arr[[0, 2, 4]])

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix[[0, 2]])
print(matrix[[0, 1, 2], [0, 1, 2]])
```

#### 🧠 Explanation

- Line 1 → array তৈরি
- Line 3 → multiple index selection
- Line 5 → 2D matrix
- Line 8 → multiple rows select
- Line 9 → diagonal elements extract
- Logic → fancy indexing = advanced selection

---

### 📄 5. 05_modifying_elements.py

#### 🔹 Purpose

- array modify করা শেখা

#### 🧾 Code

```python id="e10r5uv"
arr = np.array([10, 20, 30, 40, 50])

arr[0] = 999

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

matrix[0, 1] = 999
matrix[1] = [100, 200, 300]

print(arr)
print(matrix)
```

#### 🧠 Explanation

- Line 1 → array তৈরি
- Line 3 → single element modify
- Line 5 → matrix তৈরি
- Line 8 → specific element change
- Line 9 → full row update
- Logic → NumPy mutable structure

---

### 📄 6. 06_practice_combined.py

#### 🔹 Purpose

- full indexing practice

#### 🧾 Code

```python id="f10s6wx"
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[1])
print(arr[:, 2])
print(arr[2, 2])

arr[0, 0] = 999
arr[2] = [111, 222, 333]

print(arr)
```

#### 🧠 Explanation

- row access practice
- column access practice
- element modify practice
- full integration of indexing concept

---

## ⚙️ Implementation Flow

- 1D indexing শেখা হয়েছে
- 2D matrix indexing practice করা হয়েছে
- row/column access বোঝা গেছে
- fancy indexing শেখা হয়েছে
- modification operations practice করা হয়েছে

---

## 📈 Output / Result

- indexing concept clear হয়েছে
- matrix navigation skill build হয়েছে
- data manipulation ability উন্নত হয়েছে
- ML-ready indexing foundation তৈরি হয়েছে

---

## 🚀 What I Learned

- arr[i] → 1D access
- arr[row, col] → 2D access
- ":" → full row/column
- fancy indexing → multiple selection
- arrays are mutable

---

## 🧠 Key Concepts (Quick Revision)

- positive index → start from 0
- negative index → end থেকে access
- arr[:, col] → column access
- arr[row] → row access
- arr[[i,j]] → multiple selection

---

## 📝 Notes

- indexing ভুল হলে shape error আসে
- fancy indexing always returns copy-like result
- matrix modify করলে original change হয়

---

## 📌 Next Day Preview

- slicing deep dive
- advanced slicing patterns
- conditional indexing (boolean mask)

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- indexing visualizer tool বানানো যায়
- matrix explorer tool বানানো যায়

### 🧪 Practice Ideas

- নিজের matrix তৈরি করে index practice করো
- diagonal elements manually extract করো
- row/column swap experiment করো
