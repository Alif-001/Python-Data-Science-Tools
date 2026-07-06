# 📅 Day 3 — 2D Array (Matrix Concept)

## 🎯 Objective

- আজকে 2D NumPy array (matrix) বুঝা
- row vs column concept clear করা
- indexing, slicing, update এবং real-life matrix operation শেখা

---

## 📚 Topics Covered

- 2D array creation
- row vs column concept
- indexing (row, column)
- slicing (submatrix extraction)
- value update in matrix

---

## 📁 Project Structure

```bash
day-3/
│── 01_2d_array_creation.py
│── 02_row_column_concept.py
│── 03_indexing_2d.py
│── 04_slicing_submatrix.py
│── 05_update_values.py
│── 06_real_life_matrix.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, সবকিছু NumPy matrix দিয়ে manually তৈরি করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_2d_array_creation.py

#### 🔹 Purpose

- 2D array (matrix) তৈরি করা
- shape এবং dimension বোঝা

#### 🧾 Code

```python id="r9m2qk"
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("2D Array (Matrix):")
print(arr)

print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
```

#### 🧠 Explanation

- Line 1 → NumPy import করা হয়েছে
- Line 3 → 3x3 matrix তৈরি করা হয়েছে
- Line 9 → পুরো matrix print করা হচ্ছে
- Line 13 → shape দেখানো হচ্ছে (rows, columns)
- Line 16 → dimension check করা হচ্ছে (2D)
- Logic → matrix structure বুঝার foundation তৈরি করা হচ্ছে

---

### 📄 2. 02_row_column_concept.py

#### 🔹 Purpose

- row এবং column concept clear করা

#### 🧾 Code

```python id="k2v8pm"
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Row 0:", arr[0])
print("Row 1:", arr[1])

print("Column 0:", arr[:, 0])
print("Column 1:", arr[:, 1])
```

#### 🧠 Explanation

- Line 3 → matrix তৈরি করা হয়েছে
- Line 8 → first row access করা হয়েছে
- Line 9 → second row access করা হয়েছে
- Line 11 → first column বের করা হয়েছে
- Line 12 → second column বের করা হয়েছে
- Logic → row = horizontal data, column = vertical data

---

### 📄 3. 03_indexing_2d.py

#### 🔹 Purpose

- 2D indexing শেখা

#### 🧾 Code

```python id="v4n7xq"
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr[0][0])
print(arr[1][2])
print(arr[2, 1])
```

#### 🧠 Explanation

- Line 3 → matrix তৈরি করা হয়েছে
- Line 8 → row 0, col 0 access করা হয়েছে
- Line 9 → row 1, col 2 access করা হয়েছে
- Line 10 → alternative indexing style
- Logic → element access row-column based

---

### 📄 4. 04_slicing_submatrix.py

#### 🔹 Purpose

- submatrix extract করা শেখা

#### 🧾 Code

```python id="g8p1lz"
import numpy as np

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

sub = arr[0:2, 1:3]

print("Submatrix:")
print(sub)

print(arr[0:2, :])
print(arr[:, 0:2])
```

#### 🧠 Explanation

- Line 3 → matrix তৈরি করা হয়েছে
- Line 9 → submatrix বের করা হয়েছে
- Line 13 → first 2 rows নেওয়া হয়েছে
- Line 14 → first 2 columns নেওয়া হয়েছে
- Logic → slicing দিয়ে part of matrix extract করা যায়

---

### 📄 5. 05_update_values.py

#### 🔹 Purpose

- matrix update operations শেখা

#### 🧾 Code

```python id="h1q7mv"
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr[0, 1] = 999
arr[1] = [100, 200, 300]
arr[:, 2] = [7, 7, 7]

print(arr)
```

#### 🧠 Explanation

- Line 3 → matrix তৈরি করা হয়েছে
- Line 8 → single element update করা হয়েছে
- Line 9 → full row update করা হয়েছে
- Line 10 → column update করা হয়েছে
- Logic → NumPy matrix fully mutable

---

### 📄 6. 06_real_life_matrix.py

#### 🔹 Purpose

- real-life student marks analysis করা

#### 🧾 Code

```python id="x7k2pn"
import numpy as np

marks = np.array([
    [80, 70, 90],
    [60, 75, 85],
    [90, 88, 92]
])

print(marks)

print(marks.mean(axis=1))
print(marks.mean(axis=0))
```

#### 🧠 Explanation

- Line 3 → students × subjects matrix তৈরি করা হয়েছে
- Line 9 → student-wise average বের করা হয়েছে
- Line 10 → subject-wise average বের করা হয়েছে
- Logic → axis concept দিয়ে row/column analysis করা যায়

---

## ⚙️ Implementation Flow

- 2D array তৈরি করা হয়েছে
- row vs column concept বোঝা হয়েছে
- indexing এবং slicing practice করা হয়েছে
- matrix update শেখা হয়েছে
- real-life marks analysis করা হয়েছে

---

## 📈 Output / Result

- 2D array concept clear হয়েছে
- matrix manipulation skill তৈরি হয়েছে
- slicing দিয়ে submatrix extract করা শিখা গেছে
- real-life data analysis শুরু হয়েছে

---

## 🚀 What I Learned

- NumPy matrix = rows + columns structure
- row = horizontal data, column = vertical data
- slicing খুব powerful feature
- axis-based calculation খুব useful

---

## 🧠 Key Concepts (Quick Revision)

- arr[row, col] → element access
- arr[:, col] → column
- arr[row, :] → row
- slicing → submatrix
- axis=0 → column-wise operation
- axis=1 → row-wise operation

---

## 📝 Notes

- indexing ভুল করলে wrong data আসতে পারে
- axis concept খুব important for ML
- matrix thinking future ML foundation

---

## 📌 Next Day Preview

- 3D array (tensor concept)
- image-like structure understanding
- shape manipulation

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- student grading system build করা যায়
- subject ranking system add করা যায়

### 🧪 Practice Ideas

- নিজের 3x3 matrix বানাও
- row/column sum বের করো
- submatrix extract করে practice করো
