# 📅 Day 1 — Introduction to Plotly

## 🎯 Objective

- আজকে Plotly কী, কেন ব্যবহার করা হয়, আর কেন এটি data visualization-এর জন্য গুরুত্বপূর্ণ — সেটা শেখা।
- Static chart আর interactive chart-এর মধ্যে পার্থক্য বোঝা।
- Plotly দিয়ে প্রথম interactive chart তৈরি করা।

## 📚 Topics Covered

- What is Plotly
- Why Plotly is important
- Plotly vs Matplotlib vs Seaborn
- Installation
- Plotly Express vs Graph Objects
- First interactive chart
- Understanding `fig.show()`

## 📁 Project Structure

```bash
Day 1 — Introduction to Plotly/
│── 1_intro.py
│── 2_first_chart.py
│── 3_plotly_vs_mpl_vs_seaborn.py
│── data.csv
│── README.md
```

## 📊 Dataset

- **File Name:** `data.csv`
- **Description:** Simple weekly sales dataset used to create the first interactive Plotly chart.
- **Columns:**
  - `day` → day name of the week
  - `sales` → sales value for that day
  - `profit` → profit value for that day

## 💻 Code Breakdown (File by File)

### 📄 1. `1_intro.py`

#### 🔹 Purpose

- এই file-এ Plotly-এর basic introduction দেওয়া হয়েছে।
- Plotly কী, কী কাজে লাগে, এবং কেন এটি important — সেটা explain করা হয়েছে।
- Installation command এবং basic import দেখানো হয়েছে।

#### 🧾 Code

```python
# ==========================
# DAY 1: INTRO TO PLOTLY
# ==========================

"""
What is Plotly?

Plotly is a Python library used to create:
- Interactive charts
- Web-ready visualizations
- Dashboards

Unlike static plots (Matplotlib),
Plotly allows:
- Zoom
- Hover tooltips
- Click interaction
"""

# Why Plotly is important:
# - Used in Data Science & AI dashboards
# - Used in business analytics tools
# - Works in web apps (Dash framework)

# --------------------------
# Installation (run in terminal)
# --------------------------
# pip install plotly

# --------------------------
# Importing Plotly Express
# --------------------------
import plotly.express as px

print("Plotly imported successfully!")
```

#### 🧠 Explanation

- `import plotly.express as px` → Plotly Express import করা হয়েছে, যা দ্রুত chart বানাতে সাহায্য করে।
- comment block-এর মাধ্যমে Plotly-এর core idea explain করা হয়েছে।
- `print()` দিয়ে check করা হয়েছে library ঠিকমতো import হয়েছে কি না।
- Logic → প্রথমে library সম্পর্কে ধারণা, তারপর setup, তারপর import confirm করা।

---

### 📄 2. `2_first_chart.py`

#### 🔹 Purpose

- এই file-এ প্রথম interactive Plotly chart তৈরি করা হয়েছে।
- CSV file load করে sales trend দেখানো হয়েছে।
- `fig.show()` কীভাবে chart render করে সেটা শেখানো হয়েছে।

#### 🧾 Code

```python
# ==========================
# FIRST INTERACTIVE CHART
# ==========================

import pandas as pd
import plotly.express as px

# --------------------------
# Load dataset
# --------------------------
df = pd.read_csv("data.csv")

# Show data (just to understand)
print(df)

# --------------------------
# Create first interactive line chart
# --------------------------
fig = px.line(
    df,
    x="day",
    y="sales",
    title="Daily Sales Trend"
)

# --------------------------
# Show chart
# --------------------------
fig.show()

"""
IMPORTANT CONCEPT:

fig.show()

- This opens an interactive chart in browser
- You can zoom, hover, pan
- This is the key difference vs Matplotlib
"""
```

#### 🧠 Explanation

- `pd.read_csv("data.csv")` → dataset load করা হয়েছে।
- `px.line()` → line chart বানানো হয়েছে।
- `x="day"` → horizontal axis-এ day দেখাচ্ছে।
- `y="sales"` → vertical axis-এ sales দেখাচ্ছে।
- `fig.show()` → chart display করার জন্য সবচেয়ে important method।
- Logic → data load → chart create → interactiveভাবে show।

