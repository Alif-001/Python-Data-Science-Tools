# 📅 Day 32 — Plotly + Pandas Workflow

---

## 🎯 Objective

- আজকে আমরা শিখবো কিভাবে **real-world data analysis workflow (EDA)** করা হয়
- CSV data load করে analysis করা
- Pandas `groupby()` ব্যবহার করে insights বের করা
- Plotly দিয়ে business-level visualization তৈরি করা
- Simple EDA dashboard বানানো

---

## 📚 Topics Covered

- CSV data visualization workflow
- Pandas `groupby()` analysis
- Aggregated data visualization
- EDA (Exploratory Data Analysis) basics
- Dashboard-style charts with Plotly

---

## 📁 Project Structure

```text id="p32s11"
Day 32 — Plotly + Pandas Workflow/
│── 1_csv_visualization.py
│── 2_groupby_analysis.py
│── 3_eda_dashboard.py
│── ecommerce_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** ecommerce_data.csv
- **Description:** E-commerce sales dataset with product, category, region-wise sales and profit data

### Columns:

- order_id → প্রতিটি অর্ডারের ID
- product → পণ্যের নাম
- category → পণ্যের ক্যাটাগরি
- region → বিক্রির অঞ্চল
- sales → মোট বিক্রি
- profit → মোট লাভ

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. csv_visualization.py

### 🔹 Purpose

- CSV file load করা
- basic visualization তৈরি করা
- product-wise sales দেখা

### 🧾 Code

```python id="csv32a"
import pandas as pd
import plotly.express as px

df = pd.read_csv("ecommerce_data.csv")

fig = px.bar(df, x="product", y="sales", color="category")
fig.show()
```

### 🧠 Explanation

- Line 1 → pandas import করা হয়েছে data handling এর জন্য
- Line 3 → CSV file load করা হয়েছে DataFrame হিসেবে
- px.bar → product-wise sales visualization তৈরি করে
- color → category আলাদা করে দেখায়
- Overall → basic EDA শুরু করা হয়েছে

---

## 📄 2. groupby_analysis.py

### 🔹 Purpose

- Pandas groupby দিয়ে data summarize করা
- category-wise total sales বের করা

### 🧾 Code

```python id="grp32b"
category_sales = df.groupby("category")["sales"].sum().reset_index()
```

### 🧠 Explanation

- groupby("category") → category অনুযায়ী data group করে
- ["sales"].sum() → total sales calculate করে
- reset_index() → clean table format দেয়
- Overall → data aggregation করা হয়েছে

---

## 📄 3. eda_dashboard.py

### 🔹 Purpose

- full EDA dashboard তৈরি করা
- multiple insights একসাথে দেখা

### 🧾 Code

```python id="dash32c"
fig.add_trace(go.Bar(x=region_sales["region"], y=region_sales["sales"]))
fig.add_trace(go.Bar(x=category_profit["category"], y=category_profit["profit"]))
```

### 🧠 Explanation

- region_sales → region অনুযায়ী sales analysis
- category_profit → category-wise profit analysis
- add_trace → multiple charts এক dashboard এ দেখায়
- Overall → business insight dashboard তৈরি করা হয়েছে

---

## ⚙️ Implementation Flow

- CSV data load করা হয়েছে
- Data inspection করা হয়েছে
- groupby দিয়ে aggregation করা হয়েছে
- Summary table তৈরি করা হয়েছে
- Plotly দিয়ে visualization করা হয়েছে
- Final EDA dashboard তৈরি করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- কোন category বেশি sales করছে
- কোন region সবচেয়ে strong
- কোন product best performing
- Profit distribution কেমন

---

## 🚀 What I Learned

- CSV data analysis workflow
- Pandas groupby concept
- Aggregated visualization technique
- EDA dashboard building

---

## 🧠 Key Concepts (Quick Revision)

- `pd.read_csv()` → data load
- `groupby()` → data summary
- `reset_index()` → clean table
- Plotly → interactive visualization
- EDA → data understanding process

---

## 📝 Notes

- groupby ছাড়া real analysis possible না
- raw data সবসময় clean না হয়
- visualization ছাড়া insights বোঝা কঠিন
- EDA হলো data science এর first step

---

## 📌 Next Day Preview

- আগামী দিনে শিখবো:
  - NumPy + Plotly integration
  - Mathematical visualization
  - Data simulation techniques
  - Random data modeling

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Profit margin calculation যোগ করা
- Region-wise performance ranking
- Interactive filters যোগ করা

### 🧪 Practice Ideas

- নিজের shop data দিয়ে EDA করো
- YouTube analytics data visualize করো
- School result dataset দিয়ে dashboard বানাও
