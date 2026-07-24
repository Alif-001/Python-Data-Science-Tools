# 📅 Day 4 — Advanced Indexing

---

## 🎯 Objective

- Pandas এর advanced indexing concept বোঝা
- `iloc` vs `loc` পার্থক্য শেখা
- row ও column slicing করা শেখা
- label-based vs position-based selection বুঝা

---

## 📚 Topics Covered

- iloc (position-based indexing)
- loc (label-based indexing)
- loc vs iloc comparison
- slicing in Pandas
- index vs position concept

---

## 📁 Project Structure

```id="d4proj"
day-4/
│── 01_iloc_basics.py
│── 02_loc_basics.py
│── 03_loc_vs_iloc.py
│── 04_slicing_basics.py
│── 05_index_vs_position.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset for indexing practice

- **Columns:**
  - Name → employee name
  - Age → employee age
  - City → location
  - Salary → monthly income

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_iloc_basics.py

### 🔹 Purpose

- position-based indexing শেখা (`iloc`)

### 🧾 Code

```python id="iloc4"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.iloc[0])
print(df.iloc[1])

print(df.iloc[0:3])

print(df.iloc[[0, 3, 5]])
```

### 🧠 Explanation

- `iloc[0]` → first row (position 0)
- `iloc[0:3]` → 0 to 2 rows
- `iloc[[0,3,5]]` → specific rows

👉 iloc = purely index position based

---

## 📄 2. 02_loc_basics.py

### 🔹 Purpose

- label-based indexing শেখা (`loc`)

### 🧾 Code

```python id="loc4"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.loc[0])

print(df.loc[0:3])

print(df.loc[0, 'Name'])

print(df.loc[0, ['Name', 'City']])
```

### 🧠 Explanation

- `loc` → label-based selection
- `loc[0:3]` → inclusive slicing (0,1,2,3)
- `loc[row, column]` → row + column select

👉 loc = label/column name based access

---

## 📄 3. 03_loc_vs_iloc.py

### 🔹 Purpose

- loc vs iloc পার্থক্য বোঝা

### 🧾 Code

```python id="cmp4"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.iloc[0])
print(df.loc[0])

print(df.iloc[0:3])
print(df.loc[0:3])
```

### 🧠 Explanation

- `iloc` → index position (0,1,2)
- `loc` → label based (0,1,2,3 inclusive)
- slicing behavior আলাদা

👉 interview favorite topic

---

## 📄 4. 04_slicing_basics.py

### 🔹 Purpose

- row + column slicing শেখা

### 🧾 Code

```python id="slice4"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.iloc[1:5])

print(df.iloc[:, 0:2])

print(df.iloc[1:4, 0:3])

print(df.loc[1:4, ['Name', 'Salary']])
```

### 🧠 Explanation

- `:` → all rows
- `0:2` → column slicing
- `iloc[row, col]` → 2D slicing
- `loc` → column name-based selection

👉 slicing = data subset extraction

---

## 📄 5. 05_index_vs_position.py

### 🔹 Purpose

- index vs position concept clear করা

### 🧾 Code

```python id="ip4"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.iloc[0])
print(df.loc[0])

df2 = df.copy()
df2.index = ['a','b','c','d','e','f','g']

print(df2.loc['a'])
```

### 🧠 Explanation

- position → iloc
- label → loc
- custom index দিলে loc আরও powerful হয়

👉 indexing = pandas core concept

---

# ⚙️ Implementation Flow

1. dataset load করা হয়েছে
2. iloc দিয়ে position-based selection করা হয়েছে
3. loc দিয়ে label-based selection করা হয়েছে
4. slicing concept practice করা হয়েছে
5. loc vs iloc comparison করা হয়েছে

---

## 📈 Output / Result

- row selection clear হয়েছে
- column selection practice হয়েছে
- slicing behavior understood হয়েছে
- loc vs iloc difference mastered হয়েছে

---

## 🚀 What I Learned

- iloc = index position based
- loc = label based
- slicing behavior loc vs iloc এ আলাদা
- indexing is foundation of pandas

---

## 🧠 Key Concepts (Quick Revision)

- `iloc` → position (0,1,2)
- `loc` → label (row name)
- slicing → range selection
- loc includes last index
- iloc excludes last index

---

## 📝 Notes

- indexing mistake হলে wrong data আসতে পারে
- loc বেশি readable for real projects
- iloc faster for position-based operations

---

## 📌 Next Day Preview

👉 Day 5 — Filtering (Very Important)

- condition based selection
- AND / OR filtering
- query method

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- real dataset দিয়ে indexing practice
- custom index set করে experiment করা

## 🧪 Practice Ideas

- নিজের dataset এ loc vs iloc compare করো
- slicing different way try করো
