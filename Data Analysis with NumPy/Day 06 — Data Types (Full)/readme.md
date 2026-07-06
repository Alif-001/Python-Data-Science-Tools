# 📅 Day 6 — Data Types (Full)

## 🎯 Objective

- আজকে NumPy-এর data types (int, float, bool, string) বোঝা
- upcasting concept clear করা
- dtype manually control করা শেখা
- astype() ব্যবহার করে conversion করা
- memory optimization (int8 vs int64) বুঝা

---

## 📚 Topics Covered

- int, float, bool, string dtype
- upcasting concept (automatic type conversion)
- manual dtype selection
- astype() conversion
- memory optimization (int8 vs int64)

---

## 📁 Project Structure

```bash
day-6/
│── 01_basic_dtypes.py
│── 02_upcasting.py
│── 03_manual_dtype.py
│── 04_astype_conversion.py
│── 05_memory_optimization.py
│── 06_practice_summary.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, সবকিছু NumPy data types practice এর জন্য manually তৈরি করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_basic_dtypes.py

#### 🔹 Purpose

- NumPy-এর basic data types বুঝা (int, float, bool, string)

#### 🧾 Code

```python id="a6k1qp"
import numpy as np

arr_int = np.array([1, 2, 3])
print("Integer array:", arr_int)
print("dtype:", arr_int.dtype)

arr_float = np.array([1.5, 2.7, 3.0])
print("\nFloat array:", arr_float)
print("dtype:", arr_float.dtype)

arr_bool = np.array([True, False, True])
print("\nBoolean array:", arr_bool)
print("dtype:", arr_bool.dtype)

arr_str = np.array(["a", "b", "c"])
print("\nString array:", arr_str)
print("dtype:", arr_str.dtype)
```

#### 🧠 Explanation

- Line 3 → integer array তৈরি করা হয়েছে
- Line 8 → float array তৈরি করা হয়েছে
- Line 13 → boolean array তৈরি করা হয়েছে
- Line 18 → string array তৈরি করা হয়েছে
- Logic → NumPy automatically data type detect করে

---

### 📄 2. 02_upcasting.py

#### 🔹 Purpose

- automatic type conversion (upcasting) বোঝা

#### 🧾 Code

```python id="b7m2rq"
import numpy as np

arr1 = np.array([1, 2, 3.5])
print("dtype:", arr1.dtype)

arr2 = np.array([1, 2, "hello"])
print("dtype:", arr2.dtype)

arr3 = np.array([True, False, 1])
print("dtype:", arr3.dtype)
```

#### 🧠 Explanation

- Line 3 → int + float → float (upcast)
- Line 6 → int + string → সব string
- Line 9 → bool + int → int (True=1, False=0)
- Logic → NumPy always safe type conversion করে

---

### 📄 3. 03_manual_dtype.py

#### 🔹 Purpose

- manual dtype control করা শেখা

#### 🧾 Code

```python id="c8n3sw"
import numpy as np

arr = np.array([100, 200, 300], dtype=np.int16)

arr_f = np.array([1, 2, 3], dtype=np.float32)
arr_f2 = np.array([1, 2, 3], dtype=np.float64)

print(arr)
print(arr.dtype)

print(arr_f)
print(arr_f2)
```

#### 🧠 Explanation

- Line 3 → int16 manually set করা হয়েছে
- Line 5 → float32 ব্যবহার করা হয়েছে (memory efficient)
- Line 6 → float64 default precision
- Logic → dtype control করলে memory optimize করা যায়

---

### 📄 4. 04_astype_conversion.py

#### 🔹 Purpose

- dtype conversion using astype()

#### 🧾 Code

```python id="d9p4tx"
import numpy as np

arr = np.array([1, 2, 3, 4])

arr_float = arr.astype(np.float64)

arr2 = np.array([1.9, 2.7, 3.5])
arr_int = arr2.astype(np.int32)

print(arr_float)
print(arr_int)
```

#### 🧠 Explanation

- Line 3 → original integer array
- Line 5 → float conversion
- Line 7 → float array তৈরি
- Line 8 → int conversion (decimal loss হবে)
- Logic → astype() দিয়ে type change করা যায়

---

### 📄 5. 05_memory_optimization.py

#### 🔹 Purpose

- memory usage compare করা (int8 vs int64)

#### 🧾 Code

```python id="e1q5uv"
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5], dtype=np.int64)
arr2 = np.array([1, 2, 3, 4, 5], dtype=np.int8)

print(arr1.nbytes)
print(arr2.nbytes)
```

#### 🧠 Explanation

- Line 3 → big memory integer array
- Line 4 → small memory optimized array
- Line 6 → memory usage comparison
- Logic → ML dataset বড় হলে memory optimization গুরুত্বপূর্ণ

---

### 📄 6. 06_practice_summary.py

#### 🔹 Purpose

- mixed dtype practice

#### 🧾 Code

```python id="f2r6wx"
import numpy as np

arr = np.array([1, 2, 3, 4.5, True])

arr_int = arr.astype(np.int32)
arr_float = arr.astype(np.float32)

print(arr)
print(arr_int)
print(arr_float)
```

#### 🧠 Explanation

- Line 3 → mixed type array তৈরি
- Line 5 → int conversion
- Line 6 → float conversion
- Logic → data preprocessing-এর জন্য type conversion খুব important

---

## ⚙️ Implementation Flow

- basic data types বোঝা হয়েছে
- upcasting behavior দেখা হয়েছে
- manual dtype control করা হয়েছে
- astype() দিয়ে conversion practice করা হয়েছে
- memory optimization concept শেখা হয়েছে

---

## 📈 Output / Result

- NumPy data type system clear হয়েছে
- automatic type conversion বোঝা গেছে
- memory saving idea এসেছে
- preprocessing concept strong হয়েছে

---

## 🚀 What I Learned

- NumPy single dtype maintain করে
- upcasting automatically হয়
- astype() দিয়ে conversion করা যায়
- small dtype = less memory usage

---

## 🧠 Key Concepts (Quick Revision)

- int → whole number
- float → decimal number
- bool → True/False
- string → text
- upcasting → automatic safe conversion
- astype() → manual conversion
- int8 < int64 memory wise

---

## 📝 Notes

- dtype mismatch হলে NumPy auto convert করে
- ML dataset-এ memory optimization খুব গুরুত্বপূর্ণ
- float32 often used in deep learning

---

## 📌 Next Day Preview

- array creation methods
- zeros, ones, full
- identity matrix (eye)
- structured array building

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- memory calculator tool বানানো যায়
- dtype converter utility বানানো যায়

### 🧪 Practice Ideas

- different dtype arrays create করো
- memory compare করো
- astype() দিয়ে conversion practice করো