---

### 📄 3. `3_plotly_vs_mpl_vs_seaborn.py`

#### 🔹 Purpose

- এই file-এ Plotly, Matplotlib, আর Seaborn-এর comparison দেখানো হয়েছে।
- Static plotting আর interactive plotting-এর difference বোঝানো হয়েছে।

#### 🧾 Code

```python
# ==========================
# PLOTLY VS OTHER LIBRARIES
# ==========================

"""
We compare 3 popular visualization libraries:

1. Matplotlib
2. Seaborn
3. Plotly
"""

# --------------------------
# 1. Matplotlib (static)
# --------------------------
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)
plt.title("Matplotlib (Static Plot)")
plt.show()

# Problem:
# - No zoom
# - No hover
# - Not interactive

# --------------------------
# 2. Seaborn (beautiful but still static)
# --------------------------
import seaborn as sns

tips = sns.load_dataset("tips")

sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Seaborn (Statistical Plot)")
plt.show()

# Good for:
# - Statistics
# - Quick EDA

# --------------------------
# 3. Plotly (interactive)
# --------------------------
import plotly.express as px

fig = px.bar(
    tips,
    x="day",
    y="total_bill",
    title="Plotly (Interactive Plot)"
)

fig.show()

"""
Plotly advantages:

✔ Zoom in/out
✔ Hover details
✔ Interactive tooltips
✔ Web-ready charts
✔ Dashboard support
"""
```

#### 🧠 Explanation

- Matplotlib → basic and static visualization.
- Seaborn → great for statistical plots, but still static.
- Plotly → interactive chart তৈরি করে, যেখানে hover, zoom, pan পাওয়া যায়।
- Logic → same type of data visualization তিনভাবে compare করা হয়েছে।

## ⚙️ Implementation Flow

- Data load করা হয়েছে।
- Plotly সম্পর্কে basic ধারণা নেওয়া হয়েছে।
- First interactive chart তৈরি করা হয়েছে।
- Plotly, Matplotlib, আর Seaborn compare করা হয়েছে।
- Result হিসেবে interactive visualization experience পাওয়া গেছে।

## 📈 Output / Result

### Key findings:

- Plotly interactive chart তৈরি করতে খুব সহজ।
- `fig.show()` দিয়েই browser-based visualization দেখা যায়।
- Plotly static library না, তাই hover এবং zoom ব্যবহার করা যায়।
- Matplotlib and Seaborn useful, but Plotly dashboard-friendly।

## 🚀 What I Learned

- Plotly কী এবং কেন ব্যবহার করা হয়।
- Plotly Express দিয়ে দ্রুত chart বানানো যায়।
- Interactive visualization user experience improve করে।
- `fig.show()` Plotly output দেখানোর মূল method।

## 🧠 Key Concepts (Quick Revision)

- Plotly = interactive visualization library
- Plotly Express = quick and simple charting
- Graph Objects = advanced customization
- `fig.show()` = chart display করার জন্য use হয়
- Plotly charts browser-এ open হয়
- Hover, zoom, pan supported

## 📝 Notes

- প্রথমবার Plotly ব্যবহার করলে `fig.show()`-এর interactive output একটু নতুন লাগতে পারে।
- Installation না থাকলে আগে `pip install plotly` চালাতে হবে।
- CSV file path ঠিক না হলে `read_csv()` error দিতে পারে।

## 📌 Next Day Preview

- আগামী দিনে Plotly Express basics শিখবো।
- Layout, template, hover tooltip, zoom, pan — এগুলো আরও deeply বুঝবো।
- আরও সুন্দর ও customizable chart বানানো শিখবো।

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- আরও বড় dataset use করা যেতে পারে।
- More chart types add করা যেতে পারে।
- Different Plotly themes try করা যেতে পারে।

### 🧪 Practice Ideas

- নিজের marks dataset দিয়ে line chart বানাও।
- sales/profit data দিয়ে bar chart try করো।
- একই data Matplotlib, Seaborn, আর Plotly-তে plot করে difference compare করো।
