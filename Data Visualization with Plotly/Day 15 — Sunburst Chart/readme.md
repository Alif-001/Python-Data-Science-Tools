# 📅 Day 15 — Sunburst Chart (`px.sunburst()`)

---

## 🎯 Objective

- আজকে আমরা শিখবো কীভাবে **hierarchical data circular form এ visualize করা যায়**
- বুঝবো parent-child relationship কিভাবে work করে
- treemap এর alternative হিসেবে sunburst chart ব্যবহার করা
- business structure কে ring-based visualization এ দেখা

---

## 📚 Topics Covered

- `px.sunburst()`
- Hierarchical circular visualization
- Parent-child relationship
- Multi-level data breakdown
- Revenue distribution analysis
- Color intensity visualization
- Sunburst vs Treemap comparison

---

## 📁 Project Structure

```text id="sb15p1"
Day 15 — Sunburst Chart/
│
├── 1_basic_sunburst.py
├── 2_parent_child_relationship.py
├── 3_business_hierarchy.py
├── 4_advanced_sunburst.py
└── company_data.csv
```

---

## 📊 Dataset

**File Name:** `company_data.csv`

**Description:**
Company revenue dataset used to visualize hierarchical structure in circular format (company → department → team).

**Columns:**

- company → কোম্পানির নাম
- department → বিভাগ (Engineering / Sales / HR)
- team → সাব-টিমের নাম
- revenue → revenue contribution

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_sunburst.py`

### 🔹 Purpose

- basic sunburst chart তৈরি করা
- company → department hierarchy visualize করা

### 🧾 Code

```python id="sb15c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

fig = px.sunburst(
    df,
    path=["company", "department"],
    values="revenue",
    title="Company → Department Revenue (Sunburst)"
)

fig.show()
```

---

### 🧠 Explanation

- `pd.read_csv()` → dataset load করে
- `px.sunburst()` → circular hierarchical chart তৈরি করে
- `path=[]` → hierarchy define করে
- `values="revenue"` → segment size নির্ধারণ করে

👉 Logic:

- center = company
- outer ring = department
- বেশি revenue = বড় segment

---

## 📄 2. `2_parent_child_relationship.py`

### 🔹 Purpose

- full hierarchy visualize করা
- parent-child relationship বোঝা

### 🧾 Code

```python id="sb15c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

fig = px.sunburst(
    df,
    path=["company", "department", "team"],
    values="revenue",
    title="Full Parent → Child Relationship"
)

fig.show()
```

---

### 🧠 Explanation

- `path=["company","department","team"]`
- 3-level hierarchy তৈরি করে

👉 Logic:

- company → root
- department → mid level
- team → outer level
- structure circular rings আকারে দেখায়

---

## 📄 3. `3_business_hierarchy.py`

### 🔹 Purpose

- revenue intensity visualize করা
- business breakdown analysis

### 🧾 Code

```python id="sb15c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

fig = px.sunburst(
    df,
    path=["company", "department", "team"],
    values="revenue",
    color="revenue",
    title="Business Hierarchy with Revenue Intensity"
)

fig.show()
```

---

### 🧠 Explanation

- `color="revenue"` → intensity show করে
- high revenue = darker/bigger segment

👉 Logic:

- visual comparison সহজ হয়
- strongest revenue areas easily identify করা যায়

---

## 📄 4. `4_advanced_sunburst.py`

### 🔹 Purpose

- advanced styling + layout optimization
- dashboard-ready visualization

### 🧾 Code

```python id="sb15c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("company_data.csv")

fig = px.sunburst(
    df,
    path=["company", "department", "team"],
    values="revenue",
    color="department",
    title="Advanced Sunburst Chart"
)

fig.update_layout(
    margin=dict(t=40, l=0, r=0, b=0)
)

fig.show()
```

---

### 🧠 Explanation

- `color="department"` → department-based grouping
- `update_layout()` → spacing clean করে

👉 Logic:

- visualization clean + readable হয়
- presentation/dashboard ready output তৈরি হয়

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- hierarchy structure define করা হয়েছে
- sunburst chart তৈরি করা হয়েছে
- revenue-based sizing করা হয়েছে
- color encoding add করা হয়েছে
- layout optimized করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- TechCorp Engineering department সবচেয়ে বেশি revenue generate করে
- Sales department strong contribution দেয়
- team-level breakdown থেকে top performers identify করা যায়
- circular layout hierarchy বুঝতে easy করে

---

## 🚀 What I Learned

- Sunburst chart circular hierarchical visualization
- parent-child relationship easily visualize করা যায়
- size = importance (revenue)
- color = intensity / grouping
- treemap এর alternative visualization style

---

## 🧠 Key Concepts (Quick Revision)

- Sunburst → circular hierarchy visualization
- Path → structure definition
- Center → root node
- Rings → hierarchy levels
- Values → segment size
- Color → category/intensity

---

## 📝 Notes

- deep hierarchy হলে chart complex হতে পারে
- small dataset এ circular view less meaningful
- proper grouping না হলে readability কমে যায়

---

## 📌 Next Day Preview

আগামী দিনে আমরা শিখবো:

- 🔻 Funnel Chart (`px.funnel()`)
- sales pipeline visualization
- conversion tracking
- process flow analysis

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- real business dataset ব্যবহার করো
- profit column add করো
- department-wise comparison dashboard বানাও

---

### 🧪 Practice Ideas

- কোন company most profitable খুঁজে বের করো
- department performance compare করো
- team-level best performer identify করো
- treemap vs sunburst visually compare করো
