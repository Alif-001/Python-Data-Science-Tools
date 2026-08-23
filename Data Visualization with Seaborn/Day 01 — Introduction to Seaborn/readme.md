# 📅 Day 1 — Introduction to Seaborn

---

# 🎯 Objective

- Seaborn কী তা বোঝা
- কেন Seaborn ব্যবহার করা হয় তা শেখা
- Seaborn vs Matplotlib comparison বোঝা
- Seaborn install ও import করা
- Built-in datasets নিয়ে কাজ শেখা
- Theme setup করা
- প্রথম visualization তৈরি করা
- Axes-level vs Figure-level plots এর পার্থক্য বোঝা

---

# 📚 Topics Covered

- What is Seaborn
- Why Seaborn is used
- Seaborn vs Matplotlib
- Installation
- Importing Seaborn
- Built-in datasets
- Theme setup
- First visualization
- Axes-level vs Figure-level plots

---

# 📁 Project Structure

```bash
day-1/
│── 01_intro_seaborn.py
│── 02_first_visualization.py
│── 03_axes_vs_figure.py
│── README.md
```

---

# 📊 Dataset

- **Dataset Name:** `tips`
- **Source:** Built-in Seaborn Dataset
- **Loaded Using:** `sns.load_dataset("tips")`

## 📌 Description

Restaurant tipping dataset যেখানে customer bill, tip, gender, smoking status ইত্যাদি তথ্য রয়েছে।

## 📌 Columns

- `total_bill` → মোট বিল
- `tip` → টিপের amount
- `sex` → customer gender
- `smoker` → smoker কি না
- `day` → সপ্তাহের দিন
- `time` → lunch/dinner
- `size` → total people

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_intro_seaborn.py

## 🔹 Purpose

- Seaborn introduction
- Dataset loading
- Theme setup
- প্রথম histogram visualization তৈরি করা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

print(tips.head())

sns.set_theme(style="darkgrid")

sns.histplot(data=tips, x="total_bill")

plt.title("Distribution of Total Bill")
plt.show()
```

---

## 🧠 Explanation

- `import seaborn as sns`
  - Seaborn library import করা হয়েছে

- `import matplotlib.pyplot as plt`
  - Plot display করার জন্য matplotlib ব্যবহার করা হয়েছে

- `sns.load_dataset("tips")`
  - Built-in tips dataset load করা হয়েছে

- `tips.head()`
  - প্রথম ৫টি row দেখায়

- `sns.set_theme(style="darkgrid")`
  - Plot styling apply করা হয়েছে

- `sns.histplot()`
  - Histogram plot তৈরি করা হয়েছে

- `plt.show()`
  - Plot display করে

---

# 📄 2. 02_first_visualization.py

## 🔹 Purpose

- প্রথম real Seaborn visualization তৈরি করা
- Scatter plot শেখা
- Seaborn vs Matplotlib concept বোঝা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set_theme(style="whitegrid")

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex"
)

plt.title("Total Bill vs Tip")
plt.show()
```

---

## 🧠 Explanation

- `sns.scatterplot()`
  - Scatter plot তৈরি করে

- `x="total_bill"`
  - X-axis এ total bill দেখানো হয়েছে

- `y="tip"`
  - Y-axis এ tip দেখানো হয়েছে

- `hue="sex"`
  - Male/Female অনুযায়ী different colors apply হয়েছে

- `plt.title()`
  - Plot এর title সেট করা হয়েছে

---

# 📄 3. 03_axes_vs_figure.py

## 🔹 Purpose

- Axes-level vs Figure-level plot difference বোঝানো

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title("Axes-level Plot Example")
plt.show()

sns.relplot(
    data=tips,
    x="total_bill",
    y="tip",
    kind="scatter"
)

plt.title("Figure-level Plot Example")
plt.show()
```

---

## 🧠 Explanation

### 📌 Axes-level Plot

- `sns.scatterplot()`
  - Single axes এর মধ্যে plot তৈরি করে

### 📌 Figure-level Plot

- `sns.relplot()`
  - পুরো figure system তৈরি করে
  - Multiple subplot support করে

---

## 📌 Key Difference

### 🔹 Axes-level

- Single plot area এ কাজ করে
- More control পাওয়া যায়
- Examples:
  - `scatterplot`
  - `lineplot`
  - `histplot`

### 🔹 Figure-level

- Automatically figure তৈরি করে
- Multiple subplot support করে
- Examples:
  - `relplot`
  - `catplot`
  - `displot`

---

# ⚙️ Implementation Flow

- Seaborn import করা হয়েছে
- Built-in dataset load করা হয়েছে
- Theme apply করা হয়েছে
- Histogram visualization তৈরি করা হয়েছে
- Scatter plot তৈরি করা হয়েছে
- Axes-level এবং Figure-level plot compare করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Seaborn দিয়ে খুব সহজে সুন্দর statistical plots তৈরি করা যায়
- Built-in themes visualization কে professional look দেয়
- Figure-level plots multiple subplot support করে
- Seaborn code অনেক cleaner compared to Matplotlib

---

# 🚀 What I Learned

- Seaborn basics
- Dataset loading
- Theme customization
- Histogram plotting
- Scatter plotting
- Axes-level vs Figure-level concept
- Matplotlib integration

---

# 🧠 Key Concepts (Quick Revision)

- Seaborn = statistical visualization library
- Built on top of Matplotlib
- `sns.load_dataset()` → built-in dataset load করে
- `sns.set_theme()` → styling apply করে
- `scatterplot()` → axes-level plot
- `relplot()` → figure-level plot

---

# 📝 Notes

## 📌 Common Mistakes

- `plt.show()` দিতে ভুলে যাওয়া
- Dataset column name typo করা
- Theme apply না করা

## 📌 Optimization Tips

- Seaborn + Pandas একসাথে ব্যবহার করলে workflow সহজ হয়
- Figure-level plots complex visualization এর জন্য useful

---

# 📌 Next Day Preview

## 📅 Day 2 — Seaborn Styling & Themes

আগামী দিনে শিখবো:

- `sns.set_theme()`
- `sns.set_style()`
- darkgrid
- whitegrid
- dark
- white
- ticks
- Context scaling
- Color palettes
- Figure styling

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- More built-in datasets explore করা
- Different themes compare করা
- Multiple plots একসাথে visualize করা

---

## 🧪 Practice Ideas

- `iris` dataset load করে histogram তৈরি করো
- Different styles apply করে compare করো
- `hue` ব্যবহার করে scatter plot customize করো
- `tips.describe()` ব্যবহার করে dataset summary দেখো
