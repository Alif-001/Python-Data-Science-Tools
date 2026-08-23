# 📅 Day 7 — Box Plot (Plotly Express)

## 🎯 Objective

- আজকে Box Plot ব্যবহার করে statistical distribution analysis শেখা।
- median, quartiles, spread এবং outliers বোঝা।
- group-wise comparison করা শেখা।
- real-world data analysis workflow build করা।

## 📚 Topics Covered

- px.box()
- Quartiles (Q1, Q2, Q3)
- Outlier detection
- Group comparison
- Distribution comparison

## 📁 Project Structure

```bash
Day 7 — Box Plot/
│── 1_basic_boxplot.py
│── 2_quartiles_explained.py
│── 3_outlier_detection.py
│── 4_group_comparison.py
│── exam_scores.csv
│── README.md
```

## 📊 Dataset

- **File Name:** `exam_scores.csv`
- **Description:** Student exam score dataset used for statistical analysis and distribution comparison.
- **Columns:**
  - `student` → student ID/name
  - `gender` → male/female category
  - `department` → CSE / EEE department
  - `score` → exam score

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_boxplot.py`

### 🔹 Purpose

- Basic box plot তৈরি করা
- score distribution বোঝা

### 🧾 Code

```python id="bx7c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("exam_scores.csv")

fig = px.box(
    df,
    y="score",
    title="Distribution of Exam Scores"
)

fig.show()
```

### 🧠 Explanation

- `px.box()` → box plot তৈরি করে
- `y="score"` → numeric distribution দেখায়
- median, quartiles automatically calculate হয়
- Logic → statistical summary visualization

---

## 📄 2. `2_quartiles_explained.py`

### 🔹 Purpose

- quartiles visualization বোঝা
- raw data points দেখানো

### 🧾 Code

```python id="bx7c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("exam_scores.csv")

fig = px.box(
    df,
    y="score",
    points="all",
    title="Quartiles Visualization"
)

fig.show()
```

### 🧠 Explanation

- `points="all"` → সব data points দেখায়
- Q1, Q2 (median), Q3 visualization clear হয়
- box edges = quartile range
- Logic → distribution breakdown understanding

---

## 📄 3. `3_outlier_detection.py`

### 🔹 Purpose

- outliers detect করা
- abnormal values identify করা

### 🧾 Code

```python id="bx7c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("exam_scores.csv")

fig = px.box(
    df,
    y="score",
    points="outliers",
    title="Outlier Detection using Box Plot"
)

fig.show()
```

### 🧠 Explanation

- `points="outliers"` → শুধু outlier দেখায়
- extreme values highlight করে
- anomaly detection সহজ হয়
- Logic → unusual data detection

---

## 📄 4. `4_group_comparison.py`

### 🔹 Purpose

- department-wise comparison করা
- group distribution analyze করা

### 🧾 Code

```python id="bx7c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("exam_scores.csv")

fig = px.box(
    df,
    x="department",
    y="score",
    color="department",
    points="all",
    title="Department-wise Score Comparison"
)

fig.show()
```

### 🧠 Explanation

- `x="department"` → group-wise box plot তৈরি করে
- CSE vs EEE comparison করা যায়
- `color` → visual separation দেয়
- Logic → group distribution comparison

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- basic distribution analysis করা হয়েছে
- quartiles visualized করা হয়েছে
- outlier detection করা হয়েছে
- group-wise comparison করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- most scores মাঝামাঝি range এ clustered
- few high scores outlier হিসেবে দেখা যায়
- department-wise performance difference বোঝা যায়
- median performance easily compare করা যায়

---

## 🚀 What I Learned

- box plot shows statistical summary
- quartiles divide data into 4 parts
- outliers are extreme unusual values
- group comparison helps decision making
- distribution analysis is core EDA skill

---

## 🧠 Key Concepts (Quick Revision)

- box plot → statistical summary chart
- Q1 → 25% data point
- Q2 → median (50%)
- Q3 → 75%
- IQR → middle spread
- outlier → extreme value

---

## 📝 Notes

- small dataset এ box plot limited insight দিতে পারে
- outliers always mean error না (context important)
- grouped box plot is powerful for comparison

---

## 📌 Next Day Preview

- আগামী দিনে Violin Plot শিখবো
- distribution shape deeper ভাবে বুঝা হবে
- density + box plot combination analysis করা হবে

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- gender-wise box plot add করা
- interactive filtering system বানানো
- combined histogram + box plot visualization

### 🧪 Practice Ideas

- highest score outlier identify করো
- department performance compare করো
- remove outliers and re-analyze data
