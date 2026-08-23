# 📅 Day 12 — Density Heatmap (`px.density_heatmap()`)

---

## 🎯 Objective

- আজকে আমরা শিখবো কীভাবে data-এর **density (ঘনত্ব)** visualize করা যায়
- বুঝবো কোথায় data বেশি concentrate করছে
- correlation pattern “heat” আকারে দেখা
- scatter plot এর advanced alternative হিসেবে heatmap ব্যবহার করা

---

## 📚 Topics Covered

- `px.density_heatmap()`
- Heatmap basics
- Data density visualization
- Correlation density analysis
- Binning (`nbinsx`, `nbinsy`)
- Color scaling
- Heatmap vs Scatter comparison

---

## 📁 Project Structure

```text id="d12p1"
Day 12 — Density Heatmap/
│
├── 1_basic_density_heatmap.py
├── 2_heatmap_bins.py
├── 3_correlation_density.py
├── 4_color_scaling.py
└── student_data.csv
```

---

## 📊 Dataset

**File Name:** `student_data.csv`

**Description:**
Students performance dataset used to analyze study habits and marks relationship through density visualization.

**Columns:**

- study_hours → কত ঘণ্টা পড়াশোনা করা হয়
- sleep_hours → কত ঘণ্টা ঘুমানো হয়
- attendance → class attendance (%)
- marks → exam marks

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_density_heatmap.py`

### 🔹 Purpose

- basic density heatmap তৈরি করা
- study_hours vs marks এর density দেখা

### 🧾 Code

```python id="d12c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

fig = px.density_heatmap(
    df,
    x="study_hours",
    y="marks",
    title="Study Hours vs Marks Density Heatmap"
)

fig.show()
```

---

### 🧠 Explanation

- `pd.read_csv()` → dataset load করে
- `px.density_heatmap()` → 2D density visualization তৈরি করে
- `x`, `y` → কোন দুই variable compare হবে সেট করে
- `fig.show()` → interactive heatmap দেখায়

👉 Logic:

- যেখানে data point বেশি → সেখানে বেশি “heat”
- যেখানে কম → light area

---

## 📄 2. `2_heatmap_bins.py`

### 🔹 Purpose

- heatmap এর resolution control করা
- data grouping smooth বা detailed করা

### 🧾 Code

```python id="d12c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

fig = px.density_heatmap(
    df,
    x="study_hours",
    y="marks",
    nbinsx=6,
    nbinsy=6,
    title="Heatmap with Controlled Bins"
)

fig.show()
```

---

### 🧠 Explanation

- `nbinsx` → x-axis কত ভাগে ভাগ হবে
- `nbinsy` → y-axis কত ভাগে ভাগ হবে

👉 Logic:

- কম bins → smooth view
- বেশি bins → detailed view

---

## 📄 3. `3_correlation_density.py`

### 🔹 Purpose

- attendance vs marks এর density relationship দেখা
- correlation pattern detect করা

### 🧾 Code

```python id="d12c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

fig = px.density_heatmap(
    df,
    x="attendance",
    y="marks",
    title="Attendance vs Marks Density"
)

fig.show()
```

---

### 🧠 Explanation

- attendance এবং marks এর মধ্যে relationship দেখা যায়
- high attendance অঞ্চলে marks বেশি cluster করলে → positive correlation

👉 Logic:

- data cluster = relationship strength বোঝায়

---

## 📄 4. `4_color_scaling.py`

### 🔹 Purpose

- heatmap এর color style customize করা
- visualization আরও clear করা

### 🧾 Code

```python id="d12c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("student_data.csv")

fig = px.density_heatmap(
    df,
    x="study_hours",
    y="marks",
    title="Heatmap with Color Scaling",
    color_continuous_scale="Viridis"
)

fig.show()
```

---

### 🧠 Explanation

- `color_continuous_scale` → heatmap color scheme control করে
- `"Viridis"` → most readable scientific color scale

👉 Logic:

- dark/bright color → density intensity বোঝায়

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- 2 variables select করা হয়েছে
- density heatmap তৈরি করা হয়েছে
- bin size adjust করা হয়েছে
- correlation visually analyze করা হয়েছে
- color scale customize করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- study_hours বাড়লে marks সাধারণত বাড়ে
- attendance এবং marks এর মধ্যে strong positive cluster দেখা যায়
- certain ranges এ students বেশি concentrate করে
- heatmap scatter plot থেকে clearer pattern দেখায়

---

## 🚀 What I Learned

- Data density visualization খুব powerful EDA tool
- scatter plot clutter হলে heatmap better
- binning visualization control করে
- correlation pattern “color intensity” দিয়ে বোঝা যায়

---

## 🧠 Key Concepts (Quick Revision)

- Density Heatmap → data concentration visualization
- Binning → grouping resolution control
- Color intensity → data density indicator
- Correlation → variable relationship pattern

---

## 📝 Notes

- খুব large dataset এ heatmap best কাজ করে
- wrong bin size হলে pattern misleading হতে পারে
- color scale choice visualization clarity affect করে

---

## 📌 Next Day Preview

আগামী দিনে আমরা শিখবো:

- 📊 Density Contour Plot (`px.density_contour()`)
- smooth density region visualization
- statistical contour understanding
- advanced pattern detection

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- real-world dataset (sales / users / traffic) ব্যবহার করো
- multiple heatmaps compare করো
- interactive dashboard বানাও

---

### 🧪 Practice Ideas

- `sleep_hours vs marks` heatmap বানাও
- `attendance vs study_hours` try করো
- bin size change করে pattern observe করো
- best correlation pair খুঁজে বের করো
