# 📅 Day 24 — Advanced Hover Customization

---

# 🎯 Objective

- আজকে শিখার লক্ষ্য হলো interactive charts-এ **hover (tooltip) customization** করা
- কীভাবে chart-এর উপর mouse রাখলে সুন্দরভাবে তথ্য দেখানো যায় তা শেখা
- problem solve করা হচ্ছে: **default tooltip limited information দেয় → সেটাকে professional & readable বানানো**

---

# 📚 Topics Covered

- Hover basics in Plotly
- Custom hover data (hover_data)
- Hover template (hovertemplate)
- Tooltip formatting & styling

---

# 📁 Project Structure

```text
Day 24 — Advanced Hover Customization/
│── main.py
│── analysis.py
│── utils.py
│── data.csv
│── README.md
```

---

# 📊 Dataset

- File Name: `company_sales.csv`
- Description: Company sales, profit, and employee data over years

### Columns:

- company → Company name
- year → Year of record
- sales → Total sales (in millions)
- profit → Total profit (in millions)
- employees → Number of employees

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. main.py

### 🔹 Purpose

- Basic scatter plot তৈরি করা
- hover information দেখানো

### 🧾 Code

```python
import pandas as pd
import plotly.express as px

df = pd.read_csv("company_sales.csv")

fig = px.scatter(
    df,
    x="sales",
    y="profit",
    hover_name="company",
    title="Basic Hover Information"
)

fig.show()
```

### 🧠 Explanation

- Line 1 → pandas import করা হয়েছে data handle করার জন্য
- Line 2 → Plotly Express import করা হয়েছে visualization এর জন্য
- Line 4 → CSV file load করা হয়েছে
- Line 6 → scatter plot তৈরি করা হয়েছে
- Line 9 → company name hover-এ দেখানো হচ্ছে
- Overall → basic interactive chart তৈরি হচ্ছে

---

## 📄 2. analysis.py

### 🔹 Purpose

- extra hover data যোগ করে analysis করা
- company performance বোঝা

### 🧾 Code

```python
fig = px.scatter(
    df,
    x="sales",
    y="profit",
    hover_name="company",
    hover_data=["year", "employees"],
    title="Custom Hover Data Example"
)

fig.show()
```

### 🧠 Explanation

- hover_data → extra details show করে
- year → কোন বছরের data সেটা বোঝায়
- employees → company size বোঝায়
- overall → richer tooltip তৈরি হয়

---

## 📄 3. utils.py (if any)

### 🔹 Purpose

- reusable formatting logic (hover design ideas)

### 🧾 Code

```python
# hover formatting helper ideas

def format_value(value):
    return f"{value:,}"
```

### 🧠 Explanation

- reusable function তৈরি করা হয়েছে
- number readable format-এ convert করে
- large number সহজে বোঝা যায়

---

# ⚙️ Implementation Flow

- Data load করা হয়েছে
- Basic scatter plot তৈরি করা হয়েছে
- Hover customization যোগ করা হয়েছে
- Tooltip format improve করা হয়েছে
- Final interactive dashboard তৈরি করা হয়েছে

---

# 📈 Output / Result

### Key findings:

- company-wise sales vs profit comparison পাওয়া গেছে
- employee size অনুযায়ী company strength বোঝা গেছে
- hover info থেকে extra business insight পাওয়া গেছে

---

# 🚀 What I Learned

- hover customization কিভাবে কাজ করে
- interactive dashboard design basics
- data presentation আরও readable করা

---

# 🧠 Key Concepts (Quick Revision)

- hover_name → main label
- hover_data → extra information
- hovertemplate → full control of tooltip
- formatting → readable number display

---

# 📝 Notes

- default hover অনেক limited
- too much data দিলে tooltip messy হয়ে যায়
- balance রাখা খুব important (clean + informative)

---

# 📌 Next Day Preview

- আগামী দিনে শিখবো:
  - Advanced dashboard layout
  - Multi-chart interaction
  - Subplots & combined visuals

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- hover-এ percentage growth add করা
- profit margin calculate করা
- best company highlight করা

## 🧪 Practice Ideas

- stock market style tooltip design করা
- sales dashboard UI design করা
- company ranking hover-এ দেখানো
