# 📅 Day 29 — MultiIndex

---

## 🎯 Objective

- Pandas এ MultiIndex (hierarchical index) বুঝা
- multiple column কে index হিসেবে ব্যবহার করা
- tree-like data structure handle করা
- multi-level filtering ও selection করা
- real-world enterprise-level grouping analysis করা

---

## 📚 Topics Covered

- `set_index()` with multiple columns
- MultiIndex structure
- `.loc[]` multi-level selection
- tuple-based indexing
- `groupby()` with multiple keys
- `unstack()` (hierarchical → table format)
- hierarchical aggregation

---

## 📁 Project Structure

```id="d29proj"
day-29/
│── 01_set_multiindex.py
│── 02_select_country.py
│── 03_select_city.py
│── 04_specific_department.py
│── 05_multiindex_groupby.py
│── 06_unstack_multiindex.py
│── 07_real_world_multiindex.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

### 📄 File Name: data.csv

- **Description:** Hierarchical employee salary dataset

- **Columns:**
  - Country → country name
  - City → city name
  - Department → department name
  - Salary → employee salary

👉 এটি একটি **multi-level structured dataset (hierarchy-based)**

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry File)

### 🔹 Purpose

- MultiIndex learning module start করা

### 🧾 Code

```python id="mi29main"
print("Day 29 - MultiIndex Learning")
```

### 🧠 Explanation

- simple entry file
- concept initialization

---

## 📄 2. 01_set_multiindex.py

### 🔹 Purpose

- multiple column কে index বানানো

### 🧾 Code

```python id="mi29a"
df = df.set_index(['Country', 'City', 'Department'])
```

### 🧠 Explanation

- hierarchical structure তৈরি হয়
- tree-like data structure (parent → child → sub-child)

---

## 📄 3. 02_select_country.py

### 🔹 Purpose

- top-level index filter করা

### 🧾 Code

```python id="mi29b"
df.loc['Bangladesh']
```

### 🧠 Explanation

- country level data extract করে
- all cities + departments show করে

---

## 📄 4. 03_select_city.py

### 🔹 Purpose

- multi-level partial selection

### 🧾 Code

```python id="mi29c"
df.loc[('India', 'Mumbai')]
```

### 🧠 Explanation

- tuple-based indexing ব্যবহার হয়
- specific city data পাওয়া যায়

---

## 📄 5. 04_specific_department.py

### 🔹 Purpose

- exact row access করা

### 🧾 Code

```python id="mi29d"
df.loc[('Bangladesh', 'Dhaka', 'IT')]
```

### 🧠 Explanation

- full hierarchy specify করা হয়
- exact record return করে

---

## 📄 6. 05_multiindex_groupby.py

### 🔹 Purpose

- hierarchical grouping analysis

### 🧾 Code

```python id="mi29e"
grouped = df.groupby(['Country', 'City'])['Salary'].mean()
```

### 🧠 Explanation

- multi-level grouping তৈরি হয়
- automatic MultiIndex structure তৈরি হয়

---

## 📄 7. 06_unstack_multiindex.py

### 🔹 Purpose

- hierarchical data কে table format এ convert করা

### 🧾 Code

```python id="mi29f"
unstacked = grouped.unstack()
```

### 🧠 Explanation

- row → column conversion
- pivot table style output

---

## 📄 8. 07_real_world_multiindex.py

### 🔹 Purpose

- enterprise-level salary analysis

### 🧾 Code

```python id="mi29g"
grouped = df.groupby(['Country', 'City'])['Salary'].agg(['mean', 'max'])
table = grouped.unstack()
```

### 🧠 Explanation

- multi-metric analysis (mean + max)
- hierarchical → business dashboard format
- highest salary group identify করা হয়

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- multiple column index তৈরি করা হয়েছে
- hierarchical filtering applied করা হয়েছে
- groupby analysis করা হয়েছে
- unstack দিয়ে table format তৈরি করা হয়েছে
- insights extract করা হয়েছে

---

## 📈 Output / Result

- country → city → department hierarchy তৈরি হয়েছে
- salary distribution analysis হয়েছে
- multi-level filtering কাজ করেছে
- business-style summary report তৈরি হয়েছে

---

## 🚀 What I Learned

- MultiIndex = hierarchical data structure
- multiple columns = structured tree format
- `.loc[]` supports tuple indexing
- groupby + MultiIndex = powerful analytics tool
- unstack = reporting format converter

---

## 🧠 Key Concepts (Quick Revision)

- `set_index([...])` → MultiIndex create
- `.loc['Country']` → top-level access
- `.loc[(a,b,c)]` → deep access
- `groupby([...])` → hierarchical grouping
- `unstack()` → pivot table view

---

## 📝 Notes

- MultiIndex = complex but powerful
- used in enterprise dashboards
- proper hierarchy understanding important
- tuple indexing must follow order

---

## 📌 Next Day Preview

👉 Day 30 — Performance Optimization

- vectorization
- apply vs direct operations
- memory optimization
- pandas performance tuning
- fast data processing techniques

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- country-wise salary dashboard
- global HR analytics system

### 🧪 Practice Ideas

- add more hierarchy levels (state, company branch)
- try different aggregation functions
- convert MultiIndex → CSV export practice
