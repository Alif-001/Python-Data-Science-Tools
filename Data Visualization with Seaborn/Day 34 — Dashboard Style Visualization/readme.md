# 📅 Day 34 — Dashboard Style Visualization (Seaborn + Business Storytelling)

---

# 🎯 Objective

- Multiple plots একসাথে একটি dashboard আকারে তৈরি করা
- Business KPI (Sales, Profit, Customers, Ads) visualize করা
- Trend analysis + comparison একসাথে করা
- Professional data storytelling layout বানানো
- Portfolio-ready dashboard design করা
- Seaborn + Matplotlib integration ব্যবহার করা

---

# 📚 Topics Covered

- Multi-panel dashboard design (`subplots`)
- Sales trend analysis
- Profit trend analysis
- Customer growth tracking
- Region-wise performance analysis
- Ad spend analysis
- KPI visualization
- Scatter + line + bar combination plots
- Insight storytelling with annotations
- Portfolio-ready dashboard creation

---

# 📁 Dataset

## 📌 File Name: `dashboard_data.csv`

## 📌 Description

একটি business analytics dataset যেখানে monthly performance, region-wise sales, profit, customer growth এবং ad spending track করা হয়েছে।

## 📌 Columns

- `month` → time period (Jan–Oct)
- `region` → business region
- `sales` → total sales
- `profit` → total profit
- `customers` → customer count
- `ads` → advertising budget

---

# 📁 Project Structure

```bash id="dash34_structure"
day-34/
│── dashboard_data.csv
│── 01_basic_dashboard_layout.py
│── 02_multi_kpi_dashboard.py
│── 03_storytelling_dashboard.py
│── 04_advanced_dashboard_style.py
│── 05_insight_highlight_dashboard.py
│── 06_full_business_dashboard.py
│── 07_portfolio_ready_dashboard.py
│── README.md
```

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_dashboard_layout.py

## 🔹 Purpose

- Simple 2-panel dashboard তৈরি করা

## 🧾 Code

```python id="d34_1"
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.lineplot(data=df, x="month", y="sales", ax=axes[0])
sns.lineplot(data=df, x="month", y="profit", ax=axes[1])
```

## 🧠 Explanation

- `subplots()` → multiple charts একসাথে দেখায়
- Sales vs Profit trend compare করা হয়

---

# 📄 2. 02_multi_kpi_dashboard.py

## 🔹 Purpose

- KPI comparison dashboard তৈরি করা

## 🧾 Code

```python id="d34_2"
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.barplot(data=df, x="region", y="sales", ax=axes[0])
sns.barplot(data=df, x="region", y="profit", ax=axes[1])
sns.barplot(data=df, x="region", y="customers", ax=axes[2])
```

## 🧠 Explanation

- Region-wise business performance compare করা হয়
- KPI = Sales + Profit + Customers

---

# 📄 3. 03_storytelling_dashboard.py

## 🔹 Purpose

- Data storytelling dashboard তৈরি করা

## 🧾 Code

```python id="d34_3"
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

sns.lineplot(data=df, x="month", y="sales", ax=axes[0,0])
sns.lineplot(data=df, x="month", y="profit", ax=axes[0,1])
sns.barplot(data=df, x="region", y="sales", ax=axes[1,0])
sns.lineplot(data=df, x="month", y="customers", ax=axes[1,1])
```

## 🧠 Explanation

- Sales → Profit → Region → Customers
- Full business story flow তৈরি করা হয়

---

# 📄 4. 04_advanced_dashboard_style.py

## 🔹 Purpose

- Professional styled dashboard তৈরি করা

## 🧾 Code

```python id="d34_4"
plt.style.use("ggplot")
```

## 🧠 Explanation

- Clean + professional visualization style
- Presentation-ready output

---

# 📄 5. 05_insight_highlight_dashboard.py

## 🔹 Purpose

- Insight highlight করা

## 🧾 Code

```python id="d34_5"
axes[1].text(3, 80, "Fast Growth Period", color="red")
```

## 🧠 Explanation

- Important insights visually highlight করা হয়
- Storytelling আরও powerful হয়

---

# 📄 6. 06_full_business_dashboard.py

## 🔹 Purpose

- Complete business intelligence dashboard

## 🧾 Code

```python id="d34_6"
fig, axes = plt.subplots(2, 3, figsize=(16, 8))
```

## 🧠 Explanation

- Sales, Profit, Customers, Ads, Region, Relationships একসাথে
- Executive-level dashboard তৈরি হয়

---

# 📄 7. 07_portfolio_ready_dashboard.py

## 🔹 Purpose

- Portfolio-ready clean dashboard তৈরি করা

## 🧾 Code

```python id="d34_7"
sns.lineplot(data=df, x="month", y="sales")
sns.barplot(data=df, x="region", y="sales")
```

## 🧠 Explanation

- Simple + clean visualization
- Interview/portfolio presentation ready

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- KPI metrics visualize করা হয়েছে
- Region-wise performance compare করা হয়েছে
- Trend analysis করা হয়েছে
- Multi-panel dashboard তৈরি করা হয়েছে
- Insight highlight করা হয়েছে
- Final business dashboard তৈরি করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Sales and profit steady growth দেখায়
- Region-wise performance different
- Customer growth trend consistent
- Ad spend increases with sales
- Certain months show peak performance

---

# 🚀 What I Learned

- Multi-plot dashboard design
- Business KPI visualization
- Insight-driven storytelling
- Professional chart layout design
- Seaborn + Matplotlib integration
- Portfolio-level presentation skills

---

# 🧠 Key Concepts (Quick Revision)

- Dashboard = multiple charts in one view
- KPI = business performance indicator
- `subplots()` → layout system
- Lineplot → trend analysis
- Barplot → comparison
- Scatterplot → relationship
- Storytelling = insight-driven visualization

---

# 📝 Notes

## 📌 Common Mistakes

- Too many plots → cluttered dashboard
- No title hierarchy
- No insight explanation
- Axis labels ignore করা

## 📌 Optimization Tips

- Always group related metrics together
- Keep dashboard clean and readable
- Use consistent style across plots
- Highlight key insights visually

---

# 📌 Next Day Preview

## 📅 Day 35 — Final Mastery Revision (Seaborn)

আগামী দিনে শিখবে:

- All Seaborn plots revision
- Best practices summary
- Plot selection strategy
- Common mistakes checklist
- Portfolio project ideas

---

# ⭐ Bonus

## 🔥 Improvement Ideas

- Interactive dashboard (Plotly upgrade)
- Real-world business dataset apply করা
- KPI auto-report generator বানানো

---

## 🧪 Practice Ideas

- sales vs ads relationship analyze করো
- best performing region identify করো
- customer growth vs profit compare করো
