# 📅 Day 31 — Dashboard Project

🎯 Objective

- আজকে আমরা শিখবো কিভাবে professional dashboard তৈরি করা হয়
- একাধিক charts একসাথে দেখানোর layout (multi-panel visualization) শিখবো
- KPI (Key Performance Indicator) based reporting system তৈরি করা শিখবো
- Real-world business dashboard design বুঝবো

---

📚 Topics Covered

- Multi-plot dashboard layout
- KPI (Key Performance Indicator) visualization
- Professional subplot design
- Text-based dashboard
- Clean modern analytics UI
- CSV-based real dashboard system

---

📁 Project Structure

- day-31/
  - 01_simple_dashboard_layout.py
  - 02_kpi_dashboard.py
  - 03_professional_dashboard_layout.py
  - 04_kpi_with_charts_dashboard.py
  - 05_clean_dashboard_style.py
  - 06_real_dashboard_from_csv.py
  - dashboard_sales_data.csv
  - README.md

---

📊 Dataset

**File Name:** dashboard_sales_data.csv

**Description:**
Business performance dataset used to build a multi-panel dashboard showing sales, profit, and customer trends.

**Columns:**

- column1 → day (time index)
- column2 → sales (daily sales)
- column3 → profit (daily profit)
- column4 → customers (daily customer count)

---

💻 Code Breakdown (File by File)

---

📄 1. main.py — Simple Dashboard Layout

🔹 Purpose

- একসাথে multiple charts (line + bar) দেখানো

🧾 Code

```python
plt.subplot(2, 2, 1)
plt.plot(days, sales)
```

🧠 Explanation

- subplot ব্যবহার করে grid তৈরি করা হয়েছে
- sales trend line chart
- profit trend analysis
- bar chart দিয়ে comparison visualization

---

📄 2. analysis.py — KPI Dashboard

🔹 Purpose

- business KPI values calculate এবং display করা

🧾 Code

```python
total_sales = np.sum(sales)
avg_profit = np.mean(profit)
```

🧠 Explanation

- total sales বের করা হয়েছে
- average profit calculate করা হয়েছে
- text-based dashboard তৈরি করা হয়েছে
- axes hide করে clean UI বানানো হয়েছে

---

📄 3. utils.py — Professional Layout Dashboard

🔹 Purpose

- clean professional subplot design তৈরি করা

🧾 Code

```python
axes[0, 0].plot(days, sales)
axes[0, 1].bar(days, sales)
```

🧠 Explanation

- fig + axes ব্যবহার করা হয়েছে
- structured grid layout
- production-ready dashboard style

---

⚙️ Implementation Flow

- Dataset load করা হয়েছে (CSV বা NumPy)
- KPI values calculate করা হয়েছে
- multiple charts তৈরি করা হয়েছে
- subplot grid layout design করা হয়েছে
- dashboard render করা হয়েছে

---

📈 Output / Result

Key findings:

- একসাথে multiple metrics visualize করা যায়
- KPI dashboard business insight দেয়
- CSV data থেকে full dashboard বানানো সম্ভব
- professional analytics UI তৈরি করা যায়

---

🚀 What I Learned

- dashboard design fundamentals
- subplot vs axes difference
- KPI-based visualization concept
- real-world business reporting system

---

🧠 Key Concepts (Quick Revision)

- `subplot()` → multiple chart layout
- `axes[]` → advanced control over plots
- KPI → key business metric
- `plt.text()` → dashboard labels
- `tight_layout()` → spacing fix

---

📝 Notes

- dashboard design এ consistency খুব গুরুত্বপূর্ণ
- KPI panel সাধারণত text-only হয়
- clean UI = less clutter + more insight
- real dashboards এ interactivity add করা হয়

---

📌 Next Day Preview

- Final capstone visualization project
- full analytics dashboard system
- real-world portfolio project
- interactive visualization introduction

---

⭐ Bonus (Optional)

🔥 Improvements Ideas

- interactive dashboard (Plotly/Dash) বানানো
- real-time data update system
- auto-report generator

🧪 Practice Ideas

- sales monitoring dashboard বানাও
- student performance dashboard তৈরি করো
- stock market analytics dashboard try করো
