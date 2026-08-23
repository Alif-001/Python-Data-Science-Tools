# 📅 Day 4 — Scatter Plot (Plotly Express)

## 🎯 Objective

- আজকে Scatter Plot ব্যবহার করে দুইটা variable এর relationship বোঝা।
- Correlation (positive/negative) visualization শেখা।
- Bubble chart দিয়ে 3D-like data representation তৈরি করা।
- Advanced scatter features (color, size, symbol, hover) ব্যবহার করা।

## 📚 Topics Covered

- px.scatter()
- Correlation visualization
- Bubble chart
- color encoding
- size encoding
- symbol encoding
- hover_data

## 📁 Project Structure

```bash
Day 4 — Scatter Plot/
│── 1_basic_scatter.py
│── 2_correlation_scatter.py
│── 3_bubble_chart.py
│── 4_advanced_scatter_features.py
│── students.csv
│── README.md
```

## 📊 Dataset

- **File Name:** `students.csv`
- **Description:** Student performance dataset used to analyze relationship between study habits and marks.
- **Columns:**
  - `study_hours` → daily study time
  - `attendance` → attendance percentage
  - `marks` → exam score
  - `gender` → student gender
  - `passed` → pass/fail status

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_scatter.py`

### 🔹 Purpose

- Basic scatter plot তৈরি করা
- study_hours vs marks relationship দেখা

### 🧾 Code

```python id="d4c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("students.csv")

fig = px.scatter(
    df,
    x="study_hours",
    y="marks",
    title="Study Hours vs Marks"
)

fig.show()
```

### 🧠 Explanation

- `px.scatter()` → scatter plot তৈরি করে
- `x="study_hours"` → study time দেখায়
- `y="marks"` → exam marks দেখায়
- pattern analysis → relationship বুঝতে সাহায্য করে
- Logic → two-variable correlation visualization

---

## 📄 2. `2_correlation_scatter.py`

### 🔹 Purpose

- correlation visually analyze করা
- pass/fail grouping বোঝা

### 🧾 Code

```python id="d4c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("students.csv")

fig = px.scatter(
    df,
    x="study_hours",
    y="marks",
    color="passed",
    title="Study Hours vs Marks (Pass/Fail)"
)

fig.show()
```

### 🧠 Explanation

- `color="passed"` → category-based separation
- pass/fail group easily visible
- correlation pattern clear হয়
- Logic → classification + relationship visualization

---

## 📄 3. `3_bubble_chart.py`

### 🔹 Purpose

- 3rd dimension add করা using size
- attendance-based bubble visualization

### 🧾 Code

```python id="d4c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("students.csv")

fig = px.scatter(
    df,
    x="study_hours",
    y="marks",
    size="attendance",
    color="gender",
    title="Bubble Chart: Study vs Marks vs Attendance"
)

fig.show()
```

### 🧠 Explanation

- `size="attendance"` → bubble size represent করে attendance
- `color="gender"` → gender separation করে
- 3 variables একসাথে visualize করা যায়
- Logic → multi-dimensional data visualization

---

## 📄 4. `4_advanced_scatter_features.py`

### 🔹 Purpose

- advanced scatter features ব্যবহার করা
- hover, symbol, styling add করা

### 🧾 Code

```python id="d4c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("students.csv")

fig = px.scatter(
    df,
    x="study_hours",
    y="marks",
    color="passed",
    symbol="gender",
    size="attendance",
    hover_data=["attendance", "gender", "passed"],
    title="Advanced Scatter Plot"
)

fig.update_traces(
    marker=dict(opacity=0.8)
)

fig.update_layout(
    hovermode="closest"
)

fig.show()
```

### 🧠 Explanation

- `symbol="gender"` → different shapes for categories
- `hover_data` → extra info hover এ দেখায়
- `update_traces()` → marker style control করে
- `hovermode="closest"` → nearest point info দেখায়
- Logic → full interactive data exploration

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Basic scatter plot তৈরি করা হয়েছে
- Correlation pattern visualize করা হয়েছে
- Bubble chart দিয়ে 3D representation করা হয়েছে
- Advanced features add করে interactive analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Study hours increase করলে marks সাধারণত increase করে
- Attendance directly performance influence করে
- Gender-based difference visualization possible
- Passed students cluster pattern তৈরি করে

---

## 🚀 What I Learned

- Scatter plot is best for correlation analysis
- color = grouping variable
- size = third dimension representation
- symbol = category shape encoding
- interactive hover improves analysis depth

---

## 🧠 Key Concepts (Quick Revision)

- `px.scatter()` → relationship visualization
- correlation → variable dependency
- bubble chart → multi-variable plot
- color → category split
- size → magnitude representation
- symbol → shape encoding

---

## 📝 Notes

- Large dataset এ scatter plot heavy হতে পারে
- Too many categories দিলে visualization messy হয়
- Proper encoding selection important for clarity

---

## 📌 Next Day Preview

- আগামী দিনে Bar Chart শিখবো
- grouped, stacked, horizontal bar chart তৈরি করা হবে
- category comparison analysis শুরু হবে

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- regression trend line add করা
- interactive filter যোগ করা
- gender-wise performance dashboard বানানো

### 🧪 Practice Ideas

- study_hours vs marks নিজে analyze করো
- attendance impact check করো
- failed students pattern বের করো
