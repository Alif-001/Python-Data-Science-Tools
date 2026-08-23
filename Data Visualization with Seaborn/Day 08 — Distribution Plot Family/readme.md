# � Day 8 — Distribution Plot Family

---

# 🎯 Objective

- `sns.displot()` ব্যবহার শেখা
- Distribution বুঝতে শেখা
- Histogram + KDE together visualize করা
- Figure-level distribution plotting বোঝা
- Faceted distributions তৈরি করা
- Group comparison করা
- Different distribution styles compare করা

---

# 📚 Topics Covered

- `sns.displot()`
- Histogram + KDE
- Figure-level distribution plots
- Faceted distributions
- Distribution comparison

---

# 📁 Project Structure

```bash
day-8/
│── 01_basic_displot.py
│── 02_histogram_kde_displot.py
│── 03_bins_and_rug.py
│── 04_multiple_distribution.py
│── 05_filled_stack_distribution.py
│── 06_faceted_distribution.py
│── 07_row_col_faceting.py
│── 08_distribution_modes.py
│── README.md
```

---

# 📊 Dataset

## 📌 Dataset Name: `tips`

- **Source:** Built-in Seaborn Dataset
- **Loaded Using:** `sns.load_dataset("tips")`

---

## 📌 Description

Restaurant tipping dataset যেখানে customer bill, tip amount, smoker status, gender, এবং dining context সম্পর্কিত তথ্য রয়েছে।

---

## 📌 Columns

- `total_bill` → মোট bill amount
- `tip` → tip amount
- `sex` → customer gender
- `smoker` → smoker/non-smoker
- `day` → সপ্তাহের দিন
- `time` → lunch/dinner
- `size` → group size

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_displot.py

## 🔹 Purpose

- Basic `displot()` ব্যবহার শেখা
- Figure-level distribution plot তৈরি করা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.displot(
    data=tips,
    x="total_bill"
)

plt.show()
```

---

## 🧠 Explanation

- `sns.displot()`
  - Figure-level distribution plot তৈরি করে

- `x="total_bill"`
  - Total bill এর distribution দেখায়

- Layout নিজে manage করে

---

## 📌 Key Idea

- `displot()` = distribution plotting master function

---

# 📄 2. 02_histogram_kde_displot.py

## 🔹 Purpose

- Histogram এবং KDE together দেখানো
- Distribution shape বোঝা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.displot(
    data=tips,
    x="total_bill",
    kde=True
)

plt.title("Histogram + KDE (displot)")
plt.show()
```

---

## 🧠 Explanation

- `kde=True`
  - Smooth density curve add করে

- Bars frequency দেখায়

- Curve distribution shape দেখায়

---

## 📌 Key Idea

- Histogram = frequency
- KDE = smooth density shape

---

# 📄 3. 03_bins_and_rug.py

## 🔹 Purpose

- Bins control করা
- Rug plot ব্যবহার শেখা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.displot(
    data=tips,
    x="total_bill",
    bins=20,
    rug=True
)

plt.title("Distribution with Rug Plot")
plt.show()
```

---

## 🧠 Explanation

- `bins=20`
  - 20 intervals তৈরি করে

- `rug=True`
  - Raw data points ছোট ticks আকারে দেখায়

---

## 📌 Key Idea

- Rug plot raw observation দেখায়

---

# 📄 4. 04_multiple_distribution.py

## 🔹 Purpose

- Multiple distributions compare করা
- `hue` ব্যবহার শেখা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.displot(
    data=tips,
    x="total_bill",
    hue="sex"
)

plt.title("Distribution Comparison by Gender")
plt.show()
```

---

## 🧠 Explanation

- `hue="sex"`
  - Male/Female আলাদা distribution দেখায়

- Group-wise comparison সহজ হয়

---

## 📌 Key Idea

- `hue` = category-based comparison

---

# 📄 5. 05_filled_stack_distribution.py

## 🔹 Purpose

- Stacked distribution plot তৈরি করা
- Group contribution বোঝা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.displot(
    data=tips,
    x="total_bill",
    hue="smoker",
    multiple="stack"
)

