# 📅 Day 1 — Introduction + Environment

## 🎯 Objective

- আজকে NumPy কী এবং কেন ব্যবহার করা হয় তা শেখা
- Python list আর NumPy array-এর মধ্যে difference বোঝা
- NumPy installation, import, basic array creation, এবং element-wise operation concept clear করা

## 📚 Topics Covered

- NumPy কী
- NumPy কেন ব্যবহার করা হয়
- installation / import
- Python list vs NumPy array
- basic array creation
- element-wise operation concept

## 📁 Project Structure

```bash
day-1/
│── 01_install_import.py
│── 02_why_numpy.py
│── 03_array_creation.py
│── 04_elementwise_operation.py
│── 05_basic_operations_compare.py
│── 06_real_life_idea.py
│── README.md
```

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো dataset use করা হয়নি, কারণ এটা NumPy introduction day
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

### 📄 1. 01_install_import.py

#### 🔹 Purpose

- NumPy ব্যবহার করতে হলে আগে import করতে হয়
- `np` হলো NumPy-এর short alias, যা convention হিসেবে ব্যবহার করা হয়

#### 🧾 Code

```python
import numpy as np  # np হলো short নাম (convention)

print(np.__version__)
```

#### 🧠 Explanation

- Line 1 → NumPy import করা হয়েছে
- Line 2 → version check করা হচ্ছে
- Logic → library ready কিনা verify করা হচ্ছে

---

### 📄 2. 02_why_numpy.py

#### 🔹 Purpose

- Python list vs NumPy array difference বোঝা

#### 🧾 Code

```python
arr = [1, 2, 3]
print(arr * 5)

import numpy as np
arr_np = np.array([1, 2, 3])
print(arr_np * 5)
```

#### 🧠 Explanation

- List multiply করলে repeat হয়
- NumPy array multiply করলে element-wise operation হয়
- NumPy mathematical computing-এর জন্য optimized

---

### 📄 3. 03_array_creation.py

#### 🔹 Purpose

- 1D এবং 2D array তৈরি করা

#### 🧾 Code

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4])
print(arr1)

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(arr2)
```

#### 🧠 Explanation

- 1D array = simple list-like structure
- 2D array = matrix structure
- NumPy structured data handle করে

---

### 📄 4. 04_elementwise_operation.py

#### 🔹 Purpose

- element-wise operation বোঝা

#### 🧾 Code

```python
import numpy as np

arr = np.array([1, 2, 3])

print(arr + 2)
print(arr * 3)
print(arr ** 2)
```

#### 🧠 Explanation

- প্রতিটা element আলাদা ভাবে operate হয়
- loop ছাড়া computation করা যায়
- NumPy vectorized operation support করে

---

### 📄 5. 05_basic_operations_compare.py

#### 🔹 Purpose

- list vs NumPy performance difference বোঝা

#### 🧾 Code

```python
lst = [1, 2, 3]
print([x * 2 for x in lst])

import numpy as np
arr = np.array([1, 2, 3])
print(arr * 2)
```

#### 🧠 Explanation

- List → manual loop লাগে
- NumPy → direct operation
- Code short + fast

---

### 📄 6. 06_real_life_idea.py

#### 🔹 Purpose

- real-life marks calculation example

#### 🧾 Code

```python
import numpy as np

marks = np.array([50, 60, 70])
print(marks + 5)
```

#### 🧠 Explanation

- marks data array হিসেবে store করা হয়েছে
- bonus marks add করা হয়েছে
- real-world data processing সহজ হয়

---

## ⚙️ Implementation Flow

- NumPy install এবং import করা হয়েছে
- list vs array difference বোঝা হয়েছে
- array creation practice করা হয়েছে
- element-wise operation শেখা হয়েছে
- real-life example apply করা হয়েছে

---

## 📈 Output / Result

- NumPy basic understanding তৈরি হয়েছে
- array operation clear হয়েছে
- vectorized computation idea এসেছে

---

## 🚀 What I Learned

- NumPy is faster than Python list for math
- array supports vectorized operation
- real-life data easily process করা যায়

---

## 🧠 Key Concepts (Quick Revision)

- np.array() → array creation
- list \* n → repetition
- array \* n → element-wise multiply
- NumPy = optimized numerical computing

---

## 📝 Notes

- list vs array behavior different
- np alias standard practice
- small dataset দিয়ে practice করা best

---

## 📌 Next Day Preview

- 1D array indexing
- slicing
- modification

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- marks calculator extend করা যায়
- average, max, min add করা যায়

### 🧪 Practice Ideas

- নিজের marks নিয়ে array বানাও
- total + average বের করো
- list vs NumPy compare করো
