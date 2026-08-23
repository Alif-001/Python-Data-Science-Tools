# 📅 Day 20 — Mapbox Visualization (`Interactive Maps`)

---

## 🎯 Objective

- আজকে আমরা শিখবো কীভাবে **advanced interactive map visualization** তৈরি করা যায়
- GPS-level data visualization করা
- real-world style zoomable maps ব্যবহার করা
- user activity + location একসাথে analyze করা

---

## 📚 Topics Covered

- `px.scatter_mapbox()`
- Interactive Map visualization
- GPS-level plotting
- Map styles (dark, light, street)
- Size & color encoding on maps
- Real-time style dashboards

---

## 📁 Project Structure

```text id="mb20p1"
Day 20 — Mapbox Visualization/
│
├── 1_basic_mapbox.py
├── 2_gps_tracking.py
├── 3_city_density_map.py
├── 4_advanced_map_styles.py
└── location_data.csv
```

---

## 📊 Dataset

**File Name:** `location_data.csv`

**Description:**
City-level GPS + user activity dataset used for Mapbox visualization.

**Columns:**

- place → শহরের নাম
- lat → latitude (GPS location)
- lon → longitude (GPS location)
- users → active user সংখ্যা
- activity → activity level (low / medium / high)

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_mapbox.py`

### 🔹 Purpose

- basic interactive map তৈরি করা
- world map-এ location show করা

### 🧾 Code

```python id="mb20c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("location_data.csv")

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    hover_name="place",
    zoom=2,
    title="Basic Mapbox Visualization"
)

fig.update_layout(
    mapbox_style="open-street-map"
)

fig.show()
```

---

### 🧠 Explanation

- `lat`, `lon` → exact GPS location
- `hover_name` → hover করলে city name দেখায়
- `zoom=2` → global view

👉 Logic:

- প্রতিটি point = একটি real location

---

## 📄 2. `2_gps_tracking.py`

### 🔹 Purpose

- user activity based GPS visualization
- bubble size দিয়ে usage বোঝানো

### 🧾 Code

```python id="mb20c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("location_data.csv")

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    size="users",
    hover_name="place",
    zoom=2,
    title="GPS User Activity Map"
)

fig.update_layout(
    mapbox_style="open-street-map"
)

fig.show()
```

---

### 🧠 Explanation

- `size="users"` → বেশি users = বড় bubble
- GPS style tracking simulate করা হয়েছে

👉 Insight:

- big cities = high activity zones

---

## 📄 3. `3_city_density_map.py`

### 🔹 Purpose

- activity level based map visualization
- behavioral analysis করা

### 🧾 Code

```python id="mb20c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("location_data.csv")

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    color="activity",
    size="users",
    hover_name="place",
    zoom=2,
    title="City Activity Map"
)

fig.update_layout(
    mapbox_style="carto-positron"
)

fig.show()
```

---

### 🧠 Explanation

- `color="activity"` → activity level show করে
- `size="users"` → user intensity বোঝায়

👉 Logic:

- high activity = important regions

---

## 📄 4. `4_advanced_map_styles.py`

### 🔹 Purpose

- advanced styled interactive map তৈরি করা
- production-level visualization

### 🧾 Code

```python id="mb20c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("location_data.csv")

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    size="users",
    color="users",
    hover_name="place",
    color_continuous_scale="Viridis",
    zoom=2,
    title="Advanced Mapbox Visualization"
)

fig.update_layout(
    mapbox_style="carto-darkmatter"
)

fig.show()
```

---

### 🧠 Explanation

- `color_continuous_scale="Viridis"` → smooth gradient
- `carto-darkmatter` → dark theme map
- size + color combined visualization

👉 Insight:

- production dashboard-style map

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- latitude & longitude ব্যবহার করা হয়েছে
- interactive map তৈরি করা হয়েছে
- user activity visualize করা হয়েছে
- different map styles apply করা হয়েছে
- advanced color + size encoding করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- Dhaka, Delhi, New York → high activity centers
- South Asia → dense user distribution
- Western cities → high economic + user activity
- activity level map clustering clear করে

---

## 🚀 What I Learned

- Mapbox ব্যবহার করে real-world interactive maps বানানো যায়
- GPS data visualization খুব powerful analytics tool
- size + color একসাথে multi-dimensional insight দেয়
- map styles visualization experience পরিবর্তন করে

---

## 🧠 Key Concepts (Quick Revision)

- `scatter_mapbox` → interactive GPS map
- `lat/lon` → location coordinates
- `size` → user intensity
- `color` → activity/value
- map style → visualization theme

---

## 📝 Notes

- GPS data ভুল হলে map ভুল position দেখাবে
- internet required for map rendering
- zoom level analysis clarity affect করে

---

## 📌 Next Day Preview

আগামী দিনে আমরা শিখবো:

- 📊 Area Chart (`px.area()`)
- time-series trend visualization
- cumulative data analysis
- business growth tracking

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- real-time tracking system বানাও
- animation-based movement map তৈরি করো
- live traffic simulation add করো

---

### 🧪 Practice Ideas

- `traffic data` add করে map বানাও
- Asia vs Europe activity compare করো
- top 3 cities highlight করো
- different map styles test করো
