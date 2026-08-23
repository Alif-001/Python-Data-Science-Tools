# 📅 Day 11 — Scatter Matrix (`px.scatter_matrix()`)

---

## 🎯 Objective

- আজকে আমরা শিখবো কীভাবে একসাথে multiple variables analyze করা যায়
- Scatter Matrix ব্যবহার করে:
  - variable গুলোর মধ্যে relationship দেখা
  - correlation explore করা
  - multidimensional data visualize করা

- Data Science / Machine Learning exploration mindset তৈরি করা

---

## 📚 Topics Covered

- `px.scatter_matrix()`
- Multivariable analysis
- Correlation exploration
- Dimension visualization
- Color encoding in scatter matrix
- Feature relationship understanding

---

## 📁 Project Structure

```text
Day 11 — Scatter Matrix/
│
├── 1_basic_scatter_matrix.py
├── 2_multivariable_analysis.py
├── 3_correlation_exploration.py
└── student_data.csv
```

---

## 📊 Dataset

**File Name:** `student_data.csv`

**Description:**
Students performance dataset used for multivariable analysis and correlation exploration.

**Columns:**

- study_hours → প্রতিদিন কত ঘণ্টা পড়াশোনা করে
- sleep_hours → প্রতিদিন কত ঘণ্টা ঘুমায়
- attendance → class attendance percentage
- marks → exam marks
- iq → intelligence score (synthetic feature)

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_scatter_matrix.py`

### 🔹 Purpose

- Basic scatter matrix তৈরি করা
- সব numerical variables এর relationship visualize করা

### 🧾 Code

```python
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

fig = px.scatter_matrix(
    df,
    dimensions=["study_hours", "sleep_hours", "attendance", "marks", "iq"],
    title="Scatter Matrix - Basic View"
)

fig.show()
```

---

### 🧠 Explanation

- `pd.read_csv()` → dataset load করে
- `px.scatter_matrix()` → সব variables pairwise compare করে
- `dimensions=[]` → কোন columns গুলো দেখাবো সেটা define করে
- `fig.show()` → interactive plot display করে

👉 Logic:

- প্রতিটি variable অন্য সব variable এর সাথে compare হয়
- diagonal এ distribution দেখা যায়

---

## 📄 2. `2_multivariable_analysis.py`

### 🔹 Purpose

- Multiple variables analyze করা
- `color` ব্যবহার করে extra dimension add করা

### 🧾 Code

```python
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

fig = px.scatter_matrix(
    df,
    dimensions=["study_hours", "sleep_hours", "attendance", "marks"],
    color="iq",
    title="Multivariable Analysis with Color Encoding"
)

fig.show()
```

---

### 🧠 Explanation

- `color="iq"` → IQ অনুযায়ী points group হয়
- একই graph এ extra dimension add হয়
- pattern বুঝতে সহজ হয়

👉 Logic:

- high IQ students কোথায় cluster করছে দেখা যায়
- variables এর hidden relationship বের হয়

---

## 📄 3. `3_correlation_exploration.py`

### 🔹 Purpose

- Correlation visually analyze করা
- Marks এর সাথে relationship explore করা

### 🧾 Code

```python
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

fig = px.scatter_matrix(
    df,
    dimensions=["study_hours", "sleep_hours", "attendance", "marks"],
    color="marks",
    title="Correlation Exploration using Scatter Matrix"
)

fig.update_traces(diagonal_visible=False)

fig.show()
```

---

### 🧠 Explanation

- `color="marks"` → marks অনুযায়ী variation দেখা যায়
- `update_traces()` → diagonal remove করা হয়েছে clarity এর জন্য
- relationship pattern easier to read হয়

👉 Logic:

- study_hours ↑ → marks ↑ কিনা দেখা যায়
- sleep_hours impact observe করা যায়

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Numerical columns select করা হয়েছে
- Scatter matrix তৈরি করা হয়েছে
- Color encoding add করা হয়েছে
- Correlation visually analyze করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- study_hours increase করলে marks সাধারণত increase করে
- attendance এবং marks এর মধ্যে positive relationship আছে
- sleep_hours মাঝামাঝি level এ optimal effect দেখায়
- IQ অনুযায়ী data clustering দেখা যায়

---

## 🚀 What I Learned

- Multivariable data একসাথে visualize করা যায়
- Correlation শুধু numbers না, visualization দিয়েও বোঝা যায়
- Feature relationship understanding ML এর জন্য খুব important
- Scatter matrix exploratory data analysis (EDA) এর powerful tool

---

## 🧠 Key Concepts (Quick Revision)

- Scatter matrix = pairwise comparison of all variables
- Color = extra dimension add করে
- Correlation = relationship between variables
- EDA = data understand করার first step

---

## 📝 Notes

- অনেক variables হলে plot heavy হতে পারে
- irrelevant columns বাদ দেওয়া better
- large dataset এ performance slow হতে পারে
- clean data হলে visualization clearer হয়

---

## 📌 Next Day Preview

আগামী দিনে আমরা শিখবো:

- 📊 Density Heatmap (`px.density_heatmap()`)
- correlation density visualization
- heatmap-based pattern detection
- advanced color scaling

---

## ⭐ Bonus

### 🔥 Improvement Ideas

- real student dataset use করা
- more features add করা (study_time, stress_level)
- interactive filters add করা

---

### 🧪 Practice Ideas

- dataset এ নতুন column add করো
- different color variables try করো (`study_hours`, `attendance`)
- marks prediction intuition তৈরি করো
- কোন variable সবচেয়ে important সেটা identify করো
