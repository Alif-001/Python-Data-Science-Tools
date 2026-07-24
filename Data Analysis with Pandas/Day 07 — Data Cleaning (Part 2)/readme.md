# 📅 Day 7 — Data Cleaning (Part 2)

---

## 🎯 Objective

- Missing values (NaN) handle করে data clean করা শেখা
- `fillna()` ব্যবহার করে smart imputation করা
- forward fill ও backward fill বোঝা
- `replace()` দিয়ে value transformation করা
- real-world cleaning strategy develop করা

---

## 📚 Topics Covered

- fillna() basic usage
- column-specific missing value handling
- forward fill (ffill)
- backward fill (bfill)
- replace() method
- real-world cleaning strategy

---

## 📁 Project Structure

```id="d7proj"
day-7/
│── 01_fillna_basic.py
│── 02_fillna_column_specific.py
│── 03_forward_backward_fill.py
│── 04_replace_values.py
│── 05_cleaning_strategy.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset with missing values (real-world messy data)

- **Columns:**
  - Name → employee name
  - Age → age (some missing)
  - City → location (some missing)
  - Salary → income (some missing)

👉 এই dataset intentionally messy রাখা হয়েছে cleaning practice এর জন্য

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_fillna_basic.py

### 🔹 Purpose

- missing values replace করা (basic fill)

### 🧾 Code

```python id="d7c1"
import pandas as pd

df = pd.read_csv("data.csv")

filled_df = df.fillna(0)

print(filled_df)
```

### 🧠 Explanation

- `fillna(0)` → সব NaN কে 0 দিয়ে replace করে
- missing data complete করে analysis ready বানায়

👉 simplest cleaning technique

---

## 📄 2. 02_fillna_column_specific.py

### 🔹 Purpose

- column অনুযায়ী smart filling

### 🧾 Code

```python id="d7c2"
import pandas as pd

df = pd.read_csv("data.csv")

df_filled = df.fillna({
    'Age': df['Age'].mean(),
    'City': 'Unknown',
    'Salary': df['Salary'].median()
})

print(df_filled)
```

### 🧠 Explanation

- numeric column → mean/median
- categorical column → fixed value
- real-world cleaning এ এই method বেশি ব্যবহার হয়

👉 smart imputation strategy

---

## 📄 3. 03_forward_backward_fill.py

### 🔹 Purpose

- sequential filling শেখা

### 🧾 Code

```python id="d7c3"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.fillna(method='ffill'))
print(df.fillna(method='bfill'))
```

### 🧠 Explanation

- `ffill` → previous row value copy করে
- `bfill` → next row value copy করে
- time-series data তে খুব useful

👉 pattern-based filling

---

## 📄 4. 04_replace_values.py

### 🔹 Purpose

- exact value replace করা

### 🧾 Code

```python id="d7c4"
import pandas as pd

df = pd.read_csv("data.csv")

df_replaced = df.replace("Dhaka", "DHAKA")
print(df_replaced)

df_replaced2 = df.replace({
    "Sylhet": "SYL",
    "Khulna": "KHU"
})

print(df_replaced2)

df_replaced3 = df.replace(25000, 99999)
print(df_replaced3)
```

### 🧠 Explanation

- `replace()` → exact value change
- string বা numeric দুইটাই replace করা যায়
- multiple mapping support করে

👉 data transformation tool

---

## 📄 5. 05_cleaning_strategy.py

### 🔹 Purpose

- real-world cleaning pipeline

### 🧾 Code

```python id="d7c5"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['City'] = df['City'].fillna("Unknown")
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print(df)
```

### 🧠 Explanation

- step 1 → missing analysis
- step 2 → numeric fill (mean/median)
- step 3 → categorical fill (Unknown)
- final → clean dataset

👉 real-world cleaning pipeline

---

# ⚙️ Implementation Flow

1. dataset load করা হয়েছে
2. missing values detect করা হয়েছে
3. simple fillna() ব্যবহার করা হয়েছে
4. column-wise smart filling করা হয়েছে
5. forward/backward fill practice করা হয়েছে
6. replace() দিয়ে data transform করা হয়েছে
7. full cleaning pipeline তৈরি করা হয়েছে

---

## 📈 Output / Result

- messy dataset clean করা হয়েছে
- missing values handle করা হয়েছে
- data analysis-ready dataset তৈরি হয়েছে
- multiple cleaning strategy practice হয়েছে

---

## 🚀 What I Learned

- data cleaning = most important step in pandas
- mean/median fill = smart approach
- ffill/bfill = sequential data cleaning
- replace() = data transformation tool

---

## 🧠 Key Concepts (Quick Revision)

- `fillna()` → missing value replace
- `mean()` → average fill
- `median()` → robust fill
- `ffill` → previous value
- `bfill` → next value
- `replace()` → exact value change

---

## 📝 Notes

- wrong filling করলে analysis biased হতে পারে
- numeric vs categorical আলাদা logic দরকার
- cleaning = thinking + logic combination

---

## 📌 Next Day Preview

👉 Day 8 — Duplicate Handling

- duplicated()
- drop_duplicates()
- real-world duplicate detection

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- Kaggle dataset দিয়ে cleaning practice
- missing pattern analysis করা

## 🧪 Practice Ideas

- নিজের dataset বানিয়ে missing add করে clean করো
- fillna vs replace compare করো
