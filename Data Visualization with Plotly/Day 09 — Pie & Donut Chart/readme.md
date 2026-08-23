# 📅 Day 9 — Pie & Donut Chart (Plotly Express)

## 🎯 Objective

- আজকে Pie Chart এবং Donut Chart ব্যবহার করে percentage visualization শেখা।
- part-to-whole relationship বোঝা।
- market share / contribution analysis করা।
- pie chart এর limitations বোঝা (real-world important).

## 📚 Topics Covered

- px.pie()
- Labels & values
- Donut chart
- Percentage visualization
- Pie chart limitations

---

## 📁 Project Structure

```bash
Day 9 — Pie & Donut Chart/
│── 1_basic_pie_chart.py
│── 2_labels_and_values.py
│── 3_donut_chart.py
│── 4_percentage_visualization.py
│── 5_pie_chart_limitations.py
│── market_share.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `market_share.csv`
- **Description:** Smartphone brand-wise market share dataset
- **Columns:**
  - `brand` → smartphone brand name
  - `sales` → market share / sales percentage

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_pie_chart.py`

### 🔹 Purpose

- Basic pie chart তৈরি করা
- brand-wise market share visualize করা

### 🧾 Code

```python id="p9c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("market_share.csv")

fig = px.pie(
    df,
    names="brand",
    values="sales",
    title="Smartphone Market Share"
)

fig.show()
```

### 🧠 Explanation

- `px.pie()` → pie chart তৈরি করে
- `names="brand"` → category label
- `values="sales"` → numeric contribution
- Logic → total market share breakdown দেখানো

---

## 📄 2. `2_labels_and_values.py`

### 🔹 Purpose

- labels + percentage display করা

### 🧾 Code

```python id="p9c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("market_share.csv")

fig = px.pie(
    df,
    names="brand",
    values="sales",
    title="Brand-wise Sales Share"
)

fig.update_traces(
    textinfo="label+percent"
)

fig.show()
```

### 🧠 Explanation

- `textinfo="label+percent"` → label + percentage show করে
- pie chart আরও readable হয়
- Logic → clear percentage-based comparison

---

## 📄 3. `3_donut_chart.py`

### 🔹 Purpose

- donut chart তৈরি করা
- modern visualization style শেখা

### 🧾 Code

```python id="p9c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("market_share.csv")

fig = px.pie(
    df,
    names="brand",
    values="sales",
    hole=0.4,
    title="Donut Chart: Market Share"
)

fig.show()
```

### 🧠 Explanation

- `hole=0.4` → pie chart → donut chart
- center space create করে
- Logic → same data, better UI style

---

## 📄 4. `4_percentage_visualization.py`

### 🔹 Purpose

- percentage-based visualization show করা

### 🧾 Code

```python id="p9c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("market_share.csv")

fig = px.pie(
    df,
    names="brand",
    values="sales",
    title="Percentage Visualization"
)

fig.update_traces(
    textposition="inside",
    textinfo="percent+label"
)

fig.show()
```

### 🧠 Explanation

- `textposition="inside"` → text ভিতরে দেখায়
- `percent+label` → percentage + label display
- Logic → clean percentage visualization

---

## 📄 5. `5_pie_chart_limitations.py`

### 🔹 Purpose

- pie chart এর limitation বোঝা
- too many categories case handle করা

### 🧾 Code

```python id="p9c5"
import pandas as pd
import plotly.express as px

data = {
    "category": ["A","B","C","D","E","F","G","H","I","J"],
    "value": [10,9,8,7,6,5,4,3,2,1]
}

df = pd.DataFrame(data)

fig = px.pie(
    df,
    names="category",
    values="value",
    title="Pie Chart Limitation Example"
)

fig.show()
```

### 🧠 Explanation

- অনেক category হলে pie chart confusing হয়
- small differences বুঝা কঠিন
- Logic → readability issue highlight করা

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- basic pie chart তৈরি করা হয়েছে
- labels + percentages add করা হয়েছে
- donut chart তৈরি করা হয়েছে
- limitation case test করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- market share easily visualize করা যায়
- percentage breakdown clear হয়
- donut chart cleaner UI দেয়
- too many categories হলে pie chart weak হয়

---

## 🚀 What I Learned

- pie chart part-to-whole relationship দেখায়
- donut chart pie chart এর improved version
- percentage visualization analysis সহজ করে
- too many categories হলে bar chart better

---

## 🧠 Key Concepts (Quick Revision)

- pie chart → percentage distribution
- names → category
- values → numeric share
- hole → donut chart
- small categories → pie chart best

---

## 📝 Notes

- pie chart শুধুমাত্র small categories এ best
- large dataset এ readability কমে যায়
- comparison analysis এর জন্য bar chart better

---

## 📌 Next Day Preview

- আগামী দিনে Area Chart শিখবো
- cumulative trend visualization দেখবো
- time-series based area analysis শুরু হবে

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- explode effect add করা
- hover customization করা
- brand-wise color mapping improve করা

### 🧪 Practice Ideas

- company revenue share chart বানাও
- department-wise contribution visualize করো
- pie vs bar chart compare করো
