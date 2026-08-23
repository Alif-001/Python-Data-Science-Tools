# 📅 Day 35 — Dash Advanced

---

## 🎯 Objective

- আজকে শেখার লক্ষ্য হলো Dash Framework এর **advanced features** ব্যবহার করা
- Problem solve করা হচ্ছে:
  - single-page dashboard → multi-page web application এ convert করা
  - static dashboard → scalable production-ready system বানানো

---

## 📚 Topics Covered

- Advanced Callbacks (multi-input & multi-output concept)
- Dynamic updates in UI
- Multi-page Dash application
- Page routing system
- Modular dashboard architecture
- Basic dashboard deployment concept

---

## 📁 Project Structure

```text id="d35s13"
Day 35 — Dash Advanced/
│── app.py
│── pages/
│   │── home.py
│   │── sales.py
│   │── profit.py
│── assets/
│   │── style.css
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** data.csv
- **Description:** Monthly business performance dataset (sales, profit, expenses)

### Columns:

- month → মাসের নাম (Jan–Dec)
- sales → মোট বিক্রয়
- profit → মোট লাভ
- expenses → মোট খরচ

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. app.py

### 🔹 Purpose

- Main entry point of Dash application
- Multi-page routing system handle করা

---

### 🧾 Code

```python id="d35s14"
import dash
from dash import html, dcc

app = dash.Dash(__name__, use_pages=True)

app.layout = html.Div([

    html.H1("📊 Advanced Business Dashboard"),

    html.Div([
        dcc.Link("Home", href="/"),
        " | ",
        dcc.Link("Sales", href="/sales"),
        " | ",
        dcc.Link("Profit", href="/profit")
    ]),

    html.Hr(),

    dash.page_container
])

if __name__ == "__main__":
    app.run_server(debug=True)
```

---

### 🧠 Explanation

- Line 1–2 → Dash library import
- Line 4 → multi-page system enable করা হয়েছে
- Line 7 → main layout (UI structure)
- Line 9–13 → navigation links তৈরি করা হয়েছে
- Line 15 → page content dynamically load হয়
- Line 19 → server run করা হচ্ছে

**Logic:**

- App → Navigation → Pages → Dynamic rendering

---

## 📄 2. pages/home.py

### 🔹 Purpose

- Home page তৈরি করা
- User welcome + overview section

---

### 🧾 Code

```python id="d35s15"
import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div([

    html.H2("🏠 Home Dashboard"),

    html.P("Welcome to Advanced Dash Multi-page System"),

    html.Ul([
        html.Li("Sales Analytics"),
        html.Li("Profit Analytics"),
        html.Li("Business Dashboard")
    ])
])
```

---

### 🧠 Explanation

- `register_page()` → page system এ register করে
- `path="/"` → homepage define করে
- `layout` → UI structure define করে

**Logic:**

- Simple landing page → navigation guide

---

## 📄 3. pages/sales.py

### 🔹 Purpose

- Sales data visualization page তৈরি করা

---

### 🧾 Code

```python id="d35s16"
import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

dash.register_page(__name__)

df = pd.read_csv("data.csv")

fig = px.line(df, x="month", y="sales", title="Sales Trend")

layout = html.Div([
    html.H2("📈 Sales Analytics"),
    dcc.Graph(figure=fig)
])
```

---

### 🧠 Explanation

- CSV load করা হচ্ছে
- Sales line chart তৈরি করা হচ্ছে
- Page UI তে graph show করা হচ্ছে

**Logic:**

- Data → Chart → Page output

---

## 📄 4. pages/profit.py

### 🔹 Purpose

- Profit analysis page তৈরি করা

---

### 🧾 Code

```python id="d35s17"
import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

dash.register_page(__name__)

df = pd.read_csv("data.csv")

fig = px.bar(df, x="month", y="profit", title="Profit Analysis")

layout = html.Div([
    html.H2("💰 Profit Analytics"),
    dcc.Graph(figure=fig)
])
```

---

### 🧠 Explanation

- Profit bar chart তৈরি করা হয়েছে
- Each page independentভাবে কাজ করে

**Logic:**

- Modular dashboard system

---

## 📄 5. assets/style.css

### 🔹 Purpose

- Dashboard styling (UI design improve করা)

---

### 🧾 Code

```css id="d35s18"
body {
  font-family: Arial;
  background-color: #f4f4f4;
  text-align: center;
}

h1 {
  color: #2c3e50;
}

h2 {
  color: #34495e;
}
```

---

## ⚙️ Implementation Flow

- Data load করা হয়েছে
- Dash app initialize করা হয়েছে
- Multi-page system enable করা হয়েছে
- Pages তৈরি করা হয়েছে (Home, Sales, Profit)
- Navigation system setup করা হয়েছে
- CSS দিয়ে UI styling করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Multi-page dashboard তৈরি করা সম্ভব Python দিয়ে
- Each page independentভাবে কাজ করে
- Professional web app structure তৈরি করা যায়

---

## 🚀 What I Learned

- Dash multi-page architecture
- Page routing system
- Modular dashboard design
- Web application structure in Python
- UI + data visualization integration

---

## 🧠 Key Concepts (Quick Revision)

- `use_pages=True` → multi-page system enable
- `register_page()` → page define করে
- `page_container` → dynamic page loader
- Modular design → scalable dashboard system

---

## 📝 Notes

- Multi-page system production-level Dash feature
- Each page আলাদা file হলে maintainability বেশি হয়
- Real-world apps এই architecture follow করে

---

## 📌 Next Day Preview

- আগামী দিনে শিখবো:
- Advanced dashboard system (KPI cards + multi charts)
- Business executive level reporting dashboard
- Performance analytics system

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Login system add করা
- API integration করা
- Database connection যোগ করা

### 🧪 Practice Ideas

- Finance dashboard বানাও
- Marketing analytics system design করো
- Admin panel structure তৈরি করো
