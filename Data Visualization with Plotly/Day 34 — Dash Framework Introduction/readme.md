# 📅 Day 34 — Dash Framework Introduction

---

## 🎯 Objective

- আজকে শেখার লক্ষ্য হলো Dash Framework ব্যবহার করে **interactive web dashboard তৈরি করা**
- Python দিয়ে শুধু chart না, বরং **পুরো web app (Power BI-like dashboard)** বানানো শেখা
- Problem solve করা হচ্ছে:
  - static visualization → interactive web application এ convert করা
  - user input অনুযায়ী dynamic chart update করা

---

## 📚 Topics Covered

- Dash Framework কী এবং কেন ব্যবহার করা হয়
- Web dashboard building basics
- Layout design using `html` components
- Interactive charts using `dcc.Graph`
- User controls (Dropdown, Slider)
- Callback system (UI → Python logic connection)

---

## 📁 Project Structure

```text
Day 34 — Dash Framework Introduction/
│── 1_first_dash_app.py
│── 2_interactive_controls.py
│── 3_live_dashboard.py
│── sales_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** sales_data.csv
- **Description:** Monthly sales and profit data used for dashboard visualization

### Columns:

- month → মাসের নাম (Jan, Feb, …)
- sales → মোট বিক্রয় (Sales value)
- profit → লাভ (Profit value)

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. first_dash_app.py

### 🔹 Purpose

- প্রথম Dash web app তৈরি করা
- একটি simple sales chart web page আকারে দেখানো

---

### 🧾 Code

```python
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv("sales_data.csv")

fig = px.line(df, x="month", y="sales", title="Sales Dashboard")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("My First Dash Dashboard"),

    dcc.Graph(
        id="sales-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
```

---

### 🧠 Explanation

- Line 1–4 → লাইব্রেরি import করা হচ্ছে
- Line 6 → CSV data load করা হচ্ছে
- Line 9 → sales line chart তৈরি করা হচ্ছে
- Line 13 → Dash app initialize করা হচ্ছে
- Line 16 → UI layout তৈরি করা হচ্ছে
- Line 18 → webpage title দেখানো হচ্ছে
- Line 20 → graph embed করা হচ্ছে
- Line 25 → server run করা হচ্ছে

**Logic:**

- Data → Chart → Web UI → Browser dashboard

---

## 📄 2. interactive_controls.py

### 🔹 Purpose

- User input (Dropdown) দিয়ে chart dynamically change করা
- Interactive dashboard তৈরি করা

---

### 🧾 Code

```python
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("sales_data.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.H2("Interactive Sales Dashboard"),

    dcc.Dropdown(
        id="metric-dropdown",
        options=[
            {"label": "Sales", "value": "sales"},
            {"label": "Profit", "value": "profit"}
        ],
        value="sales"
    ),

    dcc.Graph(id="graph")
])

@app.callback(
    Output("graph", "figure"),
    Input("metric-dropdown", "value")
)
def update_graph(selected_metric):
    fig = px.line(
        df,
        x="month",
        y=selected_metric,
        title=f"{selected_metric} Over Time"
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
```

---

### 🧠 Explanation

- Dropdown → user select করে (sales / profit)
- Callback function → input গ্রহণ করে chart update করে
- Output → graph automatically update হয়

**Logic:**

- User Input → Python Callback → New Chart → UI Update

---

## 📄 3. live_dashboard.py

### 🔹 Purpose

- Advanced interactive dashboard তৈরি করা
- Dropdown + Slider একসাথে ব্যবহার করা
- Partial data filtering করা

---

### 🧾 Code

```python
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("sales_data.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Business Live Dashboard"),

    dcc.Dropdown(
        id="metric",
        options=[
            {"label": "Sales", "value": "sales"},
            {"label": "Profit", "value": "profit"}
        ],
        value="sales"
    ),

    dcc.Slider(
        id="range-slider",
        min=0,
        max=len(df)-1,
        value=len(df),
        marks={i: df["month"][i] for i in range(len(df))},
        step=1
    ),

    dcc.Graph(id="live-graph")
])

@app.callback(
    Output("live-graph", "figure"),
    Input("metric", "value"),
    Input("range-slider", "value")
)
def update_chart(metric, slider_value):
    filtered_df = df.iloc[:slider_value]

    fig = px.line(
        filtered_df,
        x="month",
        y=metric,
        title="Live Dashboard Simulation"
    )

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
```

---

### 🧠 Explanation

- Dropdown → metric select করে
- Slider → data range control করে
- Callback → দুই input একসাথে কাজ করে
- Chart → dynamically update হয়

**Logic:**

- Multi Input → Filter Data → Update Chart → Live UI

---

## ⚙️ Implementation Flow

- Data load করা হয়েছে
- Plotly chart তৈরি করা হয়েছে
- Dash layout তৈরি করা হয়েছে
- User controls যোগ করা হয়েছে (dropdown, slider)
- Callback দিয়ে dynamic update করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Interactive web dashboard তৈরি করা যায় Python দিয়ে
- User input অনুযায়ী chart change হয়
- Real-time UI behavior simulate করা যায়

---

## 🚀 What I Learned

- Dash framework basics
- Web dashboard development concept
- Callback system (core concept of Dash)
- Interactive data visualization
- UI + Python integration

---

## 🧠 Key Concepts (Quick Revision)

- Dash = Python web app framework
- `html.Div` → page structure
- `dcc.Graph` → chart container
- Callback → input-output connection
- Interactive dashboard = dynamic visualization system

---

## 📝 Notes

- Callback is the most important part of Dash
- Without callback → dashboard is static
- Slider + dropdown → real-world dashboard behavior simulate করে

---

## 📌 Next Day Preview

- আগামী দিনে শিখবো:
- Multi-chart dashboard system
- KPI cards design
- Business executive dashboard layout

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Add multiple charts in one page
- Add real-time refresh system
- Add database connection

### 🧪 Practice Ideas

- Sales vs Profit comparison dashboard বানাও
- Different metrics switch system তৈরি করো
- Finance dashboard design try করো
