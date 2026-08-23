# 📅 Day 14 — Catplot Mastery

---

# 🎯 Objective

- Seaborn-এর unified categorical plotting system শেখা
- `sns.catplot()` ব্যবহার করে এক ফাংশনে multiple plot type তৈরি করা
- `kind` parameter দিয়ে plot type control করা
- `hue` এবং faceting (`col`, `row`) ব্যবহার করে advanced comparison করা
- Categorical visualization workflow simplify করা

---

# 📚 Topics Covered

- `sns.catplot()`
- Unified categorical plotting system
- `kind="bar"`
- `kind="box"`
- `kind="violin"`
- `kind="strip"`
- `kind="swarm"`
- `hue` based grouping
- Faceting (`col`, `row`)
- Figure-level categorical visualization

---

# 📁 Project Structure

```bash id="day14"
day-14/
│── 01_basic_catplot.py
│── 02_catplot_bar.py
│── 03_catplot_box.py
│── 04_catplot_violin.py
│── 05_catplot_strip.py
│── 06_catplot_swarm.py
│── 07_catplot_hue_faceting.py
│── 08_real_world_catplot.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (`tips`)
- **Source:** Seaborn built-in dataset
- **Loaded Using:** `sns.load_dataset("tips")`

---

## 📌 Description

Restaurant tipping dataset যেখানে customer bill, tip, gender, smoker status, day, time, group size ইত্যাদি information থাকে।

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

# 📄 1. 01_basic_catplot.py

## 🔹 Purpose

- Catplot এর basic structure বোঝা
- Default categorical visualization দেখা

---

## 🧾 Code

```python id="cp1"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.catplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.show()
```

---

## 🧠 Explanation

- `sns.catplot()`
  - figure-level categorical plotting function

- default behavior → strip-like plot
- multiple plot type একসাথে handle করতে পারে

---

# 📄 2. 02_catplot_bar.py

## 🔹 Purpose

- Bar plot using catplot

---

## 🧾 Code

```python id="cp2"
sns.catplot(
    data=tips,
    x="day",
    y="total_bill",
    kind="bar"
)
```

---

## 🧠 Explanation

- `kind="bar"`
  - mean value visualize করে

- category-wise average comparison করা যায়

---

# 📄 3. 03_catplot_box.py

## 🔹 Purpose

- Box plot using catplot

---

## 🧾 Code

```python id="cp3"
sns.catplot(
    data=tips,
    x="day",
    y="total_bill",
    kind="box"
)
```

---

## 🧠 Explanation

- quartiles + median show করে
- outliers visualize করে
- distribution summary দেয়

---

# 📄 4. 04_catplot_violin.py

## 🔹 Purpose

- Violin plot using catplot

---

## 🧾 Code

```python id="cp4"
sns.catplot(
    data=tips,
    x="day",
    y="total_bill",
    kind="violin"
)
```

---

## 🧠 Explanation

- full distribution shape দেখায়
- density + statistics একসাথে পাওয়া যায়

---

# 📄 5. 05_catplot_strip.py

## 🔹 Purpose

- Raw data points visualize করা

---

## 🧾 Code

```python id="cp5"
sns.catplot(
    data=tips,
    x="day",
    y="total_bill",
    kind="strip"
)
```

---

## 🧠 Explanation

- each point = one observation
- raw distribution view পাওয়া যায়

---

# 📄 6. 06_catplot_swarm.py

## 🔹 Purpose

- Clean point distribution দেখানো

---

## 🧾 Code

```python id="cp6"
sns.catplot(
    data=tips,
    x="day",
    y="total_bill",
    kind="swarm"
)
```

---

## 🧠 Explanation

- overlapping avoid করে
- clean individual data view দেয়

---

# 📄 7. 07_catplot_hue_faceting.py

## 🔹 Purpose

- advanced grouping + faceting

---

## 🧾 Code

```python id="cp7"
sns.catplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex",
    col="time",
    kind="box"
)
```

---

## 🧠 Explanation

- `hue="sex"` → gender comparison
- `col="time"` → lunch vs dinner split
- multiple subplot automatically তৈরি হয়

---

# 📄 8. 08_real_world_catplot.py

## 🔹 Purpose

- Business insight analysis

---

## 🧾 Code

```python id="cp8"
sns.catplot(
    data=tips,
    x="time",
    y="tip",
    hue="smoker",
    kind="violin"
)
```

---

## 🧠 Explanation

- smoker vs non-smoker tipping behavior
- lunch vs dinner comparison
- real-world customer behavior analysis

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Categorical variables select করা হয়েছে
- `catplot()` দিয়ে different plot types generate করা হয়েছে
- `kind` parameter দিয়ে visualization change করা হয়েছে
- `hue` দিয়ে group comparison করা হয়েছে
- `col` দিয়ে faceting করা হয়েছে
- Real-world insight extract করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- এক function (`catplot`) দিয়ে সব categorical plots করা যায়
- bar, box, violin, strip, swarm সব এক জায়গায়
- faceting দিয়ে multi-view analysis possible
- group comparison খুব সহজ হয়
- EDA workflow অনেক clean হয়

---

# 🚀 What I Learned

- Unified categorical plotting system
- `sns.catplot()` power
- different `kind` usage
- faceting concept (`col`, `row`)
- multi-group comparison
- business insight extraction

---

# 🧠 Key Concepts (Quick Revision)

- `catplot()` → all-in-one categorical plotting
- `kind` → plot type selector
- `hue` → subgroup comparison
- `col/row` → faceting system
- figure-level control → multiple plots auto create

---

# 📝 Notes

## 📌 Common Mistakes

- `kind` ভুল লিখা
- faceting misuse
- large dataset এ swarm slow হওয়া

## 📌 Optimization Tips

- EDA শুরু করার জন্য catplot best choice
- complex comparison এর জন্য faceting use করো
- dataset size অনুযায়ী `kind` choose করো

---

# 📌 Next Day Preview

## 📅 Day 15 — FacetGrid

আগামী দিনে শিখবো:

- `FacetGrid` deep understanding
- manual faceting system
- custom mapping
- multi-panel visualization control
- advanced EDA layout design

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- different `kind` compare করো
- real dataset এ catplot use করো
- faceting combine করে complex dashboard বানাও

---

## 🧪 Practice Ideas

- `day` vs `tip` analysis করো
- `sex` based barplot বানাও
- `time` vs `total_bill` compare করো
- smoker behavior study করো
