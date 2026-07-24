# 📅 Day 6 — Data Cleaning (Part 1)

---

## 🎯 Objective

- Missing values (NaN) বুঝা
- Missing data detect করা
- Data cleaning শুরু করা
- Real-world messy dataset handle করা শেখা

---

## 📚 Topics Covered

- Missing Values (NaN) concept
- isnull() & notnull()
- dropna() basics
- subset-based cleaning
- missing data analysis

---

## 📁 Project Structure

```id="d6proj"
day-6/
│── 01_missing_values_intro.py
│── 02_isnull_notnull.py
│── 03_dropna_basic.py
│── 04_dropna_columns.py
│── 05_missing_analysis.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset with missing values (real-world scenario)

- **Columns:**
  - Name → employee name
  - Age → age (some missing)
  - City → location (some missing)
  - Salary → salary (some missing)

👉 এই dataset intentionally messy রাখা হয়েছে real-world practice এর জন্য

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_missing_values_intro.py

### 🔹 Purpose

- Missing value (NaN) পরিচিত হওয়া

### 🧾 Code

```python id="d6c1"
import pandas as pd

df = pd.read_csv("data.csv")

print(df)

print(df.isnull())
```

### 🧠 Explanation

- `NaN` → missing data
- `isnull()` → কোথায় data missing আছে দেখায়
- True = missing, False = available

👉 missing data = real-world problem

---

## 📄 2. 02_isnull_notnull.py

### 🔹 Purpose

- missing data detect করা

### 🧾 Code

```python id="d6c2"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.isnull())
print(df.notnull())

print(df.isnull().sum())
```

### 🧠 Explanation

- `isnull()` → missing detect
- `notnull()` → data available check
- `sum()` → total missing count per column

👉 cleaning শুরু করার আগে analysis জরুরি

---

## 📄 3. 03_dropna_basic.py

### 🔹 Purpose

- missing row remove করা

### 🧾 Code

```python id="d6c3"
import pandas as pd

df = pd.read_csv("data.csv")

cleaned_df = df.dropna()

print(cleaned_df)
print(df)
```

### 🧠 Explanation

- `dropna()` → NaN থাকলে পুরো row delete করে
- original data unchanged থাকে
- cleaned version আলাদা DataFrame এ থাকে

👉 aggressive cleaning method

---

## 📄 4. 04_dropna_columns.py

### 🔹 Purpose

- specific column based cleaning

### 🧾 Code

```python id="d6c4"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.dropna(subset=['Salary']))
print(df.dropna(subset=['Age', 'City']))
```

### 🧠 Explanation

- `subset` → specific column check করে
- only সেই column এ NaN থাকলে row delete হয়
- full dataset না নষ্ট করে selective cleaning

👉 controlled cleaning approach

---

## 📄 5. 05_missing_analysis.py

### 🔹 Purpose

- missing data analysis করা

### 🧾 Code

```python id="d6c5"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.isnull().sum())

print(df.isnull().mean() * 100)

print(df.isnull().sum().sum())
```

### 🧠 Explanation

- `.sum()` → column-wise missing count
- `.mean()*100` → percentage missing
- double `.sum()` → total missing values

👉 cleaning শুরু করার আগে analysis must

---

# ⚙️ Implementation Flow

1. dataset load করা হয়েছে
2. missing values detect করা হয়েছে
3. missing data count করা হয়েছে
4. full row drop করা হয়েছে
5. column-based cleaning করা হয়েছে
6. missing analysis করা হয়েছে

---

## 📈 Output / Result

- dataset এ কোথায় missing আছে জানা গেছে
- কতটা data missing তা calculate করা হয়েছে
- cleaned dataset তৈরি করা হয়েছে
- data cleaning foundation clear হয়েছে

---

## 🚀 What I Learned

- real-world dataset messy থাকে
- NaN = missing data
- cleaning এর আগে analysis জরুরি
- dropna vs subset difference বোঝা গেছে

---

## 🧠 Key Concepts (Quick Revision)

- `NaN` → missing value
- `isnull()` → detect missing
- `notnull()` → data check
- `dropna()` → remove rows
- `subset` → column control
- `mean()` → percentage missing

---

## 📝 Notes

- dropna() use করলে data loss হতে পারে
- subset ব্যবহার করলে safer cleaning হয়
- analysis ছাড়া cleaning করা dangerous

---

## 📌 Next Day Preview

👉 Day 7 — Missing Values (Part 2)

- fillna()
- forward fill
- backward fill
- replace values
- smart data cleaning techniques

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- real Kaggle dataset দিয়ে practice করা
- missing pattern analyze করা

## 🧪 Practice Ideas

- নিজের dataset বানিয়ে missing add করে test করো
- dropna vs fillna compare করো
