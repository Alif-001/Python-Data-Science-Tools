# 📅 Day 5 — Filtering (Important)

---

## 🎯 Objective

- Condition অনুযায়ী data filter করা শেখা
- Single ও multiple condition ব্যবহার করা
- AND / OR logic বোঝা
- `query()` method ব্যবহার করে clean filtering করা
- real-world data selection practice করা

---

## 📚 Topics Covered

- Single Condition Filtering
- Multiple Conditions (AND, OR)
- query() Method
- Practical Filtering Examples

---

## 📁 Project Structure

```id="f5proj"
day-5/
│── 01_single_condition_filter.py
│── 02_multiple_conditions_and.py
│── 03_multiple_conditions_or.py
│── 04_query_method.py
│── 05_practice_filters.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset for filtering practice

- **Columns:**
  - Name → employee name
  - Age → age of employee
  - City → location
  - Salary → monthly income

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. 01_single_condition_filter.py

### 🔹 Purpose

- একটি condition ব্যবহার করে data filter করা

### 🧾 Code

```python id="f5c1"
import pandas as pd

df = pd.read_csv("data.csv")

filtered = df[df['Age'] > 25]
print(filtered)

print(df[df['Salary'] > 30000])
```

### 🧠 Explanation

- `df['Age'] > 25` → True/False তৈরি করে
- True rows only return করে
- filtering = condition-based selection

👉 Single condition = basic filtering logic

---

## 📄 2. 02_multiple_conditions_and.py

### 🔹 Purpose

- AND condition ব্যবহার করা

### 🧾 Code

```python id="f5c2"
import pandas as pd

df = pd.read_csv("data.csv")

filtered = df[(df['Age'] > 25) & (df['Salary'] > 30000)]
print(filtered)

print(df[(df['City'] == 'Dhaka') & (df['Age'] > 20)])
```

### 🧠 Explanation

- `&` → AND condition
- প্রতিটি condition অবশ্যই () এর ভিতরে রাখতে হয়
- দুইটা condition true হলে তবেই row থাকবে

👉 AND = strict filtering

---

## 📄 3. 03_multiple_conditions_or.py

### 🔹 Purpose

- OR condition ব্যবহার করা

### 🧾 Code

```python id="f5c3"
import pandas as pd

df = pd.read_csv("data.csv")

filtered = df[(df['Age'] > 28) | (df['Salary'] > 40000)]
print(filtered)

print(df[(df['City'] == 'Dhaka') | (df['City'] == 'Sylhet')])
```

### 🧠 Explanation

- `|` → OR condition
- যেকোনো একটা condition true হলেই row থাকবে

👉 OR = flexible filtering

---

## 📄 4. 04_query_method.py

### 🔹 Purpose

- clean syntax ব্যবহার করে filtering

### 🧾 Code

```python id="f5c4"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.query("Age > 25"))
print(df.query("Salary > 30000"))

print(df.query("Age > 25 and Salary > 30000"))

print(df.query("City == 'Dhaka' or City == 'Sylhet'"))
```

### 🧠 Explanation

- `query()` → readable filtering syntax
- AND → `and`
- OR → `or`
- complex condition সহজে লেখা যায়

👉 query() = clean & production-friendly

---

## 📄 5. 05_practice_filters.py

### 🔹 Purpose

- real-world filtering practice

### 🧾 Code

```python id="f5c5"
import pandas as pd

df = pd.read_csv("data.csv")

print(df[df['City'] == 'Dhaka'])

print(df[df['Age'] < 25])

print(df[(df['Salary'] >= 25000) & (df['Salary'] <= 40000)])

print(df[df['Salary'] > 35000])

print(df[(df['City'] == 'Dhaka') | (df['City'] == 'Khulna')])
```

### 🧠 Explanation

- real dataset filtering practice
- range filtering (>= and <=)
- multiple city selection
- high salary filter

👉 real-world analysis starts from filtering

---

# ⚙️ Implementation Flow

1. dataset load করা হয়েছে
2. single condition filtering করা হয়েছে
3. AND condition applied করা হয়েছে
4. OR condition ব্যবহার করা হয়েছে
5. query() method practice করা হয়েছে
6. real-world filtering examples করা হয়েছে

---

## 📈 Output / Result

- filtered datasets successfully তৈরি হয়েছে
- condition-based selection clear হয়েছে
- query() syntax practice হয়েছে
- real-world analysis logic শুরু হয়েছে

---

## 🚀 What I Learned

- filtering = data analysis এর core skill
- AND / OR logic properly apply করতে হয়
- query() makes code cleaner
- correct condition না দিলে wrong data আসতে পারে

---

## 🧠 Key Concepts (Quick Revision)

- `df[condition]` → filtering
- `&` → AND
- `|` → OR
- `query()` → readable filtering
- parentheses () are mandatory

---

## 📝 Notes

- multiple condition এ bracket ভুল হলে error আসে
- query() production code এ খুব useful
- filtering = data science foundation

---

## 📌 Next Day Preview

👉 Day 6 — Missing Values (NaN Handling)

- isnull / notnull
- dropna
- fillna
- data cleaning basics

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- real dataset (Kaggle) দিয়ে filtering practice
- complex condition combine করা

## 🧪 Practice Ideas

- নিজের dataset এ salary range filter করো
- city + age combined filtering try করো
