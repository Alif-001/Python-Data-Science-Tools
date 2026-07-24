# 📅 Day 12 — Sorting & Ranking (Pandas)

---

## 🎯 Objective

- Pandas দিয়ে data sorting শেখা
- ascending / descending order বুঝা
- multiple column sorting practice করা
- ranking system তৈরি করা
- real-world analysis (top performer, ranking) বুঝা

---

## 📚 Topics Covered

- sort_values()
- sort_index()
- ascending & descending sorting
- multiple column sorting
- rank() function
- ranking methods (average, min, max, first)
- real-world ranking system

---

## 📁 Project Structure

```
day-12/
│── 01_sort_values_basic.py
│── 02_sort_multiple_columns.py
│── 03_sort_index.py
│── 04_ranking_basic.py
│── 05_rank_methods.py
│── 06_real_world_sort_rank.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `data.csv`

- **Description:** Employee/student dataset used for sorting & ranking analysis

- **Columns:**
  - Name → person name
  - Age → age
  - Salary → monthly income
  - Marks → performance score

👉 dataset unsorted অবস্থায় থাকে, পরে sorting করা হয়

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. `01_sort_values_basic.py`

### 🔹 Purpose

- single column দিয়ে sorting শেখা

### 🧾 Code

```python
df.sort_values(by='Salary')
df.sort_values(by='Salary', ascending=False)
```

### 🧠 Explanation

- `sort_values()` → column based sorting
- `ascending=False` → highest value first

---

## 📄 2. `02_sort_multiple_columns.py`

### 🔹 Purpose

- multiple column sorting শেখা

### 🧾 Code

```python
df.sort_values(by=['Age', 'Salary'])
df.sort_values(by=['Age', 'Salary'], ascending=[True, False])
```

### 🧠 Explanation

- প্রথমে Age অনুযায়ী sort
- একই Age হলে Salary অনুযায়ী sort
- priority-based sorting হয়

---

## 📄 3. `03_sort_index.py`

### 🔹 Purpose

- index based sorting বোঝা

### 🧾 Code

```python
df.sample(frac=1).sort_index()
```

### 🧠 Explanation

- data shuffle করা হয়
- তারপর index অনুযায়ী আবার সাজানো হয়

---

## 📄 4. `04_ranking_basic.py`

### 🔹 Purpose

- ranking system তৈরি করা

### 🧾 Code

```python
df['Salary_Rank'] = df['Salary'].rank()
df['Salary_Rank_Desc'] = df['Salary'].rank(ascending=False)
```

### 🧠 Explanation

- rank() → position assign করে
- highest value = rank 1 (descending হলে)

---

## 📄 5. `05_rank_methods.py`

### 🔹 Purpose

- tie handling শেখা

### 🧾 Code

```python
df['Marks'].rank(method='average')
df['Marks'].rank(method='min')
df['Marks'].rank(method='max')
df['Marks'].rank(method='first')
```

### 🧠 Explanation

- duplicate values হলে ranking কিভাবে হবে তা control করা যায়

---

## 📄 6. `06_real_world_sort_rank.py`

### 🔹 Purpose

- real-world analysis (top performer)

### 🧾 Code

```python
df.sort_values(by='Salary', ascending=False)
df.sort_values(by='Marks', ascending=False)
df['Marks_Rank'] = df['Marks'].rank(ascending=False)
df.loc[df['Marks'].idxmax()]
```

### 🧠 Explanation

- top salary holder বের করা
- top student বের করা
- best performer identify করা

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- sorting applied করা হয়েছে
- multiple column sorting করা হয়েছে
- ranking system তৈরি করা হয়েছে
- top performer analysis করা হয়েছে

---

## 📈 Output / Result

- sorted salary list পাওয়া গেছে
- top students identify করা গেছে
- ranking system তৈরি হয়েছে
- best performer বের করা গেছে

---

## 🚀 What I Learned

- sorting = data ordering technique
- ranking = performance position system
- multiple column sorting powerful analysis tool
- real-world insights সহজে বের করা যায়

---

## 🧠 Key Concepts (Quick Revision)

- `sort_values()` → column sort
- `sort_index()` → index sort
- `ascending=False` → descending order
- `rank()` → position assign
- ranking methods → tie handling

---

## 📝 Notes

- sorting = data analysis foundation
- ranking = decision making system
- ties properly handle করা খুব important

---

## 📌 Next Day Preview

👉 Day 13 — Apply Function & Lambda

- apply()
- lambda function
- row-wise / column-wise transformation
- feature engineering start

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- salary leaderboard system
- student ranking dashboard

### 🧪 Practice Ideas

- নিজের dataset sort করে try করো
- top 5 performers বের করো
