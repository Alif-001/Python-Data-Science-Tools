# 📅 Day 31 — Dashboard with Plotly

---

## 🎯 Objective

- আজকে আমরা শিখবো কিভাবে **real business dashboard তৈরি করা যায়**
- KPI (Key Performance Indicators) বানানো
- Multiple charts একসাথে dashboard আকারে দেখানো
- CEO-level reporting style visualization তৈরি করা
- Business performance analysis করা (sales, profit, expenses, customers)

---

## 📚 Topics Covered

- KPI Cards using `go.Indicator()`
- Multi-chart dashboard using `make_subplots()`
- Business metrics visualization
- Executive dashboard design
- Line + Bar chart combination in one layout

---

## 📁 Project Structure

```text
Day 31 — Dashboard with Plotly/
│── 1_kpi_cards.py
│── 2_multi_chart_dashboard.py
│── 3_business_dashboard.py
│── business_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** business_data.csv
- **Description:** Monthly business performance dataset (sales, profit, expenses, customers)

### Columns:

- month → মাস (Jan–Dec)
- sales → মোট বিক্রি
- profit → মোট লাভ
- expenses → মোট খরচ
- customers → মোট গ্রাহক সংখ্যা

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. kpi_cards.py

### 🔹 Purpose

- ব্যবসার total performance দেখানোর জন্য KPI cards তৈরি করা
- CEO dashboard summary বানানো

### 🧾 Code

```python
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("business_data.csv")

total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
total_expenses = df["expenses"].sum()
total_customers = df["customers"].sum()

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode="number",
    value=total_sales,
    title={"text": "Total Sales"}
))

fig.show()
```

### 🧠 Explanation

- Line 1 → pandas import করা হয়েছে data পড়ার জন্য
- Line 3 → CSV file load করা হয়েছে
- Line 5-8 → total KPI values calculate করা হয়েছে
- Indicator → number-based KPI card তৈরি করে
- Overall → business summary dashboard তৈরি করা হয়েছে

---

## 📄 2. multi_chart_dashboard.py

### 🔹 Purpose

- একসাথে multiple business charts দেখানো
- comparison dashboard তৈরি করা

### 🧾 Code

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("business_data.csv")

fig = make_subplots(rows=2, cols=2)

fig.add_trace(go.Scatter(x=df["month"], y=df["sales"]), row=1, col=1)
fig.add_trace(go.Bar(x=df["month"], y=df["profit"]), row=1, col=2)

fig.show()
```

### 🧠 Explanation

- make_subplots → grid dashboard তৈরি করে
- row/col → কোথায় chart বসবে define করে
- Scatter + Bar → different insights একসাথে দেখায়
- Overall → multi-view analysis system তৈরি হয়

---

## 📄 3. business_dashboard.py

### 🔹 Purpose

- Full professional business dashboard তৈরি করা
- executive-level reporting system বানানো

### 🧾 Code

```python
fig.add_trace(go.Scatter(x=df["month"], y=df["sales"], mode="lines+markers"))
fig.add_trace(go.Bar(x=df["month"], y=df["expenses"]))
```

### 🧠 Explanation

- Line chart → trend analysis দেখায়
- Bar chart → comparison সহজ করে
- Combined dashboard → real company reporting system এর মতো কাজ করে

---

## ⚙️ Implementation Flow

- Data load করা হয়েছে
- KPI calculate করা হয়েছে
- Multiple charts তৈরি করা হয়েছে
- Dashboard layout বানানো হয়েছে
- Final business report visualization তৈরি করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- Total sales yearly performance দেখা যায়
- Profit vs expenses comparison করা যায়
- Customer growth trend বোঝা যায়
- Business performance overview পাওয়া যায়

---

## 🚀 What I Learned

- KPI dashboard কিভাবে বানাতে হয়
- Multi-chart layout design
- Business analytics visualization
- Executive reporting system structure

---

## 🧠 Key Concepts (Quick Revision)

- `go.Indicator()` → KPI cards
- `make_subplots()` → dashboard layout
- `Scatter + Bar` → mixed visualization
- Business dashboard = summary + trends + comparison

---

## 📝 Notes

- KPI cards শুধু numbers show করে, trend না
- Dashboard design clean রাখা খুব important
- Too many charts একসাথে দিলে readability কমে যায়
- Real-world dashboard = simplicity + clarity

---

## 📌 Next Day Preview

- আগামী দিনে শিখবো:
  - Pandas + Plotly integration deeper level
  - Groupby visualization
  - Real EDA workflow
  - Dataset-based storytelling

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- KPI percentage change যোগ করা
- Profit growth rate calculation
- Interactive filters যোগ করা

### 🧪 Practice Ideas

- নিজের university data দিয়ে dashboard বানাও
- Sports data নিয়ে KPI dashboard তৈরি করো
- Monthly expense tracker dashboard বানাও
