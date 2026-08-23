# 📅 Day 27 — Plotly Graph Objects

---

# 🎯 Objective

- আজকে শিখার লক্ষ্য: Plotly Express থেকে **low-level Graph Objects (go.Figure)** ব্যবহার করা
- কী সমস্যা solve করা হচ্ছে:
  - Pre-built chart limitation দূর করা
  - Full customization সহ professional dashboard তৈরি করা
  - Multiple traces একসাথে control করা

---

# 📚 Topics Covered

- go.Figure() basics
- go.Scatter()
- go.Bar()
- add_trace() system
- Layout customization (update_layout)
- Multi-trace visualization

---

# 📁 Project Structure

```text
Day 27 — Plotly Graph Objects/
│── main.py
│── analysis.py
│── utils.py
│── data.csv
│── README.md
```

---

# 📊 Dataset

**File Name:** data.csv

**Description:** Monthly sales, profit and expenses data for business visualization

**Columns:**

- month → মাসের নাম (Jan–Dec)
- sales → মোট sales value
- profit → profit value
- expenses → খরচ (cost)

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. main.py

## 🔹 Purpose

এই file Graph Objects ব্যবহার করে full control সহ charts তৈরি করে

## 🧾 Code

```python
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df["month"],
        y=df["sales"],
        mode="lines+markers",
        name="Sales"
    )
)

fig.update_layout(
    title="Sales Trend using Graph Objects",
    xaxis_title="Month",
    yaxis_title="Sales"
)

fig.show()
```

## 🧠 Explanation

- Line 1 → pandas import, data handle করার জন্য
- Line 2 → plotly Graph Objects import
- Line 4 → CSV file load করা হচ্ছে
- Line 6 → empty figure তৈরি করা হচ্ছে
- Line 8–14 → sales line chart manually add করা হচ্ছে
- Line 16–20 → layout customize (title, axis)
- Line 22 → final chart show করা হচ্ছে

👉 Logic:

- data → figure → trace add → layout customize → visualization

---

# 📄 2. analysis.py

## 🔹 Purpose

এই file data analysis এবং multiple metric comparison করে

## 🧾 Code

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.describe())

print("Max Sales:", df["sales"].max())
print("Max Profit:", df["profit"].max())
```

## 🧠 Explanation

- describe() → statistical summary দেয়
- max() → highest value বের করে
- overall → dataset understanding সহজ করে

---

# 📄 3. utils.py

## 🔹 Purpose

helper functions for reusable plotting logic

## 🧾 Code

```python
def format_title(title):
    return f"📊 {title}"
```

## 🧠 Explanation

- reusable function তৈরি করা হয়েছে
- title কে beautify করে return করে
- future dashboard design এর জন্য useful

---

# ⚙️ Implementation Flow

- Data load করা হয়েছে
- Basic analysis করা হয়েছে
- Graph Objects figure তৈরি করা হয়েছে
- Multiple traces add করা হয়েছে
- Layout customize করা হয়েছে
- Final dashboard visualization তৈরি হয়েছে

---

# 📈 Output / Result

## Key findings:

- sales trend gradually increase করছে
- profit steady growth দেখাচ্ছে
- expenses controlled pattern follow করছে

---

# 🚀 What I Learned

- go.Figure() দিয়ে manual chart control
- add_trace() দিয়ে multiple layers তৈরি
- Plotly Express vs Graph Objects difference
- professional dashboard design concept

---

# 🧠 Key Concepts (Quick Revision)

- go.Figure() → base container
- add_trace() → chart layer add করা
- go.Scatter() → line/scatter plot
- go.Bar() → bar chart
- update_layout() → full styling control

---

# 📝 Notes

- Graph Objects বেশি flexible কিন্তু complex
- Beginners প্রথমে Plotly Express শিখে তারপর GO ব্যবহার করা ভালো
- Mistake: too many traces দিলে chart messy হতে পারে

---

# 📌 Next Day Preview

আগামী দিনে শিখবো:

- Advanced figure composition
- Subplot + Graph Objects integration
- Professional multi-dashboard systems

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- Profit margin add করা
- Dynamic filters যোগ করা
- Real-time data update system

## 🧪 Practice Ideas

- sales vs expenses comparison chart
- stacked bar chart তৈরি করা
- multi-company dashboard বানানো
