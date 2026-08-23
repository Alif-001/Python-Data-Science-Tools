# 📅 Day 13 — Density Contour (`px.density_contour()`)

---

## 🎯 Objective

- আজকে আমরা শিখবো কীভাবে data-এর **density regions** smooth ভাবে visualize করা যায়
- বুঝবো কোথায় data বেশি concentrate করছে (zones আকারে)
- heatmap এর পরিবর্তে smooth statistical visualization ব্যবহার করা
- data distribution কে “surface / contour map” হিসেবে দেখা

---

## 📚 Topics Covered

- `px.density_contour()`
- Density regions visualization
- Statistical distribution understanding
- Contour lines concept
- Smooth vs rough density view
- Binning and resolution control
- Heatmap vs Contour comparison

---

## 📁 Project Structure

```text id="d13p1"
Day 13 — Density Contour/
│
├── 1_basic_density_contour.py
├── 2_density_regions.py
├── 3_statistical_view.py
├── 4_smooth_contours.py
└── student_data.csv
```

---

## 📊 Dataset

**File Name:** `student_data.csv`

**Description:**
Students performance dataset used to visualize study behavior vs marks using density contour plots.

**Columns:**

- study_hours → কত ঘণ্টা পড়াশোনা করা হয়
- marks → exam marks
- sleep_hours → কত ঘণ্টা ঘুমানো হয়
- attendance → class attendance (%)

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_density_contour.py`

### 🔹 Purpose

- basic density contour plot তৈরি করা
- study_hours vs marks এর distribution দেখা

### 🧾 Code

```python id="d13c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

fig = px.density_contour(
    df,
    x="study_hours",
    y="marks",
    title="Study Hours vs Marks - Density Contour"
)

fig.show()
```

---

### 🧠 Explanation

- `pd.read_csv()` → dataset load করে
- `px.density_contour()` → density regions তৈরি করে
- `x`, `y` → কোন variables analyze হবে সেট করে
- `fig.show()` → interactive plot দেখায়

👉 Logic:

- যেখানে data বেশি → contour lines ঘন হবে
- যেখানে data কম → lines দূরে থাকবে

---

## 📄 2. `2_density_regions.py`

### 🔹 Purpose

- density region গুলো highlight করা
- marks অনুযায়ী contour coloring দেখা

### 🧾 Code

```python id="d13c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

fig = px.density_contour(
    df,
    x="study_hours",
    y="marks",
    color="marks",
    title="Density Regions (Colored Contours)"
)

fig.show()
```

---

### 🧠 Explanation

- `color="marks"` → marks অনুযায়ী contour intensity change হয়
- একই plot এ multiple density zones দেখা যায়

👉 Logic:

- high marks region আলাদা cluster তৈরি করে
- pattern separation সহজ হয়

---

## 📄 3. `3_statistical_view.py`

### 🔹 Purpose

- attendance vs marks এর statistical pattern দেখা
- filled contour visualization ব্যবহার করা

### 🧾 Code

```python id="d13c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

fig = px.density_contour(
    df,
    x="attendance",
    y="marks",
    title="Attendance vs Marks - Statistical View"
)

fig.update_traces(contours_coloring="fill")

fig.show()
```

---

### 🧠 Explanation

- `contours_coloring="fill"` → contour areas fill করে heat-like effect দেয়
- attendance vs marks relationship visually strong হয়

👉 Logic:

- filled regions = density zones
- pattern structure easily visible

---

## 📄 4. `4_smooth_contours.py`

### 🔹 Purpose

- smoother contour visualization তৈরি করা
- resolution control করা

### 🧾 Code

```python id="d13c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

fig = px.density_contour(
    df,
    x="study_hours",
    y="marks",
    nbinsx=20,
    nbinsy=20,
    title="Smooth Density Contour"
)

fig.show()
```

---

### 🧠 Explanation

- `nbinsx`, `nbinsy` → resolution control করে
- বেশি bins → smoother contour surface

👉 Logic:

- high resolution → smooth pattern
- low resolution → rough pattern

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- 2 variables select করা হয়েছে
- density contour plot তৈরি করা হয়েছে
- color variation add করা হয়েছে
- filled contours ব্যবহার করা হয়েছে
- smoothness adjust করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- study_hours বাড়লে marks এর smooth upward trend দেখা যায়
- attendance এবং marks এর মধ্যে clear density zone তৈরি হয়
- students নির্দিষ্ট range এ cluster করে
- contour plot hidden structure দেখায়

---

## 🚀 What I Learned

- Contour plot data কে “surface” হিসেবে দেখায়
- heatmap এর চেয়ে smoother pattern বোঝা যায়
- binning visualization quality control করে
- statistical distribution visualize করা যায় সহজে

---

## 🧠 Key Concepts (Quick Revision)

- Density Contour → smooth density representation
- Contour lines → equal density regions
- Filled contours → heat-like zones
- Binning → resolution control
- Statistical visualization → pattern understanding

---

## 📝 Notes

- খুব noisy data হলে contour smoother হয় না
- proper bin selection খুব গুরুত্বপূর্ণ
- small dataset এ contour less effective হতে পারে

---

## 📌 Next Day Preview

আগামী দিনে আমরা শিখবো:

- 🌳 Treemap (`px.treemap()`)
- hierarchical data visualization
- nested categories understanding
- business data structure visualization

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- real-world dataset (sales / users) দিয়ে try করো
- heatmap vs contour compare করো
- multiple variables combine করে analysis করো

---

### 🧪 Practice Ideas

- `sleep_hours vs marks` contour plot বানাও
- `attendance vs study_hours` try করো
- bins change করে smoothness observe করো
- কোন variable strongest pattern তৈরি করে বের করো
