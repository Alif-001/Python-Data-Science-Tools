# 📅 Day 11 — Slicing (Deep)

## 🎯 Objective

- NumPy slicing concept deeply বোঝা
- 1D ও 2D array slicing practice করা
- step slicing, reverse slicing শেখা
- sub-array extraction skill build করা
- view vs copy behavior বুঝা

---

## 📚 Topics Covered

- slicing syntax (start:end:step)
- step slicing & reverse slicing
- row slicing (2D)
- column slicing (2D)
- submatrix extraction
- view vs copy in slicing

---

## 📁 Project Structure

```bash
day-11/
│── 01_basic_slicing_1d.py
│── 02_step_slicing.py
│── 03_2d_row_column_slicing.py
│── 04_submatrix_slicing.py
│── 05_modify_slicing.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি, সব slicing practice NumPy array দিয়ে করা হয়েছে
- Columns:
  - column1 → N/A
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_basic_slicing_1d.py

#### 🔹 Purpose

- 1D array slicing basics শেখা

#### 🧾 Code

```python id="d11s1"
arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[::2])
```

#### 🧠 Explanation

- Line 1 → 1D array তৈরি
- Line 3 → index 1 থেকে 3 পর্যন্ত slice
- Line 4 → first 3 elements
- Line 5 → 2 index থেকে end
- Line 6 → step slicing (2 gap)
- Logic → slicing = sub-part extraction

---

### 📄 2. 02_step_slicing.py

#### 🔹 Purpose

- step slicing & reverse concept শেখা

#### 🧾 Code

```python id="d11s2"
arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr[::-1])
print(arr[::3])
print(arr[2:8:2])
```

#### 🧠 Explanation

- Line 3 → reverse array
- Line 4 → every 3rd element
- Line 5 → custom range + step
- Logic → step controls skipping behavior

---

### 📄 3. 03_2d_row_column_slicing.py

#### 🔹 Purpose

- row & column slicing শেখা

#### 🧾 Code

```python id="d11s3"
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr[:2])
print(arr[:, 0])
print(arr[:, 1])
```

#### 🧠 Explanation

- Line 1 → matrix তৈরি
- Line 3 → first 2 rows
- Line 4 → first column
- Line 5 → second column
- Logic → ":" means all rows/columns

---

### 📄 4. 04_submatrix_slicing.py

#### 🔹 Purpose

- submatrix extraction শেখা

#### 🧾 Code

```python id="d11s4"
arr = np.array([[10,20,30,40],
                [50,60,70,80],
                [90,100,110,120]])

print(arr[0:2, 1:3])
print(arr[:, 1:3])
```

#### 🧠 Explanation

- Line 1 → 2D matrix তৈরি
- Line 3 → partial rows + columns
- Line 4 → full rows + selected columns
- Logic → slicing both axis একসাথে কাজ করে

---

### 📄 5. 05_modify_slicing.py

#### 🔹 Purpose

- slicing modify behavior + view vs copy শেখা

#### 🧾 Code

```python id="d11s5"
arr = np.array([10,20,30,40,50])

arr[1:4] = 99

a = np.array([1,2,3,4])
b = a[1:3]

b[0] = 999

c = a[1:3].copy()
c[0] = 500
```

#### 🧠 Explanation

- Line 3 → slice modify করলে original change হয়
- Line 6 → view তৈরি (shared memory)
- Line 8 → view change → original affected
- Line 11 → copy safe (original unaffected)
- Logic → slicing = usually view

---

## ⚙️ Implementation Flow

- 1D slicing শেখা হয়েছে
- step slicing practice করা হয়েছে
- 2D row/column extraction করা হয়েছে
- submatrix extraction বোঝা গেছে
- view vs copy behavior analyze করা হয়েছে

---

## 📈 Output / Result

- data slicing skill উন্নত হয়েছে
- matrix থেকে অংশ বের করতে পারা যায়
- ML preprocessing ready skill build হয়েছে
- memory behavior (view/copy) clear হয়েছে

---

## 🚀 What I Learned

- arr[start:end] → basic slicing
- arr[::step] → step control
- arr[:, col] → column access
- arr[row_start:row_end, col_start:col_end] → submatrix
- slicing usually view (not copy)

---

## 🧠 Key Concepts (Quick Revision)

- ":" → full range
- step → skip control
- negative step → reverse
- 2D slicing → row, column combine
- view → original linked memory
- copy → independent memory

---

## 📝 Notes

- slicing ভুল হলে shape mismatch error আসতে পারে
- view change করলে original array change হয়
- copy safe for ML pipelines
- submatrix slicing খুব important for data analysis

---

## 📌 Next Day Preview

- Boolean indexing (masking)
- condition-based filtering
- advanced selection techniques

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- slicing visual tool বানানো
- matrix explorer app বানানো

### 🧪 Practice Ideas

- নিজের matrix বানিয়ে submatrix extract করো
- reverse slicing experiment করো
- column swapping practice করো
