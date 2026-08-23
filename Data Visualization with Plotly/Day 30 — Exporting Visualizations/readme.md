# 📅 Day 30 — Exporting Visualizations

---

🎯 Objective

- আজকে শিখার লক্ষ্য:
  - Plotly visualization বিভিন্ন format-এ export করা
  - Interactive dashboard share করা
  - Professional report তৈরি করা (HTML / PNG / PDF)

- কোন problem solve করা হচ্ছে:
  - শুধু chart তৈরি করা নয় → এখন সেটাকে real-world use (sharing + reporting) এ convert করা
  - Dashboard কে browser, report, presentation—সব জায়গায় ব্যবহারযোগ্য করা

---

📚 Topics Covered

- Save Plotly figure as HTML
- Export visualization as PNG image
- Export report as PDF
- Multi-format dashboard export workflow
- Sharing interactive dashboards

---

```
📁 Project Structure

Day 30 — Exporting Visualizations /
│── main.py
│── analysis.py
│── utils.py
│── export_data.csv
│── README.md
```

---

📊 Dataset

- File Name: export_data.csv

- Description:
  Monthly sales and profit dataset used for dashboard export practice

- Columns:
  - month → month name (Jan–Dec)
  - sales → monthly sales value
  - profit → monthly profit value

---

💻 Code Breakdown (File by File)

---

📄 1. main.py

🔹 Purpose

- Plotly chart তৈরি করা এবং different format-এ export করা

🧾 Code

```python id="exp30_main"
fig.write_html("dashboard.html")
fig.write_image("dashboard.png")
fig.write_image("dashboard.pdf")
```

🧠 Explanation

- Line 1 → interactive HTML dashboard save করা হচ্ছে
- Line 2 → PNG image হিসেবে export করা হচ্ছে
- Line 3 → PDF report তৈরি করা হচ্ছে
- Logic → একই chart থেকে multiple output generate করা হচ্ছে

---

📄 2. analysis.py

🔹 Purpose

- dataset analysis করে meaningful insights বের করা

🧾 Code

```python id="exp30_analysis"
summary = df.describe()
trend = df["sales"].pct_change()
```

🧠 Explanation

- step 1 → dataset summary statistics বের করা
- step 2 → sales growth trend calculate করা
- step 3 → report-ready insights তৈরি করা

---

📄 3. utils.py

🔹 Purpose

- helper functions for exporting and formatting

🧾 Code

```python id="exp30_utils"
def clean_data(df):
    return df.dropna()
```

🧠 Explanation

- reusable function তৈরি করা হয়েছে
- missing values clean করা হয়
- export-ready dataset নিশ্চিত করা হয়

---

⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Data clean ও prepare করা হয়েছে
- Plotly chart তৈরি করা হয়েছে
- Chart visualize করা হয়েছে
- HTML / PNG / PDF format-এ export করা হয়েছে

---

📈 Output / Result

- Key findings:
  - Interactive dashboard তৈরি করা সম্ভব HTML দিয়ে
  - PNG format presentation slide এ ব্যবহার করা যায়
  - PDF format business report এর জন্য best
  - One visualization → multiple outputs generate করা যায়

---

🚀 What I Learned

- Plotly visualization export system কীভাবে কাজ করে
- Interactive vs static output পার্থক্য
- Real-world reporting workflow
- Dashboard sharing concept

---

🧠 Key Concepts (Quick Revision)

- HTML Export:
  - interactive dashboard (browser-based)

- PNG Export:
  - static image (presentation-ready)

- PDF Export:
  - printable business report

- Multi-format Export:
  - এক chart → multiple output

---

📝 Notes

- Mistake / Challenge:
  - PNG/PDF export করতে extra dependency লাগতে পারে (kaleido)
  - Large dataset export করলে performance slow হতে পারে

- Optimization Tips:
  - filtered dataset export করা
  - unnecessary traces কমানো
  - lightweight charts ব্যবহার করা

---

📌 Next Day Preview

- এই 30 দিনের শেষে তুমি শিখেছো:
  - Plotly basic → advanced visualization
  - dashboard design
  - animation + real-time system
  - Graph Objects mastery
  - export + sharing pipeline

---

⭐ Bonus (Optional)

🔥 Improvements Ideas

- Auto report generation system বানানো
- Daily email dashboard send করা
- Web-based analytics platform তৈরি করা

🧪 Practice Ideas

- sales report generator tool বানাও
- stock market dashboard export system বানাও
- automated PDF reporting script বানাও
