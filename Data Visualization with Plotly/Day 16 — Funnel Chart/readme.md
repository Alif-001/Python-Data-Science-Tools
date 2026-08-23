# 📅 Day 16 — Funnel Chart (`px.funnel()`)

---

## 🎯 Objective

- আজকে আমরা শিখবো কীভাবে **step-by-step process flow visualize করা যায়**
- বুঝবো কোথায় users/customers drop off করছে
- conversion tracking করা
- sales / marketing funnel analysis করা

---

## 📚 Topics Covered

- `px.funnel()`
- Sales funnel visualization
- Conversion tracking
- Process analysis
- User journey understanding
- Drop-off detection
- Business pipeline analysis

---

## 📁 Project Structure

```text id="fn16p1"
Day 16 — Funnel Chart/
│
├── 1_basic_funnel.py
├── 2_conversion_tracking.py
├── 3_sales_funnel_analysis.py
├── 4_process_analysis.py
└── funnel_data.csv
```

---

## 📊 Dataset

**File Name:** `funnel_data.csv`

**Description:**
User journey / marketing funnel dataset showing how users move through different stages.

**Columns:**

- stage → funnel এর বিভিন্ন ধাপ (Visitors → Paid Users)
- value → প্রতিটি stage এ কতজন user আছে

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_funnel.py`

### 🔹 Purpose

- basic funnel chart তৈরি করা
- user journey visualize করা

### 🧾 Code

```python id="fn16c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("funnel_data.csv")

fig = px.funnel(
    df,
    x="value",
    y="stage",
    title="Basic Funnel Chart"
)

fig.show()
```

---

### 🧠 Explanation

- `pd.read_csv()` → dataset load করে
- `px.funnel()` → funnel visualization তৈরি করে
- `x="value"` → count/quantity দেখায়
- `y="stage"` → process steps দেখায়

👉 Logic:

- top stage = highest users
- bottom stage = final conversion
- প্রতিটি step এ drop-off দেখা যায়

---

## 📄 2. `2_conversion_tracking.py`

### 🔹 Purpose

- conversion rate calculate করা
- user drop-off analysis করা

### 🧾 Code

```python id="fn16c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("funnel_data.csv")

df["conversion_rate"] = df["value"] / df["value"].iloc[0] * 100

print(df)

fig = px.funnel(
    df,
    x="value",
    y="stage",
    title="Conversion Funnel Tracking"
)

fig.show()
```

---

### 🧠 Explanation

- প্রথম stage (Visitors) কে base ধরা হয়
- `conversion_rate` → কত % user পরের stage এ যাচ্ছে

👉 Logic:

- 100% → Visitors
- এরপর gradually decrease হয়
- কোথায় drop হচ্ছে সেটা identify করা যায়

---

## 📄 3. `3_sales_funnel_analysis.py`

### 🔹 Purpose

- sales funnel analyze করা
- color intensity দিয়ে performance দেখা

### 🧾 Code

```python id="fn16c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("funnel_data.csv")

fig = px.funnel(
    df,
    x="value",
    y="stage",
    color="value",
    title="Sales Funnel Analysis"
)

fig.show()
```

---

### 🧠 Explanation

- `color="value"` → stage অনুযায়ী intensity দেখায়
- high value stages visually highlight হয়

👉 Logic:

- strong stage = high value
- weak stage = drop-off point

---

## 📄 4. `4_process_analysis.py`

### 🔹 Purpose

- user journey / process flow analyze করা
- funnel structure optimize করা

### 🧾 Code

```python id="fn16c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("funnel_data.csv")

fig = px.funnel(
    df,
    x="value",
    y="stage",
    title="Process Flow Analysis (User Journey)"
)

fig.update_layout(
    yaxis_title="Stages of Process"
)

fig.show()
```

---

### 🧠 Explanation

- `update_layout()` → chart readability improve করে
- process flow clear করা হয়

👉 Logic:

- user journey step-by-step visualize করা হয়
- bottleneck easily detect করা যায়

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- funnel stages define করা হয়েছে
- user count visualize করা হয়েছে
- conversion rate calculate করা হয়েছে
- drop-off points identify করা হয়েছে
- process flow analyze করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- Visitors থেকে Signups এ বড় drop-off হয়
- Paid Users এ conversion কমে যায়
- Premium Users সবচেয়ে ছোট segment
- funnel এর নিচে গেলে user সংখ্যা কমে যায়

---

## 🚀 What I Learned

- Funnel chart process flow বুঝতে সাহায্য করে
- conversion rate business performance measure করে
- কোথায় user drop করছে সেটা easily detect করা যায়
- marketing optimization এ খুব important tool

---

## 🧠 Key Concepts (Quick Revision)

- Funnel Chart → step-by-step flow visualization
- Conversion Rate → stage transition percentage
- Drop-off → user loss between stages
- Bottleneck → weak stage in process
- User Journey → full pipeline analysis

---

## 📝 Notes

- proper order maintain না করলে chart ভুল দেখাবে
- small dataset এ funnel less meaningful হতে পারে
- real data না হলে analysis misleading হতে পারে

---

## 📌 Next Day Preview

আগামী দিনে আমরা শিখবো:

- 📊 Timeline Chart (`px.timeline()`)
- project scheduling visualization
- Gantt chart basics
- task tracking system

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- real SaaS product funnel dataset ব্যবহার করো
- A/B testing funnel compare করো
- time-based funnel analysis add করো

---

### 🧪 Practice Ideas

- নতুন stage add করো (Trial Users)
- biggest drop-off stage identify করো
- reverse funnel order observe করো
- conversion rate manually calculate করো
