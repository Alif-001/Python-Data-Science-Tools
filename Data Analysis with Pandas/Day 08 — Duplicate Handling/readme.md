# 📅 Day 8 — Duplicate Handling

---

## 🎯 Objective

- Dataset থেকে duplicate rows identify করা শেখা
- duplicate data remove করা শেখা
- real-world data cleaning strategy develop করা
- `drop_duplicates()` এর advanced usage বোঝা

---

## 📚 Topics Covered

- duplicated() detection
- duplicate filtering
- drop_duplicates() basics
- subset-based duplicate handling
- keep parameter (first, last, False)
- real-world duplicate cleaning flow

---

## 📁 Project Structure

```id="d8proj"
day-8/
│── 01_detect_duplicates.py
│── 02_show_only_duplicates.py
│── 03_drop_duplicates_basic.py
│── 04_drop_duplicates_subset.py
│── 05_keep_options.py
│── 06_real_world_cleaning.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset with duplicate records (real-world scenario)

- **Columns:**
  - Name → employee name
  - Age → employee age
  - City → location
  - Salary → income

👉 কিছু rows intentionally duplicate রাখা হয়েছে practice এর জন্য

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_detect_duplicates.py

### 🔹 Purpose

- duplicate row identify করা

### 🧾 Code

```python id="d8c1"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.duplicated())
print(df.duplicated().sum())
```

### 🧠 Explanation

- `duplicated()` → True/False mask তৈরি করে
- True = duplicate row
- `.sum()` → total duplicate count

👉 duplicate detection = cleaning first step

---

## 📄 2. 02_show_only_duplicates.py

### 🔹 Purpose

- শুধু duplicate rows show করা

### 🧾 Code

```python id="d8c2"
import pandas as pd

df = pd.read_csv("data.csv")

print(df[df.duplicated()])
```

### 🧠 Explanation

- `df[condition]` → filtering
- duplicated rows only return করে

👉 inspection before cleaning is important

---

## 📄 3. 03_drop_duplicates_basic.py

### 🔹 Purpose

- duplicate remove করা

### 🧾 Code

```python id="d8c3"
import pandas as pd

df = pd.read_csv("data.csv")

clean_df = df.drop_duplicates()

print(clean_df)
```

### 🧠 Explanation

- `drop_duplicates()` → duplicate rows remove করে
- first occurrence রাখে

👉 basic deduplication method

---

## 📄 4. 04_drop_duplicates_subset.py

### 🔹 Purpose

- specific column based duplicate remove

### 🧾 Code

```python id="d8c4"
import pandas as pd

df = pd.read_csv("data.csv")

clean_df = df.drop_duplicates(subset=['Name', 'City'])

print(clean_df)
```

### 🧠 Explanation

- `subset` → specific columns check করে
- Name + City same হলে duplicate ধরবে
- Salary ignore করা হয়

👉 smart duplicate detection

---

## 📄 5. 05_keep_options.py

### 🔹 Purpose

- duplicate retention control করা

### 🧾 Code

```python id="d8c5"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.drop_duplicates(keep='first'))
print(df.drop_duplicates(keep='last'))
print(df.drop_duplicates(keep=False))
```

### 🧠 Explanation

- `first` → প্রথম row রাখে
- `last` → শেষ row রাখে
- `False` → সব duplicate remove

👉 control over duplicate handling

---

## 📄 6. 06_real_world_cleaning.py

### 🔹 Purpose

- complete cleaning pipeline

### 🧾 Code

```python id="d8c6"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.duplicated().sum())
print(df[df.duplicated()])

df_clean = df.drop_duplicates()
df_clean = df_clean.reset_index(drop=True)

print(df_clean)
```

### 🧠 Explanation

- step 1 → duplicate count
- step 2 → inspection
- step 3 → removal
- step 4 → index reset

👉 real-world pipeline = detect → inspect → clean → reset

---

# ⚙️ Implementation Flow

1. dataset load করা হয়েছে
2. duplicate detect করা হয়েছে
3. duplicate rows inspect করা হয়েছে
4. duplicates remove করা হয়েছে
5. subset-based cleaning করা হয়েছে
6. final dataset reset করা হয়েছে

---

## 📈 Output / Result

- duplicate rows identify করা গেছে
- cleaned dataset তৈরি হয়েছে
- data consistency improve হয়েছে
- analysis-ready dataset তৈরি হয়েছে

---

## 🚀 What I Learned

- duplicate data is very common in real datasets
- cleaning without inspection risky
- subset-based logic important
- reset_index keeps dataset clean

---

## 🧠 Key Concepts (Quick Revision)

- `duplicated()` → detect duplicates
- `drop_duplicates()` → remove duplicates
- `subset` → column-based check
- `keep` → control retention
- `reset_index()` → clean indexing

---

## 📝 Notes

- duplicate remove করার আগে always inspect করা উচিত
- subset selection depends on business logic
- data loss avoid করতে careful হতে হয়

---

## 📌 Next Day Preview

👉 Day 9 — Data Types Handling

- astype()
- datetime conversion
- type optimization
- real-world data formatting

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- large dataset duplicate analysis করা
- business logic based duplicate handling

## 🧪 Practice Ideas

- different subset try করো
- keep='last' vs 'first' compare করো