plt.title("Stacked Distribution (Smoker vs Non-Smoker)")
plt.show()
```

---

## 🧠 Explanation

- `multiple="stack"`
  - Categories stack করে দেখায়

- Total distribution এবং group contribution একসাথে দেখা যায়

---

## 📌 Key Idea

- Stacked distribution = total + category breakdown

---

# 📄 6. 06_faceted_distribution.py

## 🔹 Purpose

- Faceted distribution তৈরি করা
- `col` ব্যবহার শেখা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.displot(
    data=tips,
    x="total_bill",
    col="sex"
)

plt.show()
```

---

## 🧠 Explanation

- `col="sex"`
  - Gender অনুযায়ী আলাদা subplot তৈরি করে

- Male ও Female data compare করা যায়

---

## 📌 Key Idea

- Faceting = one dataset, multiple plots

---

# 📄 7. 07_row_col_faceting.py

## 🔹 Purpose

- Advanced faceting শেখা
- Row + column split ব্যবহার করা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.displot(
    data=tips,
    x="total_bill",
    col="sex",
    row="smoker",
    kde=True
)

plt.show()
```

---

## 🧠 Explanation

- `row="smoker"`
  - Vertical split করে

- `col="sex"`
  - Horizontal split করে

- `kde=True`
  - Distribution shape আরও clear হয়

---

## 📌 Key Idea

- Row + col faceting = multi-dimensional comparison

---

# 📄 8. 08_distribution_modes.py

## 🔹 Purpose

- Different distribution styles compare করা
- `element` parameter শেখা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.displot(
    data=tips,
    x="total_bill",
    element="bars"
)
plt.title("Bars Style")
plt.show()

sns.displot(
    data=tips,
    x="total_bill",
    element="step"
)
plt.title("Step Style")
plt.show()

sns.displot(
    data=tips,
    x="total_bill",
    element="step",
    fill=True
)
plt.title("Filled Step Style")
plt.show()
```

---

## 🧠 Explanation

- `element="bars"`
  - Normal histogram style

- `element="step"`
  - Outline style histogram

- `fill=True`
  - Filled step look তৈরি করে

---

## 📌 Key Idea

- Different styles = different visual presentation

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Basic distribution plot তৈরি করা হয়েছে
- Histogram + KDE একসাথে visualize করা হয়েছে
- Bins এবং rug plot ব্যবহার করা হয়েছে
- Group comparison করা হয়েছে
- Stacked distribution তৈরি করা হয়েছে
- Faceting apply করা হয়েছে
- Different distribution styles compare করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- `displot()` distribution analysis এর জন্য খুব useful
- Histogram frequency দেখায়
- KDE smooth shape দেখায়
- `hue` দিয়ে group comparison সহজ হয়
- Faceting multi-group analysis সহজ করে
- Different styles visualization কে flexible করে

---

# 🚀 What I Learned

- `sns.displot()`
- Distribution analysis
- Histogram + KDE combine করা
- Group-wise distribution comparison
- Faceting
- Stacked distributions
- Visualization style control

---

# 🧠 Key Concepts (Quick Revision)

- `displot()` → figure-level distribution plot
- `kde=True` → smooth curve add করে
- `bins` → interval control
- `rug=True` → raw points দেখায়
- `hue` → category comparison
- `multiple="stack"` → stacked groups
- `col`, `row` → faceting

---

# 📝 Notes

## 📌 Common Mistakes

- খুব বেশি bins ব্যবহার করা
- Too many facets তৈরি করা
- KDE ছাড়া distribution interpret করা
- Overlapping categories পরিষ্কার না হওয়া

---

## 📌 Optimization Tips

- Histogram + KDE together ব্যবহার করো
- Group comparison এ `hue` ব্যবহার করো
- Faceting carefully ব্যবহার করো
- Readability এর জন্য clean layout রাখো

---

# 📌 Next Day Preview

## 📅 Day 9 — Count Plot

আগামী দিনে শিখবো:

- `sns.countplot()`
- Categorical frequency
- `hue`
- Ordering categories
- Count comparison

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- Customer spending distribution analysis করা
- Salary distribution faceted plot তৈরি করা
- Sales distribution compare করা
- Multi-panel distribution dashboard তৈরি করা

---

## 🧪 Practice Ideas

- `iris` dataset এ `displot()` ব্যবহার করো
- Different `bins` values compare করো
- `hue` দিয়ে multiple category distribution দেখো
- Faceted KDE distributions তৈরি করো
