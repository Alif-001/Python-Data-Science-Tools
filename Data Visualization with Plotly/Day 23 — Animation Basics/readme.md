# 📅 Day 23 — Animation Basics

---

## 🎯 Objective

- আজকে শিখার লক্ষ্য animation-based data visualization বোঝা
- time অনুযায়ী data পরিবর্তন visually দেখানো
- dynamic charts তৈরি করা (moving visualization)
- business growth & trend analysis শেখা

---

## 📚 Topics Covered

- animation_frame in Plotly
- animated scatter plot
- animated bar chart
- time-based visualization
- storytelling with data

---

## 📁 Project Structure

```text id="an23s1"
Day 23 — Animation Basics/
│── main.py
│── analysis.py
│── utils.py
│── yearly_sales.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** yearly_sales.csv
- **Description:** Different countries’ sales and profit data across multiple years (used for animation)

### Columns:

- year → time period (frame of animation)
- country → country name
- sales → total sales value
- profit → profit value

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py

### 🔹 Purpose

- basic animated scatter plot তৈরি করা
- year অনুযায়ী sales vs profit movement দেখানো

### 🧾 Code

```python id="code23m1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("yearly_sales.csv")

fig = px.scatter(
    df,
    x="sales",
    y="profit",
    animation_frame="year",
    hover_name="country",
    title="Animated Sales vs Profit"
)

fig.show()
```

### 🧠 Explanation

- pandas → dataset load করার জন্য
- plotly → visualization তৈরি করার জন্য
- animation_frame="year" → প্রতিটি year আলাদা frame তৈরি করে
- Logic → time অনুযায়ী data movement দেখানো হয়

---

## 📄 2. analysis.py

### 🔹 Purpose

- sales & profit growth analysis করা
- country-wise performance check করা

### 🧾 Code

```python id="code23a1"
import pandas as pd

df = pd.read_csv("yearly_sales.csv")

print(df.groupby("country")[["sales", "profit"]].mean())
```

### 🧠 Explanation

- groupby(country) → দেশ অনুযায়ী data ভাগ করা
- mean() → average performance বের করা
- Logic → কোন country better perform করছে বোঝা

---

## 📄 3. utils.py (if any)

### 🔹 Purpose

- helper function তৈরি করা (growth calculation)

### 🧾 Code

```python id="code23u1"
def growth_rate(current, previous):
    return ((current - previous) / previous) * 100
```

### 🧠 Explanation

- growth rate calculate করা
- reusable function for time series analysis

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- country-wise analysis করা হয়েছে
- animated scatter plot তৈরি করা হয়েছে
- time-based movement visualize করা হয়েছে
- growth pattern observe করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- USA সবসময় highest sales & profit ধরে রেখেছে
- India steady growth দেখিয়েছে
- Bangladesh gradually growth করছে
- sales বাড়লে profit ও সাধারণত বাড়ে

---

## 🚀 What I Learned

- animation_frame concept
- time-based visualization
- dynamic storytelling with charts
- business trend analysis using animation

---

## 🧠 Key Concepts (Quick Revision)

- animation_frame → time-based movement তৈরি করে
- scatter animation → changing relationship over time
- bar animation → ranking changes দেখায়
- storytelling → data কে motion দিয়ে বোঝানো

---

## 📝 Notes

- বেশি data দিলে animation slow হতে পারে
- clean dataset animation ভালো করে
- proper grouping খুব গুরুত্বপূর্ণ

---

## 📌 Next Day Preview

- আগামী দিনে শিখবো **Advanced Hover Customization**
- professional dashboard-level tooltips তৈরি করা
- interactive UX improvement in charts

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- profit vs sales ratio add করা
- extra year (2024+) যোগ করা
- color based on profit margin

### 🧪 Practice Ideas

- animation_frame="country" try করো
- profit based sorting করো
- fastest growing country বের করো
