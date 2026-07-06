# 📅 Day 4 — 3D Array (Tensor Basics)

## 🎯 Objective

- আজকে 3D NumPy array (tensor concept) বুঝা
- indexing, slicing এবং shape structure শেখা
- real-world image এবং ML data representation idea পাওয়া

---

## 📚 Topics Covered

- 3D array structure
- 3D indexing system
- shape understanding (depth, rows, columns)
- slicing in 3D array
- real-world image representation

---

## 📁 Project Structure

```bash
day-4/
│── 01_3d_array_structure.py
│── 02_3d_indexing.py
│── 03_shape_understanding.py
│── 04_slicing_3d.py
│── 05_real_world_image_concept.py
│── 06_ml_intuition.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, সবকিছু NumPy 3D array (tensor) দিয়ে manually তৈরি করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_3d_array_structure.py

#### 🔹 Purpose

- 3D array structure বোঝা
- multiple 2D matrix একসাথে stack করা শেখা

#### 🧾 Code

```python id="p9x2qa"
import numpy as np

arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("3D Array:")
print(arr)

print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
```

#### 🧠 Explanation

- Line 1 → NumPy import করা হয়েছে
- Line 3 → 3D array তৈরি করা হয়েছে (2 blocks of matrices)
- Line 12 → পুরো tensor print করা হয়েছে
- Line 16 → shape দেখানো হয়েছে (depth, rows, columns)
- Line 19 → dimension check করা হয়েছে (3D)
- Logic → 3D মানে multiple 2D matrix stack করা

---

### 📄 2. 02_3d_indexing.py

#### 🔹 Purpose

- 3D indexing system শেখা

#### 🧾 Code

```python id="x1k8mz"
import numpy as np

arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(arr[0])
print(arr[1])
print(arr[0, 1, 2])
```

#### 🧠 Explanation

- Line 3 → 3D array তৈরি করা হয়েছে
- Line 13 → first block access করা হয়েছে
- Line 16 → second block access করা হয়েছে
- Line 19 → specific element access করা হয়েছে
- Logic → indexing format: (block, row, column)

---

### 📄 3. 03_shape_understanding.py

#### 🔹 Purpose

- 3D shape breakdown বুঝা

#### 🧾 Code

```python id="u2v9pn"
import numpy as np

arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ],
    [
        [9, 10],
        [11, 12]
    ]
])

print(arr)
print("Shape:", arr.shape)
```

#### 🧠 Explanation

- Line 3 → 3D tensor তৈরি করা হয়েছে
- Line 14 → shape output দেখা হচ্ছে
- Logic → (depth, height, width) structure বোঝা
  - depth → কতগুলো blocks
  - height → rows
  - width → columns

---

### 📄 4. 04_slicing_3d.py

#### 🔹 Purpose

- 3D slicing শেখা
- multi-dimension selection বোঝা

#### 🧾 Code

```python id="k7m1vq"
import numpy as np

arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ],
    [
        [13, 14, 15],
        [16, 17, 18]
    ]
])

print(arr[0:2])
print(arr[0, :, :])
print(arr[:, :, 1])
```

#### 🧠 Explanation

- Line 3 → 3D array তৈরি করা হয়েছে
- Line 18 → first 2 blocks নেওয়া হয়েছে
- Line 21 → first block-এর সব rows/columns নেওয়া হয়েছে
- Line 24 → সব blocks থেকে 2nd column নেওয়া হয়েছে
- Logic → slicing multi-level data extract করতে সাহায্য করে

---

### 📄 5. 05_real_world_image_concept.py

#### 🔹 Purpose

- image কে 3D array হিসেবে বুঝা
- RGB concept শেখা

#### 🧾 Code

```python id="r2q8mv"
import numpy as np

image = np.array([
    [
        [255, 0, 0],
        [0, 255, 0]
    ],
    [
        [0, 0, 255],
        [255, 255, 0]
    ]
])

print(image)
print("Shape:", image.shape)

print("Pixel (0,1):", image[0, 1])
```

#### 🧠 Explanation

- Line 3 → fake RGB image তৈরি করা হয়েছে
- Line 12 → image print করা হয়েছে
- Line 15 → shape দেখানো হয়েছে (height, width, RGB)
- Line 18 → specific pixel access করা হয়েছে
- Logic → image = 3D array (H × W × 3 channels)

---

### 📄 6. 06_ml_intuition.py

#### 🔹 Purpose

- ML dataset structure বোঝা
- 3D array real use case দেখা

#### 🧾 Code

```python id="n8v4qp"
import numpy as np

data = np.random.randint(0, 10, (3, 2, 3))

print(data)

print(data.mean(axis=1))

print(data.reshape(-1))
```

#### 🧠 Explanation

- Line 3 → random 3D dataset তৈরি করা হয়েছে
- Line 5 → dataset print করা হয়েছে
- Line 8 → row-wise mean calculation
- Line 11 → flatten operation করা হয়েছে
- Logic → ML data often multi-dimensional হয়

---

## ⚙️ Implementation Flow

- 3D array structure বোঝা হয়েছে
- indexing system practice করা হয়েছে
- shape breakdown শিখা হয়েছে
- slicing operation করা হয়েছে
- image representation ধারণা এসেছে
- ML data intuition তৈরি হয়েছে

---

## 📈 Output / Result

- 3D tensor concept clear হয়েছে
- image = 3D array idea বোঝা গেছে
- multi-dimensional slicing শিখা গেছে
- ML data structure intuition তৈরি হয়েছে

---

## 🚀 What I Learned

- 3D array = multiple 2D matrices stack
- indexing format = (depth, row, col)
- image data = RGB channels
- ML datasets often high-dimensional

---

## 🧠 Key Concepts (Quick Revision)

- arr[block, row, col] → indexing
- shape → (depth, height, width)
- : → full selection
- RGB → last dimension in image
- flatten → convert multi-D to 1D

---

## 📝 Notes

- 3D visualization initially confusing হতে পারে
- indexing practice খুব গুরুত্বপূর্ণ
- image processing future ML topic

---

## 📌 Next Day Preview

- array attributes deep dive
- dtype understanding
- memory concept basics

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- image editor simulation বানানো যায়
- mini pixel manipulation tool

### 🧪 Practice Ideas

- নিজের 3D array বানাও
- slicing practice করো
- RGB pixel modify করে দেখো
