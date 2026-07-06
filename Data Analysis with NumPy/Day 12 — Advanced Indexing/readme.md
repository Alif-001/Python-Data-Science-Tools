# 📅 Day 12 — Advanced Indexing

## 🎯 Objective

- NumPy advanced indexing concept শেখা
- fancy indexing deeply practice করা
- row-column pair selection বোঝা
- boolean + fancy indexing difference clear করা
- ML/data filtering skill build করা

---

## 📚 Topics Covered

- fancy indexing (1D & 2D)
- indexing with index arrays
- row-column cross indexing
- boolean vs fancy indexing comparison
- advanced matrix selection patterns

---

## 📁 Project Structure

```bash
day-12/
│── 01_fancy_indexing_1d.py
│── 02_fancy_indexing_2d.py
│── 03_row_column_cross_indexing.py
│── 04_boolean_vs_fancy_mix.py
│── 05_advanced_matrix_selection.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, NumPy array ব্যবহার করে advanced indexing practice করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_fancy_indexing_1d.py

#### 🔹 Purpose

- 1D fancy indexing শেখা
- multiple index একসাথে access করা

#### 🧾 Code

```python id="d12f1"
arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[[0, 2, 4]])
print(arr[[5, 1, 3]])
print(arr[[1, 1, 2]])
```

#### 🧠 Explanation

- Line 1 → 1D array তৈরি
- Line 3 → multiple index selection
- Line 4 → order change করে access
- Line 5 → duplicate index allowed
- Logic → fancy indexing = list-based selection

---

### 📄 2. 02_fancy_indexing_2d.py

#### 🔹 Purpose

- 2D row/column fancy indexing

#### 🧾 Code

```python id="d12f2"
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr[[0, 2]])
print(arr[:, [0, 2]])
```

#### 🧠 Explanation

- Line 1 → matrix তৈরি
- Line 3 → specific rows select
- Line 4 → specific columns select
- Logic → row/column filtering

---

### 📄 3. 03_row_column_cross_indexing.py

#### 🔹 Purpose

- row-column pair selection শেখা

#### 🧾 Code

```python id="d12f3"
arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])

rows = [0,1,2]
cols = [2,1,0]

print(arr[rows, cols])
```

#### 🧠 Explanation

- Line 1 → matrix তৈরি
- Line 3 → row index list
- Line 4 → column index list
- Line 6 → pair-wise selection
- Logic → (row[i], col[i]) mapping

---

### 📄 4. 04_boolean_vs_fancy_mix.py

#### 🔹 Purpose

- fancy vs boolean indexing comparison

#### 🧾 Code

```python id="d12f4"
arr = np.array([5,10,15,20,25,30])

print(arr[[0,3,5]])
print(arr[arr > 15])
```

#### 🧠 Explanation

- Line 3 → fancy indexing (fixed positions)
- Line 4 → boolean filtering (condition-based)
- Logic → selection method difference

---

### 📄 5. 05_advanced_matrix_selection.py

#### 🔹 Purpose

- diagonal-like advanced selection

#### 🧾 Code

```python id="d12f5"
arr = np.array([[11,12,13],
                [21,22,23],
                [31,32,33]])

rows = [0,1,2]
cols = [0,1,2]

print(arr[rows, cols])
```

#### 🧠 Explanation

- Line 1 → matrix তৈরি
- Line 3 → diagonal selection pattern
- Line 6 → main diagonal elements
- Logic → coordinate-based extraction

---

## ⚙️ Implementation Flow

- 1D fancy indexing practice করা হয়েছে
- 2D row/column selection শেখা হয়েছে
- cross indexing concept clear হয়েছে
- boolean vs fancy difference বোঝা গেছে
- diagonal selection pattern শেখা হয়েছে

---

## 📈 Output / Result

- advanced data selection skill build হয়েছে
- ML filtering logic strong হয়েছে
- matrix manipulation ability উন্নত হয়েছে
- indexing confidence increase হয়েছে

---

## 🚀 What I Learned

- arr[[i,j]] → fancy indexing
- arr[:, [cols]] → column selection
- arr[rows, cols] → pair selection
- boolean indexing → condition-based filtering
- fancy indexing → position-based filtering

---

## 🧠 Key Concepts (Quick Revision)

- fancy indexing → list of indices
- boolean indexing → condition filter
- row-column pairing → element mapping
- same index length required for pair selection
- returns copy-like result

---

## 📝 Notes

- fancy indexing is not view (usually copy)
- shape mismatch causes error
- boolean indexing is more flexible for ML
- pair indexing must have equal length lists

---

## 📌 Next Day Preview

- Boolean indexing deep dive
- complex condition filtering
- real-world dataset filtering

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- dataset filtering engine বানানো যায়
- mini query system (like SQL) বানানো যায়

### 🧪 Practice Ideas

- নিজের array থেকে diagonal extract করো
- random index selection practice করো
- condition + fancy mix practice করো
