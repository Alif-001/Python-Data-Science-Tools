# 📅 Day 3 — Line Plot (Plotly Express)

## 🎯 Objective

- আজকে Line Plot এর মাধ্যমে data trend analysis শেখা।
- Time-series data কিভাবে visualize করতে হয় সেটা বোঝা।
- Multiple lines, markers, styling ব্যবহার করে professional chart তৈরি করা।
- Real-world trend analysis এর basic foundation তৈরি করা।

## 📚 Topics Covered

- px.line()
- Multiple lines
- Markers in line chart
- Styling lines
- Time-series visualization
- Trend analysis

## 📁 Project Structure

```bash
Day 3 — Line Plot/
│── 1_basic_line.py
│── 2_multiple_lines.py
│── 3_markers_and_styling.py
│── 4_time_series.py
│── sales_trend.csv
│── README.md
```

## 📊 Dataset

- **File Name:** `sales_trend.csv`
- **Description:** Daily sales and profit dataset used for trend analysis and time-series visualization.
- **Columns:**
  - `date` → daily date of records
  - `sales` → sales amount
  - `profit` → profit amount

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_line.py`

### 🔹 Purpose

- Basic line plot তৈরি করা
- sales trend visualize করা
- Plotly Express এর simplest usage বোঝা

### 🧾 Code

```python id="d3l1a1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")

df["date"] = pd.to_datetime(df["date"])

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Daily Sales Trend"
)

fig.show()
```

### 🧠 Explanation

- `pd.read_csv()` → dataset load করা হয়েছে
- `pd.to_datetime()` → date কে proper format এ convert করা হয়েছে
- `px.line()` → line chart তৈরি করছে
- `x="date"` → time axis সেট করা হয়েছে
- `y="sales"` → sales trend plot করা হয়েছে
- `fig.show()` → interactive chart display করছে
- Logic → time-based trend visualization

---

## 📄 2. `2_multiple_lines.py`

### 🔹 Purpose

- Sales এবং Profit একসাথে compare করা
- Multiple line chart তৈরি করা

### 🧾 Code

```python id="d3l2m1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")
df["date"] = pd.to_datetime(df["date"])

df_melted = df.melt(
    id_vars="date",
    value_vars=["sales", "profit"],
    var_name="metric",
    value_name="value"
)

fig = px.line(
    df_melted,
    x="date",
    y="value",
    color="metric",
    title="Sales vs Profit Trend"
)

fig.show()
```

### 🧠 Explanation

- `melt()` → data reshape করে long format বানায়
- `value_vars` → sales এবং profit combine করে
- `color="metric"` → আলাদা line তৈরি করে
- Logic → multiple metrics এক chart এ compare করা

---

## 📄 3. `3_markers_and_styling.py`

### 🔹 Purpose

- Line chart এ markers add করা
- Styling improve করা

### 🧾 Code

```python id="d3l3s1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")
df["date"] = pd.to_datetime(df["date"])

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Sales Trend with Markers"
)

fig.update_traces(
    mode="lines+markers",
    line=dict(color="blue", width=3)
)

fig.show()
```

### 🧠 Explanation

- `mode="lines+markers"` → line + data points দেখায়
- `line=dict()` → line styling customize করে
- markers → exact data points বুঝতে সাহায্য করে
- Logic → better readability + presentation quality

---

## 📄 4. `4_time_series.py`

### 🔹 Purpose

- Proper time-series visualization তৈরি করা
- sorted date-based analysis করা

### 🧾 Code

```python id="d3l4t1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Time Series Sales Analysis"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales",
    hovermode="x unified"
)

fig.show()
```

### 🧠 Explanation

- `sort_values()` → time order ঠিক করে
- `hovermode="x unified"` → একই সময়ে সব value দেখায়
- time-series analysis → pattern বুঝতে সাহায্য করে
- Logic → clean chronological visualization

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Date format convert করা হয়েছে
- Basic line chart তৈরি করা হয়েছে
- Multiple metrics compare করা হয়েছে
- Markers + styling add করা হয়েছে
- Final time-series analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Sales trend সহজে visualize করা যায়
- Profit vs Sales একসাথে compare করা যায়
- Time-series data analysis আরও meaningful হয়
- Markers data understanding improve করে

---

## 🚀 What I Learned

- Line plot is best for trend analysis
- Multiple lines দিয়ে comparison করা যায়
- Data reshaping (melt) খুব powerful technique
- Time-series analysis requires sorting + datetime conversion

---

## 🧠 Key Concepts (Quick Revision)

- `px.line()` → trend visualization
- `melt()` → data reshape
- `color=` → multiple lines
- `markers` → data points highlight
- time-series → ordered datetime data

---

## 📝 Notes

- Date না convert করলে chart ভুল order এ দেখাতে পারে
- Multiple lines এর জন্য data reshape important
- Large dataset এ performance optimize করা দরকার

---

## 📌 Next Day Preview

- আগামী দিনে Scatter Plot শিখবো
- Correlation analysis শুরু হবে
- Bubble chart + size/color encoding শেখা হবে

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- moving average trend add করা
- anomaly detection line যোগ করা
- interactive date range filter বানানো

### 🧪 Practice Ideas

- নিজের monthly sales data দিয়ে line chart বানাও
- sales vs profit compare করো
- time-series data sort করে trend analyze করো
