# 📅 Day 6 — Histogram (Plotly Express)

## 🎯 Objective

- আজকে Histogram ব্যবহার করে data distribution বুঝা শেখা।
- continuous numeric data কিভাবে ranges (bins) এ ভাগ করা হয় সেটা শেখা।
- frequency, spread, pattern analysis করা।
- gender-based distribution comparison শেখা।

## 📚 Topics Covered

- px.histogram()
- Distribution analysis
- nbins parameter
- Color grouping
- Density histogram

## 📁 Project Structure

```bash
Day 6 — Histogram/
│── 1_basic_histogram.py
│── 2_nbins_example.py
│── 3_color_grouping.py
│── 4_density_histogram.py
│── student_scores.csv
│── README.md
```

## 📊 Dataset

- **File Name:** `student_scores.csv`
- **Description:** Student math score dataset used to analyze score distribution and compare gender-wise performance.
- **Columns:**
  - `student` → student name/ID
  - `gender` → male/female category
  - `math_score` → exam score

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_histogram.py`

### 🔹 Purpose

- Basic histogram তৈরি করা
- math score distribution দেখা

### 🧾 Code

```python id="h6c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_scores.csv")

fig = px.histogram(
    df,
    x="math_score",
    title="Distribution of Math Scores"
)

fig.show()
```

### 🧠 Explanation

- `px.histogram()` → distribution plot তৈরি করে
- `x="math_score"` → numeric data analyze করে
- frequency distribution দেখায়
- Logic → data spread understanding

---

## 📄 2. `2_nbins_example.py`

### 🔹 Purpose

- bins control করা
- distribution detail level adjust করা

### 🧾 Code

```python id="h6c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_scores.csv")

fig = px.histogram(
    df,
    x="math_score",
    nbins=5,
    title="Histogram with 5 Bins"
)

fig.show()
```

### 🧠 Explanation

- `nbins=5` → 5 ভাগে data split করে
- কম bins → broad view
- বেশি bins → detailed view
- Logic → distribution granularity control

---

## 📄 3. `3_color_grouping.py`

### 🔹 Purpose

- gender-wise distribution compare করা
- overlapping histogram তৈরি করা

### 🧾 Code

```python id="h6c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_scores.csv")

fig = px.histogram(
    df,
    x="math_score",
    color="gender",
    barmode="overlay",
    title="Math Score Distribution by Gender"
)

fig.update_traces(opacity=0.7)

fig.show()
```

### 🧠 Explanation

- `color="gender"` → category separation করে
- `barmode="overlay"` → bars overlap করে comparison সহজ করে
- `opacity=0.7` → transparency adjust করে
- Logic → group-based distribution analysis

---

## 📄 4. `4_density_histogram.py`

### 🔹 Purpose

- probability density analysis করা
- statistical distribution বোঝা

### 🧾 Code

```python id="h6c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_scores.csv")

fig = px.histogram(
    df,
    x="math_score",
    histnorm="probability density",
    nbins=6,
    title="Density Histogram of Math Scores"
)

fig.show()
```

### 🧠 Explanation

- `histnorm="probability density"` → frequency কে probability তে convert করে
- statistical interpretation সহজ হয়
- ML/AI analysis এ useful
- Logic → probability-based distribution analysis

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Basic histogram তৈরি করা হয়েছে
- nbins দিয়ে distribution control করা হয়েছে
- gender-wise comparison করা হয়েছে
- density-based statistical histogram তৈরি করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Most students মাঝামাঝি score range এ আছে
- Gender-wise distribution প্রায় similar
- Score spread symmetric না skewed তা বোঝা যায়
- Peak range easily identify করা যায়

---

## 🚀 What I Learned

- Histogram shows data distribution, not categories
- nbins controls granularity
- color helps group comparison
- density histogram = probability view
- EDA (Exploratory Data Analysis) এর core tool histogram

---

## 🧠 Key Concepts (Quick Revision)

- histogram → distribution visualization
- bins → grouping of numeric ranges
- frequency → number of occurrences
- density → probability-based distribution
- overlay → category comparison

---

## 📝 Notes

- Too few bins → oversimplified view
- Too many bins → noisy visualization
- Histogram only works well for numeric continuous data
- Proper bin selection is important for analysis

---

## 📌 Next Day Preview

- আগামী দিনে Box Plot শিখবো
- quartiles, median, outliers বোঝা হবে
- statistical summary visualization শুরু হবে

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- KDE curve add করা
- normal distribution overlay করা
- interactive bin slider বানানো

### 🧪 Practice Ideas

- math_score distribution male vs female compare করো
- different nbins value test করো
- highest frequency range identify করো
