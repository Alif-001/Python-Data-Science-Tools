# 📅 Day 21 — 3D Scatter Plot

---

## 🎯 Objective

- আজকে শিখার লক্ষ্য হলো 3D data visualization বোঝা
- একসাথে 3টি numerical variable analyze করা
- multi-dimensional relationship visually explore করা
- real dataset থেকে student performance pattern বের করা

---

## 📚 Topics Covered

- px.scatter_3d()
- 3D coordinate system (x, y, z)
- multi-variable analysis
- color & size dimension
- camera control in 3D plot

---

## 📁 Project Structure

```text
Day 21 — 3D Scatter Plot/
│── main.py
│── analysis.py
│── utils.py
│── student_performance.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** student_performance.csv
- **Description:** Students performance dataset used for 3D visualization of study behavior and marks relationship

### Columns:

- student → student name / ID
- study_hours → daily study time
- sleep_hours → daily sleep time
- marks → exam score
- attendance → class attendance percentage

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py

### 🔹 Purpose

- মূল 3D scatter plot তৈরি করা
- study_hours, sleep_hours, marks একসাথে visualize করা

### 🧾 Code

```python
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_performance.csv")

fig = px.scatter_3d(
    df,
    x="study_hours",
    y="sleep_hours",
    z="marks",
    title="3D Student Performance Visualization"
)

fig.show()
```

### 🧠 Explanation

- Line 1 → pandas import করা হচ্ছে data handle করার জন্য
- Line 2 → plotly express import করা হচ্ছে visualization এর জন্য
- Line 4 → CSV file load করা হচ্ছে
- Line 6-12 → 3D scatter plot তৈরি করা হচ্ছে
- Logic → 3 variable একসাথে 3D space এ plot করা হচ্ছে

---

## 📄 2. analysis.py

### 🔹 Purpose

- multi-dimensional relationship analysis করা
- marks, attendance, study pattern explore করা

### 🧾 Code

```python
import pandas as pd

df = pd.read_csv("student_performance.csv")

print(df.describe())
print(df.corr())
```

### 🧠 Explanation

- describe() → dataset summary (mean, min, max)
- corr() → variable relationship check করে
- Logic → কোন factor marks এর সাথে strong relation রাখে তা বোঝা

---

## 📄 3. utils.py (if any)

### 🔹 Purpose

- helper functions for data preprocessing

### 🧾 Code

```python
def normalize(column):
    return (column - column.min()) / (column.max() - column.min())
```

### 🧠 Explanation

- normalization → data scale 0–1 এর মধ্যে আনা
- reusable function → multiple column এ apply করা যায়

---

## ⚙️ Implementation Flow

- Data load করা হয়েছে
- Basic exploration করা হয়েছে
- 3D visualization তৈরি করা হয়েছে
- correlation analysis করা হয়েছে
- multi-variable relationship study করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- study_hours বাড়লে marks সাধারণত বাড়ে
- attendance উচ্চ হলে performance better হয়
- sleep_hours মাঝামাঝি range এ optimal performance দেয়

---

## 🚀 What I Learned

- 3D visualization concept
- multi-variable relationship analysis
- interactive plotting with Plotly
- camera control concept in 3D space

---

## 🧠 Key Concepts (Quick Revision)

- 3D scatter = 3 variables একসাথে visualize করা
- x, y, z axis = 3 numerical dimensions
- color/size = extra dimension add করা যায়
- correlation = variable relationship measure

---

## 📝 Notes

- বেশি 3D plot use করলে visualization confusing হতে পারে
- proper axis labeling খুব important
- camera angle change করলে pattern better বোঝা যায়

---

## 📌 Next Day Preview

- আগামী দিনে শিখবো **Surface Plot (3D surface visualization)**
- continuous 3D function visualization
- mathematical surface analysis

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- color mapping add করা
- attendance based grouping করা
- animation based 3D plot try করা

### 🧪 Practice Ideas

- sleep_hours vs marks vs attendance swap করো
- best performing students highlight করো
- correlation strongest variable বের করো
