# 📅 Day 5 — Bar Chart (Plotly Express)

## 🎯 Objective

- আজকে Bar Chart ব্যবহার করে category-based data comparison শেখা।
- Business analytics style visualization তৈরি করা।
- Grouped, stacked, এবং horizontal bar chart তৈরি করা।
- Real-world sales analysis workflow বোঝা।

## 📚 Topics Covered

- px.bar()
- Grouped bar chart
- Stacked bar chart
- Horizontal bar chart
- Category comparison

## 📁 Project Structure

```bash
Day 5 — Bar Chart/
│── 1_basic_bar_chart.py
│── 2_grouped_bar_chart.py
│── 3_stacked_bar_chart.py
│── 4_horizontal_bar_chart.py
│── sales_data.csv
│── README.md
```

## 📊 Dataset

- **File Name:** `sales_data.csv`
- **Description:** Monthly sales dataset by region used for category comparison and business analysis.
- **Columns:**
  - `month` → month name
  - `region` → sales region
  - `sales` → total sales value
  - `profit` → profit value

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_bar_chart.py`

### 🔹 Purpose

- Basic bar chart তৈরি করা
- month-wise sales comparison দেখা

### 🧾 Code

```python id="b5c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

fig = px.bar(
    df,
    x="month",
    y="sales",
    title="Monthly Sales"
)

fig.show()
```

### 🧠 Explanation

- `px.bar()` → bar chart তৈরি করে
- `x="month"` → category axis (months)
- `y="sales"` → values plot করে
- Logic → category comparison visualization

---

## 📄 2. `2_grouped_bar_chart.py`

### 🔹 Purpose

- grouped comparison তৈরি করা
- region-wise sales compare করা

### 🧾 Code

```python id="b5c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

fig = px.bar(
    df,
    x="month",
    y="sales",
    color="region",
    barmode="group",
    title="Grouped Bar Chart: Sales by Region"
)

fig.show()
```

### 🧠 Explanation

- `color="region"` → region-based grouping
- `barmode="group"` → side-by-side bars
- Logic → multiple category comparison in same chart

---

## 📄 3. `3_stacked_bar_chart.py`

### 🔹 Purpose

- stacked contribution analysis
- total sales breakdown

### 🧾 Code

```python id="b5c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

fig = px.bar(
    df,
    x="month",
    y="sales",
    color="region",
    barmode="stack",
    title="Stacked Bar Chart: Sales Contribution"
)

fig.show()
```

### 🧠 Explanation

- `barmode="stack"` → bars একসাথে stack হয়
- contribution analysis সহজ হয়
- Logic → total + category breakdown visualization

---

## 📄 4. `4_horizontal_bar_chart.py`

### 🔹 Purpose

- ranking style chart তৈরি করা
- horizontal bar visualization

### 🧾 Code

```python id="b5c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

region_sales = df.groupby("region")["sales"].sum().reset_index()

fig = px.bar(
    region_sales,
    x="sales",
    y="region",
    orientation="h",
    color="sales",
    title="Total Sales by Region"
)

fig.show()
```

### 🧠 Explanation

- `groupby()` → region-wise total sales বের করে
- `orientation="h"` → horizontal bar chart
- ranking visualization সহজ হয়
- Logic → aggregation + ranking display

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Basic category comparison করা হয়েছে
- Grouped comparison তৈরি করা হয়েছে
- Contribution analysis (stacked) করা হয়েছে
- Horizontal ranking chart তৈরি করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Month-wise sales comparison সহজে বোঝা যায়
- Region-wise performance compare করা যায়
- Contribution analysis clearer হয় stacked chart এ
- Ranking visualization horizontal chart এ best

---

## 🚀 What I Learned

- Bar chart is best for categorical comparison
- Grouped bar = side-by-side comparison
- Stacked bar = contribution analysis
- Horizontal bar = ranking visualization
- Aggregation improves insight quality

---

## 🧠 Key Concepts (Quick Revision)

- `px.bar()` → category comparison
- `barmode="group"` → side-by-side bars
- `barmode="stack"` → contribution view
- `orientation="h"` → horizontal layout
- `groupby()` → data aggregation

---

## 📝 Notes

- Too many categories দিলে chart cluttered হয়
- Stacked charts always need clean grouping
- Aggregation is important for correct analysis

---

## 📌 Next Day Preview

- আগামী দিনে Histogram শিখবো
- distribution analysis শুরু হবে
- data spread এবং frequency বুঝতে শিখবো

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- profit vs sales dual bar chart বানানো
- interactive filters যোগ করা
- dashboard style bar visualization তৈরি করা

### 🧪 Practice Ideas

- region-wise profit compare করো
- best performing month find করো
- stacked chart দিয়ে contribution analysis করো
