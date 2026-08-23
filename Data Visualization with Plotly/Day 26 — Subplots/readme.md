# 📅 Day 26 — Subplots

---

# 🎯 Objective

- আজকে শিখার লক্ষ্য হলো একাধিক chart একসাথে এক figure-এর মধ্যে দেখানো (dashboard style visualization)
- কীভাবে business dashboard বানানো যায় তা শেখা
- problem solve করা হচ্ছে: **single chart data insight কম দেয় → multiple charts একসাথে compare করা সহজ করা**

---

# 📚 Topics Covered

- Subplots concept
- make_subplots() usage
- Multiple charts in one figure
- Shared axes (shared_xaxes)
- Dashboard-style layout
- add_trace() concept

---

# 📁 Project Structure

```text id="p26s1"
Day 26 — Subplots/
│── main.py
│── analysis.py
│── utils.py
│── data.csv
│── README.md
```

---

# 📊 Dataset

- File Name: `sales_data.csv`
- Description: Monthly sales, profit, and expenses tracking data

### Columns:

- month → Month name
- sales → Total sales
- profit → Total profit
- expenses → Total expenses

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. main.py

### 🔹 Purpose

- Basic subplot তৈরি করা
- sales ও profit একসাথে compare করা

### 🧾 Code

```python id="q7v1a1"
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("sales_data.csv")

fig = make_subplots(rows=2, cols=1)

fig.add_trace(
    go.Scatter(x=df["month"], y=df["sales"], name="Sales"),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=df["month"], y=df["profit"], name="Profit"),
    row=2, col=1
)

fig.update_layout(title="Basic Subplots Example")

fig.show()
```

### 🧠 Explanation

- Line 1 → pandas import করা হয়েছে data handle করার জন্য
- Line 2 → Plotly graph_objects import করা হয়েছে
- Line 3 → subplot system import করা হয়েছে
- Line 5 → CSV data load করা হয়েছে
- Line 7 → 2 rows subplot তৈরি করা হয়েছে
- Line 9-12 → sales chart প্রথম row-এ বসানো হয়েছে
- Line 14-17 → profit chart দ্বিতীয় row-এ বসানো হয়েছে
- Overall → multi-chart comparison তৈরি হয়েছে

---

## 📄 2. analysis.py

### 🔹 Purpose

- shared axes ব্যবহার করে aligned comparison করা
- time-based analysis improve করা

### 🧾 Code

```python id="q7v1a2"
fig = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True
)

fig.add_trace(go.Scatter(x=df["month"], y=df["sales"], name="Sales"), row=1, col=1)
fig.add_trace(go.Scatter(x=df["month"], y=df["profit"], name="Profit"), row=2, col=1)

fig.update_layout(title="Shared Axis Subplots")

fig.show()
```

### 🧠 Explanation

- shared_xaxes=True → একই timeline ব্যবহার করা হয়
- দুই chart perfectly aligned হয়
- comparison সহজ হয়
- business analysis আরও clear হয়

---

## 📄 3. utils.py (if any)

### 🔹 Purpose

- reusable plotting helper idea

### 🧾 Code

```python id="q7v1a3"
def subplot_title(title):
    return {"text": title}
```

### 🧠 Explanation

- reusable layout helper function
- title formatting সহজ করে
- multiple dashboards-এ ব্যবহার করা যায়

---

# ⚙️ Implementation Flow

- Data load করা হয়েছে
- Subplot layout তৈরি করা হয়েছে
- Multiple charts একসাথে যুক্ত করা হয়েছে
- Shared axis ব্যবহার করা হয়েছে
- Dashboard-style visualization তৈরি হয়েছে

---

# 📈 Output / Result

### Key findings:

- sales vs profit side-by-side compare করা গেছে
- expenses trend আলাদাভাবে দেখা গেছে
- business performance এক নজরে বোঝা গেছে

---

# 🚀 What I Learned

- subplot system কিভাবে কাজ করে
- multiple charts এক figure-এ combine করা
- shared axes ব্যবহার করে better comparison করা

---

# 🧠 Key Concepts (Quick Revision)

- make_subplots() → grid layout তৈরি করে
- add_trace() → subplot-এ chart যোগ করে
- shared_xaxes → same timeline alignment
- dashboard layout → multi-metric analysis

---

# 📝 Notes

- subplots = real dashboard foundation
- too many charts দিলে confusion হতে পারে
- proper layout design খুব important

---

# 📌 Next Day Preview

- আগামী দিনে শিখবো:
  - Advanced dashboard interaction
  - Filtering & dropdown controls
  - Real-time style analytics layout

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- KPI dashboard design
- sales vs expense ratio chart
- profit trend highlighting

## 🧪 Practice Ideas

- CEO dashboard তৈরি করা
- finance monitoring system বানানো
- business performance tracker design করা
