# 📅 Day 8 — Violin Plot (Plotly Express)

## 🎯 Objective

- আজকে Violin Plot ব্যবহার করে distribution shape and density visualization শেখা।
- box plot এর সাথে violin plot এর পার্থক্য বোঝা।
- group-wise score distribution compare করা।
- statistical analysis আরও গভীরভাবে দেখা।

## 📚 Topics Covered

- px.violin()
- Distribution shape
- Split violin
- Density visualization

## 📁 Project Structure

```bash
Day 8 — Violin Plot/
│── 1_basic_violin.py
│── 2_distribution_shape.py
│── 3_split_violin.py
│── 4_density_visualization.py
│── student_performance.csv
│── README.md
```

## 📊 Dataset

- **File Name:** `student_performance.csv`
- **Description:** Student performance dataset used to analyze score distribution across departments and genders.
- **Columns:**
  - `student` → student name/ID
  - `gender` → male/female category
  - `department` → CSE / EEE department
  - `score` → student score

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_violin.py`

### 🔹 Purpose

- Basic violin plot তৈরি করা
- score distribution এর overall shape দেখা

### 🧾 Code

```python id="v8c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_performance.csv")

fig = px.violin(
    df,
    y="score",
    title="Distribution of Student Scores"
)

fig.show()
```

### 🧠 Explanation

- `px.violin()` → violin plot তৈরি করে
- `y="score"` → numeric distribution দেখায়
- distribution shape বোঝা যায়
- Logic → scores কোথায় বেশি concentrated তা দেখা

---

## 📄 2. `2_distribution_shape.py`

### 🔹 Purpose

- distribution shape আরও clearly দেখা
- box plot এবং points একসাথে visualize করা

### 🧾 Code

```python id="v8c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_performance.csv")

fig = px.violin(
    df,
    y="score",
    box=True,
    points="all",
    title="Distribution Shape Visualization"
)

fig.show()
```

### 🧠 Explanation

- `box=True` → ভিতরে box plot দেখায়
- `points="all"` → সব data points দেখায়
- wide অংশ মানে বেশি data concentration
- Logic → density + summary একসাথে দেখানো

---

## 📄 3. `3_split_violin.py`

### 🔹 Purpose

- gender-based group comparison করা
- department-wise distribution compare করা

### 🧾 Code

```python id="v8c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_performance.csv")

fig = px.violin(
    df,
    x="department",
    y="score",
    color="gender",
    box=True,
    points="all",
    title="Split Violin Plot by Gender"
)

fig.update_traces(
    side="positive",
    meanline_visible=True
)

fig.show()
```

### 🧠 Explanation

- `x="department"` → department-wise comparison
- `color="gender"` → gender-based grouping
- `side="positive"` → split effect তৈরি করে
- `meanline_visible=True` → average line দেখায়
- Logic → two-group distribution comparison

---

## 📄 4. `4_density_visualization.py`

### 🔹 Purpose

- density-focused visualization করা
- styled violin plot তৈরি করা

### 🧾 Code

```python id="v8c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_performance.csv")

fig = px.violin(
    df,
    x="department",
    y="score",
    color="department",
    box=True,
    title="Density Visualization using Violin Plot"
)

fig.update_layout(
    template="plotly_dark"
)

fig.show()
```

### 🧠 Explanation

- `color="department"` → department-wise separation
- `box=True` → box summary add করে
- `template="plotly_dark"` → dark theme apply করে
- Logic → distribution shape + nice styling

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Basic violin plot তৈরি করা হয়েছে
- Distribution shape দেখা হয়েছে
- Gender-wise split comparison করা হয়েছে
- Density-focused styled chart বানানো হয়েছে

---

## 📈 Output / Result

### Key findings:

- Score distribution কোথায় বেশি concentrated তা দেখা যায়
- Department-wise variation বোঝা যায়
- Gender-based differences compare করা যায়
- Box plot এর তুলনায় shape আরও clearly বোঝা যায়

---

## 🚀 What I Learned

- Violin plot distribution shape দেখায়
- Density visualization statistical insight দেয়
- Split violin দিয়ে group comparison করা যায়
- Box plot আর violin plot একসাথে useful
- Data concentration analysis সহজ হয়

---

## 🧠 Key Concepts (Quick Revision)

- violin plot → density + distribution chart
- wide part → বেশি values
- narrow part → কম values
- split violin → group comparison
- box=True → summary inside chart

---

## 📝 Notes

- violin plot বুঝতে box plot knowledge helpful
- small dataset এ density shape limited হতে পারে
- group comparison এর জন্য category পরিষ্কার থাকতে হয়

---

## 📌 Next Day Preview

- আগামী দিনে Pie & Donut Chart শিখবো
- percentage-based visualization শুরু হবে
- labels, values, and part-to-whole analysis করা হবে

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- gender-wise violin comparison আরও extend করা
- histogram + violin combo chart বানানো
- multiple department comparison add করা

### 🧪 Practice Ideas

- gender-wise score distribution compare করো
- department-wise spread observe করো
- points remove করে cleaner violin plot দেখো
