# 📅 Day 14 — Treemap (`px.treemap()`)

---

## 🎯 Objective

- আজকে আমরা শিখবো কীভাবে **hierarchical data (nested structure)** visualize করা যায়
- বুঝবো কোন company / department / team কতটা contribution দিচ্ছে
- business data কে “tree structure” আকারে দেখা
- part-to-whole relationship visualize করা

---

## 📚 Topics Covered

- `px.treemap()`
- Hierarchical visualization
- Nested categories
- Business data breakdown
- Path-based structure (`path`)
- Revenue contribution analysis
- Color encoding in treemap

---

## 📁 Project Structure

```text id="tm14p1"
Day 14 — Treemap/
│
├── 1_basic_treemap.py
├── 2_nested_categories.py
├── 3_business_breakdown.py
├── 4_advanced_treemap.py
└── company_data.csv
```

---

## 📊 Dataset

**File Name:** `company_data.csv`

**Description:**
Company revenue dataset used to visualize hierarchical business structure (company → department → team).

**Columns:**

- company → কোম্পানির নাম
- department → কোন বিভাগ (Engineering / Sales / HR)
- team → সাব-টিমের নাম
- revenue → revenue contribution

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_treemap.py`

### 🔹 Purpose

- basic treemap তৈরি করা
- company → department hierarchy visualize করা

### 🧾 Code

```python id="tm14c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

fig = px.treemap(
    df,
    path=["company", "department"],
    values="revenue",
    title="Company Revenue Treemap"
)

fig.show()
```

---

### 🧠 Explanation

- `pd.read_csv()` → dataset load করে
- `px.treemap()` → hierarchical visualization তৈরি করে
- `path=[]` → hierarchy structure define করে
- `values="revenue"` → box size নির্ধারণ করে

👉 Logic:

- বেশি revenue = বড় box
- কম revenue = ছোট box

---

## 📄 2. `2_nested_categories.py`

### 🔹 Purpose

- multi-level hierarchy দেখানো
- company → department → team breakdown

### 🧾 Code

```python id="tm14c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

fig = px.treemap(
    df,
    path=["company", "department", "team"],
    values="revenue",
    title="Nested Hierarchy Treemap"
)

fig.show()
```

---

### 🧠 Explanation

- `path=["company","department","team"]`
- তিন level hierarchy তৈরি করে

👉 Logic:

- company → top level
- department → mid level
- team → lowest level breakdown

---

## 📄 3. `3_business_breakdown.py`

### 🔹 Purpose

- revenue অনুযায়ী business breakdown analysis
- color intensity ব্যবহার করা

### 🧾 Code

```python id="tm14c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

fig = px.treemap(
    df,
    path=["company", "department", "team"],
    values="revenue",
    color="revenue",
    title="Business Revenue Breakdown"
)

fig.show()
```

---

### 🧠 Explanation

- `color="revenue"` → intensity show করে
- বেশি revenue = darker/bigger blocks

👉 Logic:

- visual comparison সহজ হয়
- high revenue area easily identify করা যায়

---

## 📄 4. `4_advanced_treemap.py`

### 🔹 Purpose

- advanced styling + layout improvement
- dashboard-ready visualization

### 🧾 Code

```python id="tm14c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

fig = px.treemap(
    df,
    path=["company", "department", "team"],
    values="revenue",
    color="department",
    title="Advanced Treemap with Styling"
)

fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25)
)

fig.show()
```

---

### 🧠 Explanation

- `color="department"` → department-based grouping
- `update_layout()` → chart spacing improve করে

👉 Logic:

- visualization clean হয়
- dashboard-ready output তৈরি হয়

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- hierarchy structure define করা হয়েছে
- treemap তৈরি করা হয়েছে
- revenue-based sizing করা হয়েছে
- color encoding add করা হয়েছে
- layout optimized করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- Engineering department সাধারণত বেশি revenue generate করে
- company-wise contribution clearly visible
- team-level breakdown থেকে top performers identify করা যায়
- nested structure business understanding সহজ করে

---

## 🚀 What I Learned

- Treemap hierarchical data visualize করতে ব্যবহার হয়
- `path` দিয়ে structure define করা হয়
- size = value importance বোঝায়
- color = intensity / category difference বোঝায়
- business analytics এ খুব powerful tool

---

## 🧠 Key Concepts (Quick Revision)

- Treemap → hierarchical visualization
- Path → structure definition
- Values → box size control
- Color → visual grouping / intensity
- Nested categories → multi-level data breakdown

---

## 📝 Notes

- খুব deep hierarchy হলে readability কমে যেতে পারে
- small dataset এ treemap less meaningful হতে পারে
- proper grouping না করলে misleading visualization হতে পারে

---

## 📌 Next Day Preview

আগামী দিনে আমরা শিখবো:

- 🌞 Sunburst Chart (`px.sunburst()`)
- circular hierarchical visualization
- radial data structure
- advanced business hierarchy mapping

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- real company dataset ব্যবহার করো
- profit column add করো
- department comparison dashboard বানাও

---

### 🧪 Practice Ideas

- কোন company most profitable খুঁজে বের করো
- department-wise revenue compare করো
- team-level best performer identify করো
- hierarchy depth change করে observe করো
