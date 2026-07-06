# 📅 Day 13 — Boolean Indexing 🔥

## 🎯 Objective

- NumPy Boolean indexing deeply শেখা
- condition-based filtering practice করা
- masking concept বোঝা
- array value replace করা শেখা
- multiple condition (AND / OR / NOT) ব্যবহার করা

---

## 📚 Topics Covered

- boolean indexing (condition filtering)
- masking (True/False array)
- replace values using condition
- multiple conditions (&, |, ~)
- 2D boolean filtering
- real-world data filtering

---

## 📁 Project Structure

```bash
day-13/
│── 01_boolean_basic_filter.py
│── 02_boolean_masking.py
│── 03_replace_values_condition.py
│── 04_multiple_conditions.py
│── 05_2d_boolean_filter.py
│── 06_real_world_masking.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, NumPy array ব্যবহার করে boolean filtering practice করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_boolean_basic_filter.py

#### 🔹 Purpose

- basic condition-based filtering শেখা

#### 🧾 Code

```python id="d13b1"
arr = np.array([10,15,20,25,30,35,40])

print(arr[arr > 20])
print(arr[arr <= 20])
print(arr[arr == 30])
```

#### 🧠 Explanation

- Line 1 → 1D array তৈরি
- Line 3 → greater than 20 filter
- Line 4 → less or equal filter
- Line 5 → exact match filter
- Logic → condition returns True/False mask

---

### 📄 2. 02_boolean_masking.py

#### 🔹 Purpose

- masking concept বোঝা

#### 🧾 Code

```python id="d13b2"
arr = np.array([5,10,15,20,25,30])

mask = arr > 15

print(arr[mask])
```

#### 🧠 Explanation

- Line 3 → boolean mask তৈরি
- Line 5 → mask ব্যবহার করে filtering
- Logic → True index only selected

---

### 📄 3. 03_replace_values_condition.py

#### 🔹 Purpose

- condition-based value replace

#### 🧾 Code

```python id="d13b3"
arr = np.array([10,20,30,40,50])

arr[arr > 30] = 0

arr = np.array([1,2,3,4,5])
arr[arr % 2 == 1] = 99
```

#### 🧠 Explanation

- Line 3 → condition match করে replace
- Line 6 → new array
- Line 7 → odd values replace
- Logic → filtering + mutation

---

### 📄 4. 04_multiple_conditions.py

#### 🔹 Purpose

- AND, OR, NOT condition practice

#### 🧾 Code

```python id="d13b4"
arr = np.array([10,15,20,25,30,35,40])

print(arr[(arr > 15) & (arr < 35)])
print(arr[(arr < 15) | (arr > 35)])
print(arr[~(arr > 25)])
```

#### 🧠 Explanation

- Line 3 → AND condition
- Line 4 → OR condition
- Line 5 → NOT condition
- Logic → multiple filters combine করা যায়

---

### 📄 5. 05_2d_boolean_filter.py

#### 🔹 Purpose

- 2D array boolean filtering

#### 🧾 Code

```python id="d13b5"
arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])

print(arr[arr > 50])

arr[arr < 50] = -1
```

#### 🧠 Explanation

- Line 3 → 2D matrix তৈরি
- Line 5 → flatten করে filter
- Line 7 → condition-based replace
- Logic → matrix filtering automatic flattening

---

### 📄 6. 06_real_world_masking.py

#### 🔹 Purpose

- real-world data filtering practice

#### 🧾 Code

```python id="d13b6"
marks = np.array([45,55,60,35,80,90,20])

passed = marks[marks >= 50]
failed = marks[marks < 50]

marks[marks < 50] += 10
```

#### 🧠 Explanation

- Line 3 → pass filter
- Line 4 → fail filter
- Line 6 → bonus update
- Logic → real dataset cleaning idea

---

## ⚙️ Implementation Flow

- condition-based filtering শেখা হয়েছে
- masking concept clear হয়েছে
- value replace practice করা হয়েছে
- multiple condition apply করা হয়েছে
- real-world data example বোঝা গেছে

---

## 📈 Output / Result

- data filtering skill improve হয়েছে
- ML preprocessing ready skill build হয়েছে
- dataset cleaning logic শেখা হয়েছে
- conditional operations mastery হয়েছে

---

## 🚀 What I Learned

- arr[condition] → boolean indexing
- mask = condition → reusable filter
- & → AND
- | → OR
- ~ → NOT
- condition can modify array directly

---

## 🧠 Key Concepts (Quick Revision)

- boolean array = True/False filter
- only True values selected
- multiple condition must use () brackets
- filtering = data cleaning tool
- modifies original array if assigned

---

## 📝 Notes

- parentheses () required for multiple conditions
- boolean indexing returns copy-like result
- very powerful for ML data preprocessing
- wrong condition → empty array

---

## 📌 Next Day Preview

- broadcasting deep dive
- shape alignment rules
- real-world vector operations

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- mini data filter engine বানানো যায়
- student result analyzer project

### 🧪 Practice Ideas

- নিজের marks dataset filter করো
- multiple condition combine practice করো
- fail/pass/average category বানাও
