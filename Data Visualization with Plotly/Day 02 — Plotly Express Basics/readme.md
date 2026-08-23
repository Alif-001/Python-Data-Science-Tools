# 📅 Day 2 — Plotly Express Basics

## 🎯 Objective

- আজকে Plotly Express (px) এবং Graph Objects (go) এর basic difference বোঝা।
- Figure object কীভাবে কাজ করে সেটা শেখা।
- Layout, theme, hover, zoom, pan — এগুলোর real interactive power দেখা।
- Simple থেকে slightly advanced interactive chart বানানো।

## 📚 Topics Covered

- plotly.express
- Figure object (plotly.graph_objects)
- Layout basics
- Themes / Templates
- Interactive features
- Hover tooltips
- Zoom & pan

## 📁 Project Structure

```bash
Day 2 — Plotly Express Basics/
│── 1_plotly_express_intro.py
│── 2_figure_object_basics.py
│── 3_layout_and_themes.py
│── 4_interactive_features.py
│── sales.csv
│── README.md
```

## 📊 Dataset

- **File Name:** `sales.csv`
- **Description:** Weekly sales dataset with region-based information used for visualization and comparison.
- **Columns:**
  - `day` → day of the week
  - `sales` → sales amount
  - `profit` → profit amount
  - `region` → sales region (North/South/East/West)

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_plotly_express_intro.py`

### 🔹 Purpose

- Plotly Express (px) এর basic introduction দেওয়া হয়েছে।
- খুব সহজভাবে line chart তৈরি করা হয়েছে।
- বুঝানো হয়েছে px কেন fast and beginner-friendly।

### 🧾 Code

```python
import pandas as pd
import plotly.express as px

# dataset load
df = pd.read_csv("sales.csv")

# simple line chart
fig = px.line(
    df,
    x="day",
    y="sales",
    title="Sales Trend (Plotly Express)"
)

fig.show()
```

### 🧠 Explanation

- `pd.read_csv()` → dataset load করা হয়েছে
- `px.line()` → simple line chart তৈরি করছে
- `x="day"` → X-axis এ দিন দেখাচ্ছে
- `y="sales"` → sales value plot করছে
- `fig.show()` → interactive chart browser এ open করছে
- Logic → data → quick chart → visualization

---

## 📄 2. `2_figure_object_basics.py`

### 🔹 Purpose

- Graph Objects (go) দিয়ে low-level control শেখা
- manually figure + trace add করা

### 🧾 Code

```python
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("sales.csv")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df["day"],
        y=df["sales"],
        mode="lines+markers",
        name="Sales"
    )
)

fig.show()
```

### 🧠 Explanation

- `go.Figure()` → empty chart container তৈরি করে
- `add_trace()` → chart data manually add করা হয়
- `go.Scatter()` → line + marker chart বানায়
- `mode="lines+markers"` → line + point দুটোই দেখায়
- Logic → full manual control over chart

---

## 📄 3. `3_layout_and_themes.py`

### 🔹 Purpose

- Chart styling এবং theme system শেখা
- layout customization বোঝা

### 🧾 Code

```python
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales.csv")

fig = px.bar(
    df,
    x="day",
    y="sales",
    color="region",
    title="Sales by Day (Styled)"
)

fig.update_layout(
    template="plotly_dark",
    title="Styled Sales Chart",
    xaxis_title="Day of Week",
    yaxis_title="Sales",
    font=dict(size=14)
)

fig.show()
```

### 🧠 Explanation

- `px.bar()` → bar chart তৈরি করে
- `color="region"` → region অনুযায়ী color separation
- `update_layout()` → chart design modify করে
- `template="plotly_dark"` → dark theme apply করে
- Logic → data visualization + styling improvement

---

## 📄 4. `4_interactive_features.py`

### 🔹 Purpose

- Plotly-এর interactivity feature explore করা
- hover, zoom, pan behavior বোঝা

### 🧾 Code

```python
import pandas as pd
import plotly.express as px

df = pd.read_csv("sales.csv")

fig = px.scatter(
    df,
    x="sales",
    y="profit",
    color="region",
    size="sales",
    hover_data=["day", "region"],
    title="Sales vs Profit (Interactive)"
)

fig.update_traces(
    hovertemplate=
    "Sales: %{x}<br>" +
    "Profit: %{y}<br>" +
    "<extra></extra>"
)

fig.show()
```

### 🧠 Explanation

- `px.scatter()` → scatter plot তৈরি করে
- `color="region"` → category-based coloring
- `size="sales"` → bubble size dynamic
- `hover_data` → extra info hover এ দেখায়
- `update_traces()` → hover design customize করে
- Logic → fully interactive data exploration

---

## ⚙️ Implementation Flow

- Data load করা হয়েছে
- Plotly Express দিয়ে quick chart তৈরি করা হয়েছে
- Graph Objects দিয়ে manual chart build করা হয়েছে
- Layout এবং theme customize করা হয়েছে
- Interactive features (hover, zoom, pan) explore করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Plotly Express দ্রুত visualization তৈরি করতে সাহায্য করে
- Graph Objects দিয়ে full control পাওয়া যায়
- Layout system দিয়ে chart professional look দেওয়া যায়
- Hover + zoom + pan Plotly-এর main power

---

## 🚀 What I Learned

- Plotly Express vs Graph Objects difference
- Interactive chart কিভাবে কাজ করে
- Layout customization system
- Hover tooltip customization
- Data visualization exploration workflow

---

## 🧠 Key Concepts (Quick Revision)

- `px` = high-level easy API
- `go` = low-level full control API
- `fig.show()` = interactive output render করে
- Layout = chart design system
- Hover = data insight tool
- Zoom/Pan = built-in interactivity

---

## 📝 Notes

- Graph Objects beginners এর জন্য একটু complex হতে পারে
- Plotly charts browser-based তাই internet/browser rendering লাগে
- Dataset path ভুল হলে `FileNotFoundError` আসতে পারে

---

## 📌 Next Day Preview

- আগামী দিনে Line Plot deep dive করা হবে
- Multiple lines, markers, trend analysis শেখা হবে
- Time-series visualization শুরু হবে

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Dark/light theme toggle add করা
- More interactive filters যোগ করা
- Region-based dashboard বানানো

### 🧪 Practice Ideas

- sales vs profit bubble chart নিজে বানাও
- region-wise bar chart customize করো
- hover template নিজের মতো modify করো
