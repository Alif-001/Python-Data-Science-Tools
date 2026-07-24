# 📅 Day 10 — String Operations

---

## 🎯 Objective

- Pandas এ string data clean ও transform করা শেখা
- text filtering ও searching করা শেখা
- email/text parsing করা শেখা
- real-world dirty text dataset clean করা

---

## 📚 Topics Covered

- lower() & upper() string normalization
- contains() দিয়ে text filtering
- split() দিয়ে text parsing
- replace() দিয়ে string transformation
- pandas str accessor usage

---

## 📁 Project Structure

```id="d10proj"
day-10/
│── 01_lower_upper.py
│── 02_contains_filter.py
│── 03_split_operation.py
│── 04_replace_string.py
│── 05_real_world_text_cleaning.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** User email dataset with inconsistent text formatting

- **Columns:**
  - Name → user name
  - Email → email address (mixed case, dirty format)
  - City → user location

👉 email data intentionally messy (real-world scenario)

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_lower_upper.py

### 🔹 Purpose

- text normalization (case standardization)

### 🧾 Code

```python id="d10c1"
import pandas as pd

df = pd.read_csv("data.csv")

df['Email_lower'] = df['Email'].str.lower()
df['Email_upper'] = df['Email'].str.upper()

print(df)
```

### 🧠 Explanation

- `str.lower()` → সব text ছোট হাতের করে
- `str.upper()` → সব text বড় হাতের করে
- data standardization এর জন্য গুরুত্বপূর্ণ

👉 cleaning starts with normalization

---

## 📄 2. 02_contains_filter.py

### 🔹 Purpose

- text-based filtering করা

### 🧾 Code

```python id="d10c2"
import pandas as pd

df = pd.read_csv("data.csv")

gmail_users = df[df['Email'].str.contains("gmail")]

print(gmail_users)
```

### 🧠 Explanation

- `contains()` → string search tool
- Gmail users filter করা হয়েছে
- real-world: log filtering, user segmentation

👉 text search = powerful filtering tool

---

## 📄 3. 03_split_operation.py

### 🔹 Purpose

- text parsing করা

### 🧾 Code

```python id="d10c3"
import pandas as pd

df = pd.read_csv("data.csv")

df[['Username', 'Domain']] = df['Email'].str.split('@', expand=True)

print(df)
```

### 🧠 Explanation

- `split('@')` → email break করে দুই ভাগে
- username + domain আলাদা হয়
- `expand=True` → column-wise split

👉 data extraction technique

---

## 📄 4. 04_replace_string.py

### 🔹 Purpose

- string transformation

### 🧾 Code

```python id="d10c4"
import pandas as pd

df = pd.read_csv("data.csv")

df['Email'] = df['Email'].str.replace("gmail.com", "gmail.org")
df['City'] = df['City'].str.replace("Dhaka", "DHAKA")

print(df)
```

### 🧠 Explanation

- `replace()` → exact string change
- domain/format update করা যায়
- data standardization এর অংশ

👉 transformation tool

---

## 📄 5. 05_real_world_text_cleaning.py

### 🔹 Purpose

- full text cleaning pipeline

### 🧾 Code

```python id="d10c5"
import pandas as pd

df = pd.read_csv("data.csv")

df['Email'] = df['Email'].str.lower()
df['Email'] = df['Email'].str.strip()

gmail_users = df[df['Email'].str.contains("gmail")]

df[['Username', 'Domain']] = df['Email'].str.split('@', expand=True)

print(df)
print(gmail_users)
```

### 🧠 Explanation

- step 1 → lowercase normalization
- step 2 → whitespace cleaning
- step 3 → filtering
- step 4 → parsing

👉 complete text processing pipeline

---

# ⚙️ Implementation Flow

1. dataset load করা হয়েছে
2. text normalize করা হয়েছে
3. filtering applied করা হয়েছে
4. string split করা হয়েছে
5. final structured dataset তৈরি হয়েছে

---

## 📈 Output / Result

- inconsistent email data cleaned
- structured username + domain তৈরি হয়েছে
- filtered Gmail users পাওয়া গেছে
- analysis-ready text dataset তৈরি হয়েছে

---

## 🚀 What I Learned

- string cleaning = very important in real data
- pandas `str` accessor is powerful
- text parsing helps feature engineering
- normalization improves consistency

---

## 🧠 Key Concepts (Quick Revision)

- `str.lower()` → lowercase conversion
- `str.upper()` → uppercase conversion
- `str.contains()` → text search
- `str.split()` → text splitting
- `str.replace()` → text transformation

---

## 📝 Notes

- case mismatch can break analysis
- always normalize before filtering
- text cleaning = ML feature engineering step

---

## 📌 Next Day Preview

👉 Day 11 — Basic Statistics

- mean, median, mode
- min, max, sum
- std deviation
- data insights extraction

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- email validation system বানানো
- domain-wise user analysis করা

## 🧪 Practice Ideas

- নিজের dataset এ `.contains()` use করে filtering practice করো
- username extraction try করো
