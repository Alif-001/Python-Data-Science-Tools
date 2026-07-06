# 📅 Day 5 — Array Attributes Deep

## 🎯 Objective

- আজকে NumPy array-এর core attributes বোঝা
- ndim, shape, size, dtype concept clear করা
- memory behavior basic level এ বুঝা

---

## 📚 Topics Covered

- ndim (dimension understanding)
- shape (structure of array)
- size (total elements)
- dtype (data type of array)
- memory concept (basic idea)

---

## 📁 Project Structure

```bash
day-5/
│── 01_ndim_shape_size.py
│── 02_2d_3d_attributes.py
│── 03_dtype_understanding.py
│── 04_memory_concept_basic.py
│── 05_practice_summary.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, সবকিছু NumPy array attributes practice এর জন্য manually তৈরি করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_ndim_shape_size.py

#### 🔹 Purpose

- 1D array-এর basic attributes বোঝা

#### 🧾 Code

```python id="a1k8mq"
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

print("Array:", arr1)
print("Dimension (ndim):", arr1.ndim)
print("Shape:", arr1.shape)
print("Size:", arr1.size)
```

#### 🧠 Explanation

- Line 1 → NumPy import করা হয়েছে
- Line 3 → 1D array তৈরি করা হয়েছে
- Line 5 → array print করা হয়েছে
- Line 8 → dimension দেখা হচ্ছে (1D = 1)
- Line 11 → shape দেখা হচ্ছে (elements count structure)
- Line 14 → total element count বের করা হচ্ছে
- Logic → array structure বোঝার base concept

---

### 📄 2. 02_2d_3d_attributes.py

#### 🔹 Purpose

- 2D এবং 3D array attributes compare করা

#### 🧾 Code

```python id="b2m9qp"
import numpy as np

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("2D Array:\n", arr2)
print("ndim:", arr2.ndim)
print("shape:", arr2.shape)
print("size:", arr2.size)

arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("\n3D Array:\n", arr3)
print("ndim:", arr3.ndim)
print("shape:", arr3.shape)
print("size:", arr3.size)
```

#### 🧠 Explanation

- Line 3 → 2D matrix তৈরি করা হয়েছে

- Line 6 → 2D array print করা হয়েছে

- Line 7 → dimension check করা হয়েছে (2D)

- Line 8 → shape দেখানো হয়েছে (rows, cols)

- Line 9 → size বের করা হয়েছে

- Line 11 → 3D array তৈরি করা হয়েছে

- Line 17 → 3D structure print করা হয়েছে

- Line 18 → dimension (3D)

- Line 19 → shape (depth, row, col)

- Line 20 → total elements count

- Logic → higher dimension = nested structure

---

### 📄 3. 03_dtype_understanding.py

#### 🔹 Purpose

- data type system বোঝা
- type conversion behavior দেখা

#### 🧾 Code

```python id="c3n0qr"
import numpy as np

arr1 = np.array([1, 2, 3])
print("dtype:", arr1.dtype)

arr2 = np.array([1.5, 2.5, 3.7])
print("dtype:", arr2.dtype)

arr3 = np.array([1, 2, 3.5])
print("dtype:", arr3.dtype)

arr4 = np.array([1, 2, "hello"])
print("dtype:", arr4.dtype)
```

#### 🧠 Explanation

- Line 3 → integer array → int type
- Line 6 → float array → float type
- Line 9 → mixed int+float → auto float conversion
- Line 12 → string mixed → সব string হয়ে যায়
- Logic → NumPy single dtype maintain করে (performance reason)

---

### 📄 4. 04_memory_concept_basic.py

#### 🔹 Purpose

- NumPy vs Python list memory concept বোঝা

#### 🧾 Code

```python id="d4p1rt"
import numpy as np

py_list = [1, 2, 3, 4]
print("Python List:", py_list)

np_arr = np.array([1, 2, 3, 4])
print("NumPy Array:", np_arr)
print("dtype:", np_arr.dtype)
```

#### 🧠 Explanation

- Line 3 → Python list তৈরি করা হয়েছে
- Line 6 → NumPy array তৈরি করা হয়েছে
- Line 7 → dtype দেখানো হয়েছে
- Logic → NumPy fixed-type + continuous memory use করে → faster execution

---

### 📄 5. 05_practice_summary.py

#### 🔹 Purpose

- সব attributes একসাথে practice করা

#### 🧾 Code

```python id="e5q2sw"
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr)

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

#### 🧠 Explanation

- Line 3 → 2D array তৈরি করা হয়েছে
- Line 6 → full array print
- Line 8 → dimension check
- Line 9 → structure check
- Line 10 → total elements
- Line 11 → data type
- Logic → complete attribute overview practice

---

## ⚙️ Implementation Flow

- 1D, 2D, 3D array attributes দেখা হয়েছে
- ndim, shape, size, dtype practice করা হয়েছে
- memory concept basic level এ বোঝা হয়েছে
- type conversion behavior observe করা হয়েছে

---

## 📈 Output / Result

- array structure understanding clear হয়েছে
- dtype behavior concept clear হয়েছে
- memory optimization idea এসেছে
- NumPy internal behavior সম্পর্কে ধারণা হয়েছে

---

## 🚀 What I Learned

- ndim → কত dimension
- shape → structure of data
- size → total elements
- dtype → data type consistency
- NumPy uses fixed-type memory for speed

---

## 🧠 Key Concepts (Quick Revision)

- arr.ndim → dimension count
- arr.shape → (rows, cols, depth)
- arr.size → total elements
- arr.dtype → data type
- NumPy = optimized memory + speed

---

## 📝 Notes

- dtype mismatch হলে automatic conversion হয়
- NumPy memory efficient because of fixed type
- shape understanding ML-এর জন্য খুব important

---

## 📌 Next Day Preview

- data types deep dive
- astype conversion
- memory optimization tricks

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- datatype converter tool বানানো যায়
- memory comparison demo বানানো যায়

### 🧪 Practice Ideas

- different arrays create করে attributes check করো
- dtype change করে observe করো
- 2D → 3D shape experiment করো
