# 📅 Day 13 — Strip Plot & Swarm Plot

---

# 🎯 Objective

- Raw data points কিভাবে visualize করা হয় তা শেখা
- `sns.stripplot()` এবং `sns.swarmplot()` ব্যবহার করা শেখা
- Overlapping points problem বুঝা এবং solve করা
- `jitter` concept ব্যবহার করে data spread করা
- Category-wise individual data analysis করা
- Distribution কে point-by-point দেখতে শেখা

---

# 📚 Topics Covered

- `sns.stripplot()`
- `sns.swarmplot()`
- Categorical scatter visualization
- Overlapping points problem
- Jitter concept
- Hue-based grouping
- Raw data distribution analysis
- Strip vs Swarm comparison

---

# 📁 Project Structure

```bash id="day13"
day-13/
│── 01_basic_stripplot.py
│── 02_jitter_explained.py
│── 03_swarmplot_basic.py
│── 04_strip_vs_swarm.py
│── 05_hue_categorical_points.py
│── 06_real_world_analysis.py
│── 07_combined_violin_strip.py
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

# 📄 1. 01_basic_stripplot.py

## 🔹 Purpose

- Raw data points visualize করা
- প্রতিটি observation দেখানো

---

## 🧾 Code

```python id="sp1"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.stripplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title("Strip Plot: All Data Points per Day")
plt.show()
```

---

## 🧠 Explanation

- `sns.stripplot()`
  - প্রতিটি data point আলাদা dot হিসেবে দেখায়

- প্রতিটি dot = একজন customer
- full raw distribution visualize হয়

---

# 📄 2. 02_jitter_explained.py

## 🔹 Purpose

- Overlapping points problem solve করা

---

## 🧾 Code

```python id="sp2"
sns.stripplot(
    data=tips,
    x="day",
    y="total_bill",
    jitter=True
)
```

---

## 🧠 Explanation

- `jitter=True`
  - points সামান্য randomভাবে spread করে

- overlapping problem কমে যায়
- `jitter=False` → points overlap করে

---

# 📄 3. 03_swarmplot_basic.py

## 🔹 Purpose

- Clean point distribution দেখানো

---

## 🧾 Code

```python id="sp3"
sns.swarmplot(
    data=tips,
    x="day",
    y="total_bill"
)
```

---

## 🧠 Explanation

- `swarmplot()`
  - automatically overlap avoid করে

- each point neatly arrange হয়
- small dataset এ খুব effective

---

# 📄 4. 04_strip_vs_swarm.py

## 🔹 Purpose

- Strip plot vs Swarm plot comparison

---

## 🧾 Code

```python id="sp4"
sns.stripplot(data=tips, x="day", y="total_bill")

sns.swarmplot(data=tips, x="day", y="total_bill")
```

---

## 🧠 Explanation

- stripplot → fast but overlap হতে পারে
- swarmplot → clean but slow
- use case depends on dataset size

---

# 📄 5. 05_hue_categorical_points.py

## 🔹 Purpose

- Category-based grouping visualize করা

---

## 🧾 Code

```python id="sp5"
sns.stripplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex"
)
```

---

## 🧠 Explanation

- `hue="sex"`
  - male vs female আলাদা color এ দেখায়

- category ভিতরে subgroup comparison হয়

---

# 📄 6. 06_real_world_analysis.py

## 🔹 Purpose

- Real-world behavioral analysis

---

## 🧾 Code

```python id="sp6"
sns.swarmplot(
    data=tips,
    x="time",
    y="tip",
    hue="smoker"
)
```

---

## 🧠 Explanation

- lunch vs dinner tip behavior analyze করা
- smoker vs non-smoker comparison
- individual level insight পাওয়া যায়

---

# 📄 7. 07_combined_violin_strip.py

## 🔹 Purpose

- Distribution + raw data একসাথে দেখা

---

## 🧾 Code

```python id="sp7"
sns.violinplot(
    data=tips,
    x="day",
    y="total_bill",
    inner=None
)

sns.stripplot(
    data=tips,
    x="day",
    y="total_bill",
    color="black",
    alpha=0.5
)
```

---

## 🧠 Explanation

- violinplot → distribution shape
- stripplot → actual data points
- combined view = deep insight analysis

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Categorical + numerical data select করা হয়েছে
- `stripplot()` দিয়ে raw points visualize করা হয়েছে
- `jitter` দিয়ে overlap fix করা হয়েছে
- `swarmplot()` দিয়ে clean distribution দেখা হয়েছে
- `hue` দিয়ে group comparison করা হয়েছে
- violin + strip combine করে deep analysis করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- প্রতিটি individual data point দেখা যায়
- overlap problem jitter solve করে
- swarmplot clean visualization দেয়
- distribution + raw data একসাথে analysis করা যায়
- customer behavior pattern বোঝা সহজ হয়

---

# 🚀 What I Learned

- Raw data visualization concept
- Overlapping problem handling
- Jitter technique usage
- Strip vs Swarm difference
- Category-wise point analysis
- Combined visualization technique

---

# 🧠 Key Concepts (Quick Revision)

- `stripplot()` → raw scattered points
- `swarmplot()` → non-overlapping points
- `jitter` → random spread for clarity
- `hue` → subgroup color separation
- Violin + strip = best EDA combo

---

# 📝 Notes

## 📌 Common Mistakes

- swarmplot large dataset এ ব্যবহার করা
- jitter না ব্যবহার করে overlap ignore করা
- hue misuse করা

## 📌 Optimization Tips

- large dataset এ stripplot better
- small dataset এ swarmplot perfect
- violin + strip combine করলে best insight পাওয়া যায়

---

# 📌 Next Day Preview

## 📅 Day 14 — Catplot Mastery

আগামী দিনে শিখবো:

- `sns.catplot()`
- unified categorical plotting
- bar, box, violin, strip integration
- faceting system
- multi-plot visualization

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- different datasets এ strip/swarm test করো
- violin + swarm combine করো
- hue-based deeper analysis করো

---

## 🧪 Practice Ideas

- `day` vs `tip` stripplot বানাও
- `sex` based swarm analysis করো
- `time` vs `total_bill` compare করো
- real survey dataset visualize করো
