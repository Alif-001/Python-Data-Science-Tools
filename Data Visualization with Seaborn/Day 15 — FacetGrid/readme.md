# 📅 Day 15 — FacetGrid

---

# 🎯 Objective

- Seaborn-এর advanced faceting system শেখা
- `FacetGrid` ব্যবহার করে multi-panel visualization তৈরি করা
- row, column ভিত্তিক data splitting বোঝা
- `.map()` দিয়ে custom plotting control শেখা
- real-world dashboard style visualization তৈরি করা

---

# 📚 Topics Covered

- `FacetGrid`
- Row faceting
- Column faceting
- Multi-panel visualization
- Custom mapping with `.map()`
- Hue integration
- Advanced EDA layout design

---

# 📁 Project Structure

```bash id="day15"
day-15/
│── 01_basic_facetgrid.py
│── 02_row_col_facetgrid.py
│── 03_custom_mapping.py
│── 04_multiple_variables_facetgrid.py
│── 05_histogram_facetgrid.py
│── 06_advanced_facetgrid.py
│── 07_real_world_dashboard.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (`tips`)
- **Source:** Seaborn built-in dataset
- **Loaded Using:** `sns.load_dataset("tips")`

---

## 📌 Description

Restaurant tipping dataset যেখানে customer spending, tip, gender, smoker status, day, time ইত্যাদি information থাকে।

---

## 📌 Columns

- `total_bill` → total bill amount
- `tip` → tip amount
- `sex` → gender
- `smoker` → smoker status
- `day` → day of week
- `time` → lunch/dinner
- `size` → group size

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_facetgrid.py

## 🔹 Purpose

- FacetGrid এর basic structure বোঝা
- column-based splitting শেখা

---

## 🧾 Code

```python id="fg1"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

g = sns.FacetGrid(
    data=tips,
    col="sex"
)

g.map(sns.histplot, "total_bill")

plt.show()
```

---

## 🧠 Explanation

- `FacetGrid`
  - data কে multiple subplot এ ভাগ করে

- `col="sex"`
  - male / female আলাদা subplot তৈরি করে

- `.map()`
  - প্রতিটি subplot এ same plot apply করে

---

# 📄 2. 02_row_col_facetgrid.py

## 🔹 Purpose

- row + column faceting শেখা

---

## 🧾 Code

```python id="fg2"
g = sns.FacetGrid(
    data=tips,
    col="sex",
    row="smoker"
)

g.map(sns.scatterplot, "total_bill", "tip")
```

---

## 🧠 Explanation

- `col="sex"` → horizontal split
- `row="smoker"` → vertical split
- 2D comparison grid তৈরি হয়

---

# 📄 3. 03_custom_mapping.py

## 🔹 Purpose

- custom plot function mapping

---

## 🧾 Code

```python id="fg3"
g = sns.FacetGrid(
    data=tips,
    col="time"
)

g.map(sns.kdeplot, "total_bill", fill=True)
```

---

## 🧠 Explanation

- KDE plot ব্যবহার করে distribution দেখানো
- `fill=True` → area fill করে density বোঝায়

---

# 📄 4. 04_multiple_variables_facetgrid.py

## 🔹 Purpose

- hue + faceting combined analysis

---

## 🧾 Code

```python id="fg4"
g = sns.FacetGrid(
    data=tips,
    col="day",
    hue="sex"
)

g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()
```

---

## 🧠 Explanation

- `hue="sex"` → gender-based coloring
- `col="day"` → day-wise split
- `.add_legend()` → legend show করে

---

# 📄 5. 05_histogram_facetgrid.py

## 🔹 Purpose

- distribution comparison using histogram

---

## 🧾 Code

```python id="fg5"
g = sns.FacetGrid(
    data=tips,
    col="smoker"
)

g.map(sns.histplot, "total_bill")
```

---

## 🧠 Explanation

- smoker vs non-smoker distribution compare করা
- frequency analysis করা যায়

---

# 📄 6. 06_advanced_facetgrid.py

## 🔹 Purpose

- multi-dimensional advanced analysis

---

## 🧾 Code

```python id="fg6"
g = sns.FacetGrid(
    data=tips,
    col="time",
    row="sex",
    hue="smoker"
)

g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()
```

---

## 🧠 Explanation

- 3D-style segmentation:
  - time (col)
  - sex (row)
  - smoker (color)

- full EDA power view তৈরি হয়

---

# 📄 7. 07_real_world_dashboard.py

## 🔹 Purpose

- dashboard-style visualization

---

## 🧾 Code

```python id="fg7"
g = sns.FacetGrid(
    data=tips,
    col="day",
    hue="sex"
)

g.map(sns.boxplot, "time", "total_bill")
g.add_legend()
```

---

## 🧠 Explanation

- day-wise mini dashboards তৈরি হয়
- business reporting style analysis করা যায়

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- FacetGrid structure তৈরি করা হয়েছে
- row/column-based splitting করা হয়েছে
- `.map()` দিয়ে plot apply করা হয়েছে
- hue দিয়ে group comparison করা হয়েছে
- legend add করা হয়েছে
- multi-panel visualization তৈরি হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- FacetGrid = manual multi-panel system
- row + col = powerful data segmentation
- `.map()` = flexible plotting engine
- hue = group comparison inside grid
- dashboard-style analysis possible

---

# 🚀 What I Learned

- FacetGrid system
- multi-dimensional visualization
- custom plotting with `.map()`
- advanced EDA layout design
- dashboard-style analysis

---

# 🧠 Key Concepts (Quick Revision)

- `FacetGrid()` → multi-panel structure
- `col` → horizontal split
- `row` → vertical split
- `.map()` → plotting function apply
- `hue` → color grouping
- `add_legend()` → legend display

---

# 📝 Notes

## 📌 Common Mistakes

- `.map()` ভুল function ব্যবহার
- legend missing করা
- large dataset এ slow rendering

## 📌 Optimization Tips

- small subset দিয়ে test করা
- appropriate plot type choose করা
- faceting carefully design করা

---

# 📌 Next Day Preview

## 📅 Day 16 — Pair Plot

আগামী দিনে শিখবো:

- `pairplot()` deep understanding
- multivariable relationship analysis
- correlation visualization
- automatic EDA matrix
- feature relationship discovery

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- real dataset এ dashboard তৈরি করা
- multiple FacetGrid combine করা
- business report style visualization বানানো

---

## 🧪 Practice Ideas

- smoker vs non-smoker analysis করো
- day-wise spending pattern দেখো
- tip behavior segmentation করো
- gender-based comparison করো
