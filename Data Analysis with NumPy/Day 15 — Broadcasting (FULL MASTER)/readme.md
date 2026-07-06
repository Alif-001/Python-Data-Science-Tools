# 📅 Day 15 — Broadcasting (FULL MASTER) 🔥

## 🎯 Objective

- আজকে NumPy broadcasting concept deep ভাবে শেখা
- different shape array কিভাবে automatically operate করে সেটা বোঝা
- real-world ML use case বুঝা
- row, column, scalar broadcasting practice করা

---

## 📚 Topics Covered

- broadcasting rules
- scalar + array operations
- array + array (different shapes)
- row broadcasting
- column broadcasting
- shape compatibility logic
- real-world ML usage

---

## 📁 Project Structure

```bash
day-15/
│── 01_broadcasting_rules.py
│── 02_scalar_broadcasting.py
│── 03_array_different_shape.py
│── 04_column_broadcasting.py
│── 05_row_broadcasting.py
│── 06_real_world_use_cases.py
│── 07_broadcasting_shape_logic.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি। সব উদাহরণ NumPy broadcasting concept বোঝানোর জন্য manually তৈরি করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_broadcasting_rules.py

#### 🔹 Purpose

- broadcasting rules বোঝা
- same shape array operation বুঝা

#### 🧾 Code

```python id="d15m1"
import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-4 → same shape 1D arrays
- Line 6 → direct element-wise addition
- Logic → same shape হলে direct operation হয়

---

### 📄 2. 02_scalar_broadcasting.py

#### 🔹 Purpose

- scalar value কিভাবে পুরো array তে apply হয় তা শেখা

#### 🧾 Code

```python id="d15m2"
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr + 5)
print(arr * 2)
print(arr ** 2)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → array তৈরি
- Line 5 → scalar automatically সব element এ apply
- Line 6 → multiplication
- Line 7 → power operation
- Logic → scalar broadcasting automatically expand হয়

---

### 📄 3. 03_array_different_shape.py

#### 🔹 Purpose

- different shape array কিভাবে automatically match হয় তা বোঝা

#### 🧾 Code

```python id="d15m3"
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])

print(a + b)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-6 → 2D array
- Line 8 → 1D array
- Line 10 → b automatically row-wise expand হয়
- Logic → smaller array broadcast হয়ে বড় shape এ match করে

---

### 📄 4. 04_column_broadcasting.py

#### 🔹 Purpose

- column-wise broadcasting (vertical expansion) বোঝা

#### 🧾 Code

```python id="d15m4"
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [10],
    [20]
])

print(a + b)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-6 → matrix
- Line 8-11 → column vector
- Line 13 → column-wise expansion হয়
- Logic → (2,1) shape automatically (2,3) এর সাথে match করে

---

### 📄 5. 05_row_broadcasting.py

#### 🔹 Purpose

- row broadcasting concept বোঝা

#### 🧾 Code

```python id="d15m5"
import numpy as np

a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([10, 20, 30])

print(a + b)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-6 → column vector
- Line 8 → row vector
- Line 10 → দুইটা expand হয়ে full matrix তৈরি করে
- Logic → row + column broadcasting combine হয়

---

### 📄 6. 06_real_world_use_cases.py

#### 🔹 Purpose

- real-world ML/CV use case বোঝা
- normalization, scaling, brightness adjustment

#### 🧾 Code

```python id="d15m6"
import numpy as np

data = np.array([10, 20, 30, 40, 50])
mean = 20

normalized = data - mean
print(normalized)

image = np.array([
    [100, 150],
    [200, 250]
])

brightness = 50
print(image + brightness)

features = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

scale = np.array([10, 100, 1000])
print(features * scale)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → dataset
- Line 5 → mean subtraction (centering)
- Line 8 → image array
- Line 12 → brightness adjustment
- Line 15 → feature matrix
- Line 19 → scaling per feature
- Logic → ML preprocessing heavily uses broadcasting

---

### 📄 7. 07_broadcasting_shape_logic.py

#### 🔹 Purpose

- shape compatibility বুঝা
- কোন shape কিভাবে কাজ করে সেটা analyze করা

#### 🧾 Code

```python id="d15m7"
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b1 = np.array([10, 20, 30])
b2 = np.array([[10], [20]])

print(a + b1)
print(a + b2)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-6 → matrix
- Line 8 → (3,) shape
- Line 9 → (2,1) shape
- Line 11 → valid broadcasting
- Line 12 → valid broadcasting
- Logic → shape compatibility rules apply automatically

---

## ⚙️ Implementation Flow

- broadcasting rules শেখা হয়েছে
- scalar operation practice করা হয়েছে
- different shape arrays combine করা হয়েছে
- row/column expansion বোঝা হয়েছে
- real-world ML use case দেখা হয়েছে
- shape logic analysis করা হয়েছে

---

## 📈 Output / Result

- automatic expansion concept clear হয়েছে
- vectorized computation আরও strong হয়েছে
- ML preprocessing idea তৈরি হয়েছে
- shape understanding improve হয়েছে

---

## 🚀 What I Learned

- broadcasting automatic shape matching করে
- scalar পুরো array তে apply হয়
- ছোট array বড় array এর সাথে expand হয়
- ML data preprocessing এ খুব গুরুত্বপূর্ণ
- row/column expansion আলাদা behavior দেখায়

---

## 🧠 Key Concepts (Quick Revision)

- broadcasting → automatic shape alignment
- scalar → single value expansion
- row broadcasting → horizontal expansion
- column broadcasting → vertical expansion
- shape rule → compatibility is key

---

## 📝 Notes

- shape mismatch হলে error আসবে
- broadcasting powerful কিন্তু careful use করতে হয়
- ML preprocessing heavily depends on this
- smaller arrays expand হয় automatically

---

## 📌 Next Day Preview

- advanced broadcasting edge cases
- matrix math deeper understanding
- real ML feature engineering use
- optimization tricks

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- shape checker tool বানানো
- broadcasting visualizer বানানো

### 🧪 Practice Ideas

- নিজের array দিয়ে different shapes test করো
- row vs column broadcasting compare করো
- ML feature scaling practice করো
