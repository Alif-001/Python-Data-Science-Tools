# 📅 Day 36 — Advanced Analytics Dashboard Project

---

## 🎯 Objective

- আজকে শেখার লক্ষ্য হলো একটি **real-world business analytics dashboard** তৈরি করা
- Problem solve করা হচ্ছে:
  - raw CSV data → interactive business insights dashboard এ convert করা
  - static charts → dynamic filtering based dashboard তৈরি করা
  - real e-commerce analytics system simulate করা

---

## 📚 Topics Covered

- Business Analytics Dashboard design
- Sales analytics visualization
- Customer analytics insights
- Interactive filtering (region + category)
- KPI (Key Performance Indicators) calculation
- Dash callback-based dynamic dashboard

---

## 📁 Project Structure

```text id="d36s11"
Day 36 — Advanced Analytics Dashboard Project/
│── app.py
│── data.csv
│── assets/
│   └── style.css
│── README.md
```

---

## 📊 Dataset

- **File Name:** data.csv
- **Description:** E-commerce sales dataset used for business analytics dashboard

### Columns:

- order_id → অর্ডার আইডি
- region → কোন এলাকা থেকে অর্ডার এসেছে
- category → product category (Electronics/Fashion)
- customer → customer name
- sales → total sales value
- profit → profit value

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. app.py

### 🔹 Purpose

- Complete business analytics dashboard তৈরি করা
- Interactive filtering system implement করা
- KPI + charts dynamically update করা

---

### 🧾 Code

```python id="d36s12"
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("📊 Business Analytics Dashboard"),

    html.Div([

        dcc.Dropdown(
            id="region-filter",
            options=[{"label": r, "value": r} for r in df["region"].unique()],
            value="Dhaka",
            clearable=False
        ),

        dcc.Dropdown(
            id="category-filter",
            options=[{"label": c, "value": c} for c in df["category"].unique()],
            value="Electronics",
            clearable=False
        )
    ]),

    html.Br(),

    html.Div(id="kpi-section"),

    html.Br(),

    dcc.Graph(id="sales-chart"),
    dcc.Graph(id="profit-chart")
])

@app.callback(
    [
        Output("kpi-section", "children"),
        Output("sales-chart", "figure"),
        Output("profit-chart", "figure")
    ],
    [
        Input("region-filter", "value"),
        Input("category-filter", "value")
    ]
)
def update_dashboard(region, category):

    filtered_df = df[
        (df["region"] == region) &
        (df["category"] == category)
    ]

    total_sales = filtered_df["sales"].sum()
    total_profit = filtered_df["profit"].sum()
    customers = filtered_df["customer"].nunique()

    kpis = html.Div([
        html.H3(f"Total Sales: {total_sales}"),
        html.H3(f"Total Profit: {total_profit}"),
        html.H3(f"Customers: {customers}")
    ])

    sales_fig = px.bar(filtered_df, x="customer", y="sales", title="Customer Sales")

    profit_fig = px.bar(filtered_df, x="customer", y="profit", title="Customer Profit")

    return kpis, sales_fig, profit_fig

if __name__ == "__main__":
    app.run_server(debug=True)
```

---

### 🧠 Explanation

- Line 1–4 → required libraries import
- Line 6 → CSV data load করা হচ্ছে
- Line 8 → Dash app initialize
- Line 12–38 → UI layout design (filters + charts + KPIs)
- Line 40–72 → callback function (core logic)

**Logic Flow:**

- User filter select করে
- Data filter হয়
- KPI calculate হয়
- Charts update হয়
- UI refresh হয় automatically

---

## 📄 2. assets/style.css

### 🔹 Purpose

- Dashboard UI design improve করা
- KPI cards styling করা

---

### 🧾 Code

```css id="d36s13"
body {
  font-family: Arial;
  background-color: #f5f6fa;
  text-align: center;
}

h1 {
  color: #2c3e50;
}

h3 {
  color: #34495e;
  display: inline-block;
  margin: 10px;
  padding: 10px;
  background: white;
  border-radius: 10px;
  box-shadow: 0px 0px 5px #ccc;
}
```

---

## ⚙️ Implementation Flow

- Data load করা হয়েছে (CSV file)
- Filters তৈরি করা হয়েছে (region + category)
- User input নেওয়া হচ্ছে dropdown থেকে
- Data filtering করা হচ্ছে Pandas দিয়ে
- KPI calculate করা হচ্ছে
- Charts generate করা হচ্ছে Plotly দিয়ে
- Dashboard dynamically update হচ্ছে

---

## 📈 Output / Result

### Key findings:

- Interactive business dashboard তৈরি করা সম্ভব Python দিয়ে
- Real-time filtering system কাজ করে
- KPI + visualization একসাথে দেখানো যায়
- Real-world analytics system simulate করা যায়

---

## 🚀 What I Learned

- Business analytics dashboard design
- Dash callback system deep understanding
- Interactive filtering concept
- KPI calculation techniques
- Real-world E-commerce analytics workflow

---

## 🧠 Key Concepts (Quick Revision)

- Callback = dashboard brain
- Filtering = data slicing technique
- KPI = business performance metrics
- Dash = interactive web app framework

---

## 📝 Notes

- Callback ছাড়া Dash app static হয়
- Pandas filtering is core of analytics
- KPI cards give executive-level insights
- Real dashboards always use filtering + charts together

---

## 📌 Next Day Preview

- আগামী দিনে শিখবো:
- Plotly + NumPy advanced simulation
- Mathematical visualization
- Real-world data modeling techniques

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Date range filter add করা
- Export to CSV feature add করা
- Multi-page dashboard extend করা

### 🧪 Practice Ideas

- Finance dashboard বানাও
- Marketing analytics system design করো
- Customer segmentation dashboard তৈরি করো
