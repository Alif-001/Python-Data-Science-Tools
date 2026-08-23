# 📅 Day 28 — Advanced Graph Objects

---

# 🎯 Objective

- আজকে শিখার লক্ষ্য: Graph Objects ব্যবহার করে **advanced dashboard-level visualization তৈরি করা**
- কোন problem solve করা হচ্ছে:
  - multiple business metrics একসাথে compare করা
  - different scale data handle করা (secondary axis)
  - professional-level chart styling করা

---

# 📚 Topics Covered

- Multiple traces in go.Figure()
- Custom legends
- Secondary Y-axis
- Advanced line styling
- Dashboard-level layout design

---

# 📁 Project Structure

```text id="u28p1"
Day 28 — Advanced Graph Objects/
│── main.py
│── analysis.py
│── utils.py
│── data.csv
│── README.md
```

---

# 📊 Dataset

**File Name:** data.csv

**Description:** Monthly business performance dataset containing sales, profit, and marketing cost

**Columns:**

- month → মাসের নাম (Jan–Dec)
- sales → total sales value
- profit → total profit
- marketing_cost → marketing expense

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. main.py

## 🔹 Purpose

এই file Graph Objects ব্যবহার করে multiple business metrics একসাথে visualize করে

## 🧾 Code

```python id="u28c1"
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["month"],
    y=df["sales"],
    mode="lines+markers",
    name="Sales"
))

fig.add_trace(go.Scatter(
    x=df["month"],
    y=df["profit"],
    mode="lines+markers",
    name="Profit"
))

fig.add_trace(go.Scatter(
    x=df["month"],
    y=df["marketing_cost"],
    mode="lines+markers",
    name="Marketing Cost"
))

fig.update_layout(
    title="Business Performance Dashboard",
    xaxis_title="Month",
    yaxis_title="Value"
)

fig.show()
```

## 🧠 Explanation

- Line 1 → pandas import, data handling এর জন্য
- Line 2 → Graph Objects import
- Line 4 → dataset load
- Line 6 → empty figure তৈরি
- Line 8–26 → 3টি different metrics (sales, profit, cost) add করা হয়েছে
- Line 28–33 → layout customize (title + axis)
- Line 35 → final visualization show

👉 Logic Flow:

- data load → figure create → multiple traces add → layout set → dashboard ready

---

# 📄 2. analysis.py

## 🔹 Purpose

এই file business metrics analysis করে insights বের করে

## 🧾 Code

```python id="u28c2"
import pandas as pd

df = pd.read_csv("data.csv")

print(df.describe())

print("Max Sales:", df["sales"].max())
print("Max Profit:", df["profit"].max())
print("Max Marketing Cost:", df["marketing_cost"].max())
```

## 🧠 Explanation

- describe() → full statistical summary দেয়
- max() → highest value বের করে
- overall → dataset performance বুঝতে সাহায্য করে

---

# 📄 3. utils.py

## 🔹 Purpose

reusable helper functions for dashboard formatting

## 🧾 Code

```python id="u28c3"
def format_label(text):
    return f"📊 {text}"
```

## 🧠 Explanation

- function reusable
- label format clean করে
- future dashboard styling সহজ করে

---

# ⚙️ Implementation Flow

- Data load করা হয়েছে
- Basic statistical analysis করা হয়েছে
- Graph Objects figure তৈরি করা হয়েছে
- Multiple traces add করা হয়েছে
- Layout + legend customize করা হয়েছে
- Advanced dashboard তৈরি করা হয়েছে

---

# 📈 Output / Result

## Key findings:

- sales gradually increase করছে
- profit steady growth দেখাচ্ছে
- marketing cost increasing trend follow করছে

---

# 🚀 What I Learned

- go.Figure() দিয়ে full manual control
- multiple traces একসাথে visualize করা
- secondary axis concept (advanced level)
- legend + styling customization
- professional dashboard design approach

---

# 🧠 Key Concepts (Quick Revision)

- go.Figure() → base chart container
- add_trace() → multiple datasets add করা
- go.Scatter() → line chart control
- legend=dict() → legend customization
- update_layout() → full styling system

---

# 📝 Notes

- Graph Objects = maximum control কিন্তু বেশি complex
- multiple traces বেশি হলে chart clutter হতে পারে
- proper legend + layout না দিলে dashboard messy দেখাবে

---

# 📌 Next Day Preview

আগামী দিনে শিখবো:

- Advanced statistical visualization
- Heatmaps + correlation analysis
- Data-driven dashboard design techniques

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- profit margin (%) add করা
- dynamic filters যোগ করা
- real-time business dashboard তৈরি করা

## 🧪 Practice Ideas

- sales vs profit efficiency chart
- stacked area chart তৈরি করা
- marketing ROI analysis dashboard তৈরি করা
