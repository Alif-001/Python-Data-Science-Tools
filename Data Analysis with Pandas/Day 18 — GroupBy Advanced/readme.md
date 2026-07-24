# 📅 Day 18 — GroupBy Advanced (Pandas)

---

## 🎯 Objective

- Multi-level grouping (multiple columns) শেখা
- advanced aggregation techniques ব্যবহার করা
- `agg()` দিয়ে multiple statistics বের করা
- custom aggregation function তৈরি করা
- real-world business level grouping analysis করা

---

## 📚 Topics Covered

- multiple column groupby
- multi-index grouping
- agg() advanced usage
- dictionary-based aggregation
- custom aggregation function
- lambda aggregation
- real-world grouped insights

---

## 📁 Project Structure

```id="d18proj"
day-18/
│── 01_multiple_groupby.py
│── 02_multi_groupby_sum.py
│── 03_agg_multiple_stats.py
│── 04_agg_multiple_columns.py
│── 05_custom_aggregation.py
│── 06_multiple_custom_agg.py
│── 07_real_world_groupby.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee dataset used for advanced grouping analysis

- **Columns:**
  - Name → employee name
  - Department → work department
  - City → location
  - Age → age of employee
  - Salary → monthly income

👉 multi-dimensional grouping analysis করা হবে

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. `01_multiple_groupby.py`

### 🔹 Purpose

- multiple column grouping শেখা

### 🧾 Code

```python id="d18c1"
df.groupby(['Department', 'City'])['Salary'].mean()
```

### 🧠 Explanation

- Department + City → multi-level grouping
- hierarchical grouping তৈরি হয়

---

## 📄 2. `02_multi_groupby_sum.py`

### 🔹 Purpose

- multi-group sum calculation

### 🧾 Code

```python id="d18c2"
df.groupby(['Department', 'City'])['Salary'].sum()
```

### 🧠 Explanation

- group wise total salary calculation
- business level reporting

---

## 📄 3. `03_agg_multiple_stats.py`

### 🔹 Purpose

- multiple statistics একসাথে বের করা

### 🧾 Code

```python id="d18c3"
df.groupby('Department')['Salary'].agg(['mean', 'sum', 'max', 'min'])
```

### 🧠 Explanation

- এক query তে multiple metrics
- fast summary generation

---

## 📄 4. `04_agg_multiple_columns.py`

### 🔹 Purpose

- multiple columns aggregation control করা

### 🧾 Code

```python id="d18c4"
df.groupby('Department').agg({
    'Salary': ['mean', 'max'],
    'Age': ['min', 'max']
})
```

### 🧠 Explanation

- different columns → different functions
- structured analysis

---

## 📄 5. `05_custom_aggregation.py`

### 🔹 Purpose

- custom aggregation function শেখা

### 🧾 Code

```python id="d18c5"
def salary_range(x):
    return x.max() - x.min()
```

### 🧠 Explanation

- custom business logic apply করা যায়
- salary variation analysis

---

## 📄 6. `06_multiple_custom_agg.py`

### 🔹 Purpose

- built-in + custom aggregation mix

### 🧾 Code

```python id="d18c6"
lambda x: x.max() - x.min()
```

### 🧠 Explanation

- lambda দিয়ে quick custom logic
- flexible aggregation system

---

## 📄 7. `07_real_world_groupby.py`

### 🔹 Purpose

- real-world business analysis

### 🧾 Code

```python id="d18c7"
df.groupby(['Department', 'City'])['Salary'].agg(['mean', 'max', 'min'])
```

### 🧠 Explanation

- city + department wise salary analysis
- highest paying group identify করা

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- multi-column grouping করা হয়েছে
- multiple aggregation apply করা হয়েছে
- custom function ব্যবহার করা হয়েছে
- business insights extract করা হয়েছে

---

## 📈 Output / Result

- department + city wise salary analysis
- average salary report তৈরি হয়েছে
- highest paying group identify করা হয়েছে
- salary variation (range) বের করা হয়েছে

---

## 🚀 What I Learned

- multi-group analysis = deep insights
- agg() = powerful summarization tool
- custom function = business logic flexibility
- lambda = quick transformation
- multi-index = advanced pandas skill

---

## 🧠 Key Concepts (Quick Revision)

- `groupby()` → grouping data
- multi-column group → hierarchical analysis
- `agg()` → multiple statistics
- lambda → quick custom logic
- custom function → business rules

---

## 📝 Notes

- multi-group analysis = real-world data science skill
- aggregation helps decision making
- complex grouping = deeper insights

---

## 📌 Next Day Preview

👉 Day 19 — GroupBy Deep Dive

- transform vs filter
- group iteration
- advanced group operations
- real-world analytics logic

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- HR analytics dashboard
- salary comparison tool by city

### 🧪 Practice Ideas

- নিজের dataset এ multi-group analysis করো
- different aggregation experiment করো
