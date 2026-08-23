# 📅 Day 10 — Area Chart (Plotly Express)

## 🎯 Objective

- আজকে Area Chart ব্যবহার করে time-series data visualization শেখা।
- cumulative trend বোঝা।
- stacked area chart দিয়ে multiple category analysis করা।
- dashboard-style trend analysis তৈরি করা।

---

## 📚 Topics Covered

- px.area()
- Cumulative trend
- Stacked area chart
- Time-series area visualization

---

## 📁 Project Structure

```bash
Day 10 — Area Chart/
│── 1_basic_area.py
│── 2_cumulative_trend.py
│── 3_stacked_area_chart.py
│── 4_time_series_area.py
│── sales_trend.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `sales_trend.csv`
- **Description:** Product-wise daily sales dataset used for time-series and trend analysis.
- **Columns:**
  - `date` → sales date
  - `product` → product name (A, B, C)
  - `sales` → number of sales

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `main.py` (1_basic_area.py)

### 🔹 Purpose

- Basic area chart তৈরি করা
- total sales trend visualize করা

### 🧾 Code

```python id="a10c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

fig = px.area(
    df,
    x="date",
    y="sales",
    title="Basic Area Chart (Total Sales)"
)

fig.show()
```

### 🧠 Explanation

- `px.area()` → filled line chart তৈরি করে
- `sort_values()` → time-series order ঠিক রাখে
- Logic → sales growth visually represent করা

---

## 📄 2. `analysis.py` (2_cumulative_trend.py)

### 🔹 Purpose

- cumulative trend analysis করা
- daily total sales দেখানো

### 🧾 Code

```python id="a10c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")
df["date"] = pd.to_datetime(df["date"])

daily = df.groupby("date")["sales"].sum().reset_index()

fig = px.area(
    daily,
    x="date",
    y="sales",
    title="Cumulative Sales Trend"
)

fig.show()
```

### 🧠 Explanation

- `groupby()` → daily total sales বের করে
- area chart → growth visualization দেখায়
- Logic → overall business performance tracking

---

## 📄 3. `utils.py` (3_stacked_area_chart.py)

### 🔹 Purpose

- product-wise stacked area chart তৈরি করা
- category contribution analysis

### 🧾 Code

```python id="a10c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")
df["date"] = pd.to_datetime(df["date"])

fig = px.area(
    df,
    x="date",
    y="sales",
    color="product",
    title="Stacked Area Chart: Product-wise Sales"
)

fig.show()
```

### 🧠 Explanation

- `color="product"` → multiple categories show করে
- stacked effect → contribution analysis বোঝায়
- Logic → product-wise performance comparison

---

## 📄 4. `main.py` (4_time_series_area.py)

### 🔹 Purpose

- advanced time-series area visualization
- dashboard-style analysis

### 🧾 Code

```python id="a10c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")
df["date"] = pd.to_datetime(df["date"])

df = df.sort_values("date")

fig = px.area(
    df,
    x="date",
    y="sales",
    color="product",
    line_group="product",
    title="Time Series Area Visualization"
)

fig.update_layout(
    hovermode="x unified"
)

fig.show()
```

### 🧠 Explanation

- `line_group` → product separation
- `hovermode="x unified"` → clean dashboard hover
- Logic → advanced time-series analysis

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- date column convert করা হয়েছে
- sorting করা হয়েছে (important for time-series)
- basic area chart তৈরি করা হয়েছে
- cumulative trend analysis করা হয়েছে
- stacked product-wise chart বানানো হয়েছে
- advanced time-series visualization করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- sales growth over time clearly দেখা যায়
- product-wise contribution compare করা যায়
- overall business trend বোঝা যায়
- dashboard-style visualization তৈরি হয়

---

## 🚀 What I Learned

- area chart trend visualization এর জন্য খুব powerful
- cumulative analysis business insights দেয়
- stacked area chart category comparison সহজ করে
- time-series data properly sort করা জরুরি

---

## 🧠 Key Concepts (Quick Revision)

- area chart → line + filled region
- cumulative trend → total growth over time
- stacked area → multiple category contribution
- time-series → ordered date-based analysis

---

## 📝 Notes

- unsorted data হলে chart ভুল দেখাতে পারে
- too many categories হলে readability কমে যায়
- time-series analysis এ date format খুব important

---

## 📌 Next Day Preview

- আগামী দিনে Scatter Matrix শিখবো
- multi-variable relationship analysis করা হবে
- correlation exploration শুরু হবে

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- profit column add করে dual area chart বানানো
- interactive filters add করা
- moving average trend যোগ করা

### 🧪 Practice Ideas

- product A vs B trend compare করো
- weekly cumulative sales analysis করো
- line chart vs area chart compare করো
