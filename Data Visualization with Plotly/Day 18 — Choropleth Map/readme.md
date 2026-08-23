# 📅 Day 18 — Choropleth Map (`Geographic Visualization`)

---

## 🎯 Objective

- আজকে আমরা শিখবো কীভাবে **geographic data visualize** করতে হয়
- দেশভিত্তিক (country-wise) data comparison করা
- কোন দেশে বেশি/কম value আছে তা color দিয়ে বোঝা
- real-world dashboard style map visualization তৈরি করা

---

## 📚 Topics Covered

- `px.choropleth()`
- Geographic visualization basics
- Country-level data mapping
- Color-based intensity analysis
- Color scaling techniques
- Location mode understanding

---

## 📁 Project Structure

```text id="ch18p1"
Day 18 — Choropleth Map/
│
├── 1_basic_choropleth.py
├── 2_country_analysis.py
├── 3_population_visualization.py
├── 4_color_mapping.py
└── country_data.csv
```

---

## 📊 Dataset

**File Name:** `country_data.csv`

**Description:**
Country-level economic and digital usage dataset used for geographic visualization.

**Columns:**

- country → দেশের নাম
- gdp → অর্থনৈতিক শক্তি (GDP)
- mobile_users → মোবাইল ব্যবহারকারী সংখ্যা
- internet_users → ইন্টারনেট ব্যবহারকারী সংখ্যা

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_choropleth.py`

### 🔹 Purpose

- basic choropleth map তৈরি করা
- GDP অনুযায়ী দেশগুলোর comparison দেখা

### 🧾 Code

```python id="ch18c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("country_data.csv")

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="gdp",
    title="World GDP Visualization"
)

fig.show()
```

---

### 🧠 Explanation

- `pd.read_csv()` → dataset load করে
- `locations="country"` → কোন column দেশ represent করছে
- `locationmode="country names"` → country name based mapping
- `color="gdp"` → GDP অনুযায়ী color intensity

👉 Logic:

- বেশি GDP → গাঢ় রঙ
- কম GDP → হালকা রঙ

---

## 📄 2. `2_country_analysis.py`

### 🔹 Purpose

- mobile users based country analysis
- technology adoption compare করা

### 🧾 Code

```python id="ch18c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("country_data.csv")

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="mobile_users",
    title="Mobile Users by Country"
)

fig.show()
```

---

### 🧠 Explanation

- `mobile_users` → country-wise mobile penetration দেখায়
- country অনুযায়ী adoption pattern বোঝা যায়

👉 Insight:

- developing countries → high mobile dependency

---

## 📄 3. `3_population_visualization.py`

### 🔹 Purpose

- internet users distribution visualize করা
- digital connectivity analysis

### 🧾 Code

```python id="ch18c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("country_data.csv")

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="internet_users",
    title="Internet Users by Country"
)

fig.show()
```

---

### 🧠 Explanation

- `internet_users` → digital connectivity বোঝায়
- country-wise digital gap identify করা যায়

👉 Logic:

- বেশি internet users → বেশি digital growth

---

## 📄 4. `4_color_mapping.py`

### 🔹 Purpose

- advanced color styling ব্যবহার করা
- visualization আরও clear ও readable করা

### 🧾 Code

```python id="ch18c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("country_data.csv")

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="gdp",
    color_continuous_scale="Viridis",
    title="GDP Color Mapping (Advanced)"
)

fig.update_layout(
    geo=dict(showframe=False, showcoastlines=True)
)

fig.show()
```

---

### 🧠 Explanation

- `color_continuous_scale="Viridis"` → better visual gradient
- `showcoastlines=True` → map structure clearer
- `showframe=False` → clean look

👉 Logic:

- color gradient → data intensity বুঝায়

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Country-based data select করা হয়েছে
- Choropleth map তৈরি করা হয়েছে
- Different metrics visualize করা হয়েছে
- Color scale apply করা হয়েছে
- Geographic comparison করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- USA সর্বোচ্চ GDP value show করে
- South Asian countries moderate GDP range এ আছে
- mobile users developing countries এ বেশি
- internet usage GDP এর সাথে correlated

---

## 🚀 What I Learned

- geographic visualization data analysis কে powerful করে
- country-level comparison সহজ হয়
- color intensity → value difference বুঝায়
- real-world dashboards এ choropleth widely used

---

## 🧠 Key Concepts (Quick Revision)

- Choropleth Map → country-wise colored visualization
- locationmode → country matching system
- color scale → data intensity representation
- GDP / internet users → comparison metrics

---

## 📝 Notes

- country name অবশ্যই exact match হতে হবে
- wrong name দিলে map render নাও হতে পারে
- color scale selection visualization clarity affect করে

---

## 📌 Next Day Preview

আগামী দিনে আমরা শিখবো:

- 📦 Box Plot (`px.box()`)
- outlier detection
- statistical distribution analysis
- data spread visualization

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- real world dataset (population / COVID data) ব্যবহার করো
- hover information add করো
- multi-metric dashboard বানাও

---

### 🧪 Practice Ideas

- `population` column add করে map বানাও
- `education rate` analyze করো
- different color scales test করো
- Asia vs Europe comparison করো
