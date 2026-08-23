# 📅 Day 19 — Scatter Geo Map (`px.scatter_geo()`)

---

## 🎯 Objective

- আজকে আমরা শিখবো কীভাবে **real-world map visualization** করা যায়
- city-level data world map-এ দেখানো
- bubble size ও color দিয়ে multi-variable analysis করা
- geographic insights বের করা

---

## 📚 Topics Covered

- `px.scatter_geo()`
- Geographic scatter visualization
- Bubble map concept
- Latitude & Longitude usage
- Multi-variable mapping (size + color)
- World map data analysis

---

## 📁 Project Structure

```text id="sg19p1"
Day 19 — Scatter Geo Map/
│
├── 1_basic_scatter_geo.py
├── 2_bubble_map_analysis.py
├── 3_city_level_visualization.py
├── 4_color_size_mapping.py
└── city_data.csv
```

---

## 📊 Dataset

**File Name:** `city_data.csv`

**Description:**
City-level population and GDP dataset used for geographic bubble visualization.

**Columns:**

- city → শহরের নাম
- country → দেশ
- lat → latitude (location)
- lon → longitude (location)
- population → জনসংখ্যা
- gdp → অর্থনৈতিক শক্তি

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_scatter_geo.py`

### 🔹 Purpose

- basic world map visualization
- city location show করা

### 🧾 Code

```python id="sg19c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("city_data.csv")

fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    hover_name="city",
    title="Cities on World Map"
)

fig.show()
```

---

### 🧠 Explanation

- `lat`, `lon` → exact geographic position
- `hover_name` → mouse hover করলে city name দেখায়
- each point = একটি city

👉 Logic:

- map-এর উপর points বসিয়ে location visualization করা হয়

---

## 📄 2. `2_bubble_map_analysis.py`

### 🔹 Purpose

- population based bubble map তৈরি করা
- city importance visualize করা

### 🧾 Code

```python id="sg19c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("city_data.csv")

fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    size="population",
    hover_name="city",
    title="Population Bubble Map"
)

fig.show()
```

---

### 🧠 Explanation

- `size="population"` → bubble size নির্ধারণ করে
- বেশি population → বড় bubble

👉 Insight:

- big cities easily identify করা যায়

---

## 📄 3. `3_city_level_visualization.py`

### 🔹 Purpose

- population + GDP একসাথে analyze করা
- economic strength visualization

### 🧾 Code

```python id="sg19c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("city_data.csv")

fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    size="population",
    color="gdp",
    hover_name="city",
    title="City GDP + Population Analysis"
)

fig.show()
```

---

### 🧠 Explanation

- `size` → population
- `color` → GDP
- দুইটা metric একসাথে compare করা যায়

👉 Logic:

- big + dark = powerful city

---

## 📄 4. `4_color_size_mapping.py`

### 🔹 Purpose

- advanced geo visualization তৈরি করা
- better styling + readability

### 🧾 Code

```python id="sg19c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("city_data.csv")

fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    size="population",
    color="gdp",
    hover_name="city",
    color_continuous_scale="Viridis",
    title="Advanced Geo Visualization"
)

fig.update_geos(
    showcountries=True,
    showcoastlines=True
)

fig.show()
```

---

### 🧠 Explanation

- `color_continuous_scale` → color theme control করে
- `showcountries=True` → country borders দেখায়
- `showcoastlines=True` → map clearer হয়

👉 Insight:

- real dashboards-এর মতো visualization

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- latitude & longitude ব্যবহার করা হয়েছে
- scatter geo map তৈরি করা হয়েছে
- population অনুযায়ী bubble size সেট করা হয়েছে
- GDP অনুযায়ী color mapping করা হয়েছে
- advanced map styling apply করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- New York & Delhi সবচেয়ে high population cities
- USA ও Europe cities high GDP show করে
- South Asia high population density area
- economic + population relationship clear হয়

---

## 🚀 What I Learned

- geographic coordinates ব্যবহার করে real-world mapping করা যায়
- bubble size = importance বোঝায়
- color = economic strength বোঝায়
- multi-variable geo visualization powerful analytics tool

---

## 🧠 Key Concepts (Quick Revision)

- `scatter_geo` → world map scatter plot
- `lat/lon` → location system
- `size` → magnitude (population)
- `color` → value intensity (GDP)
- bubble map → weighted visualization

---

## 📝 Notes

- latitude/longitude ভুল হলে point ভুল জায়গায় দেখাবে
- large dataset হলে performance slow হতে পারে
- color scale visualization clarity affect করে

---

## 📌 Next Day Preview

আগামী দিনে আমরা শিখবো:

- 📊 Violin Plot (`px.violin()`)
- distribution + density analysis
- statistical spread visualization
- advanced EDA techniques

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- real world dataset (world cities API) ব্যবহার করো
- animation add করো
- time-based geo tracking বানাও

---

### 🧪 Practice Ideas

- `GDP per capita` add করে visualize করো
- Asia vs Europe comparison করো
- top 5 cities highlight করো
- different color scales test করো
