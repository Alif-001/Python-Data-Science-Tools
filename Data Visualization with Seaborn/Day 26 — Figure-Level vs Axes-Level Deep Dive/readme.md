# 📅 Day 26 — Figure-Level vs Axes-Level Deep Dive

---

# 🎯 Objective

- Axes-level vs Figure-level plotting বোঝা
- Seaborn-এর architecture clear করা
- `relplot`, `displot`, `catplot` শেখা
- `pairplot` ও `jointplot` দিয়ে multivariate analysis বোঝা
- কখন কোন plot ব্যবহার করতে হবে তা শিখা

---

# 📚 Topics Covered

- Axes-level plots
- Figure-level plots
- `relplot`
- `displot`
- `catplot`
- `pairplot`
- `jointplot`
- Plot selection strategy

---

# 📁 Project Structure

```bash id="day26-structure"
day-26/
│── 01_axes_vs_figure_basic.py
│── 02_relplot_deep_dive.py
│── 03_displot_explained.py
│── 04_catplot_explained.py
│── 05_pairplot_vs_jointplot.py
│── 06_when_to_use_which.py
│── 07_real_world_eda_workflow.py
│── README.md
```

---

# 📊 Dataset

## 📌 File Name: `tips`, `iris` (built-in datasets)

## 📌 Description

এই project এ Seaborn এর built-in dataset ব্যবহার করা হয়েছে:

- `tips` → restaurant tipping behavior
- `iris` → flower feature dataset

---

## 📌 Columns

### 🍽 Tips Dataset

- `total_bill` → total bill amount
- `tip` → tip amount
- `sex` → gender
- `day` → day of week
- `time` → lunch/dinner

### 🌸 Iris Dataset

- `sepal_length` → sepal size
- `sepal_width` → sepal width
- `petal_length` → petal length
- `petal_width` → petal width
- `species` → flower type

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_axes_vs_figure_basic.py

## 🔹 Purpose

- Axes-level vs Figure-level difference বোঝা

## 🧾 Code

```python id="d26-1"
sns.scatterplot(data=tips, x="total_bill", y="tip")
sns.relplot(data=tips, x="total_bill", y="tip")
```

## 🧠 Explanation

- Axes-level → single plot control
- Figure-level → full figure system
- Figure-level automatic layout manage করে

---

# 📄 2. 02_relplot_deep_dive.py

## 🔹 Purpose

- `relplot` বোঝা

## 🧾 Code

```python id="d26-2"
sns.relplot(data=tips, x="total_bill", y="tip", hue="sex")
```

## 🧠 Explanation

- Relationship visualization
- Automatic styling + faceting support
- No manual figure management needed

---

# 📄 3. 03_displot_explained.py

## 🔹 Purpose

- Distribution system বোঝা

## 🧾 Code

```python id="d26-3"
sns.displot(data=tips, x="total_bill", kind="hist", kde=True)
```

## 🧠 Explanation

- Histogram + KDE combined view
- Distribution shape analyze করে
- Figure-level distribution tool

---

# 📄 4. 04_catplot_explained.py

## 🔹 Purpose

- Categorical plotting system বোঝা

## 🧾 Code

```python id="d26-4"
sns.catplot(data=tips, x="day", y="total_bill", kind="box", hue="sex")
```

## 🧠 Explanation

- Boxplot, violinplot, stripplot replace করতে পারে
- Category-based analysis সহজ করে

---

# 📄 5. 05_pairplot_vs_jointplot.py

## 🔹 Purpose

- Multivariate vs bivariate analysis বোঝা

## 🧾 Code

```python id="d26-5"
sns.pairplot(iris, hue="species")
sns.jointplot(data=tips, x="total_bill", y="tip")
```

## 🧠 Explanation

- Pairplot → full dataset overview
- Jointplot → 2-variable deep analysis

---

# 📄 6. 06_when_to_use_which.py

## 🔹 Purpose

- Plot selection strategy শেখা

## 🧾 Code

```python id="d26-6"
print("Check comments for guide")
```

## 🧠 Explanation

- Relational → relplot / scatterplot
- Distribution → displot / histplot
- Categorical → catplot / boxplot
- Multivariate → pairplot

---

# 📄 7. 07_real_world_eda_workflow.py

## 🔹 Purpose

- Full EDA pipeline তৈরি করা

## 🧾 Code

```python id="d26-7"
sns.displot(tips, x="total_bill", kde=True)
sns.relplot(data=tips, x="total_bill", y="tip")
sns.catplot(data=tips, x="day", y="total_bill", kind="box")
```

## 🧠 Explanation

- Step-by-step analysis pipeline
- Distribution → relationship → category insight

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Axes-level plot ব্যবহার করা হয়েছে
- Figure-level plot explore করা হয়েছে
- Multivariate analysis করা হয়েছে
- EDA workflow তৈরি করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Axes-level = precise control
- Figure-level = scalable analysis
- relplot/displot/catplot = automation tools
- pairplot/jointplot = deep insight tools

---

# 🚀 What I Learned

- Seaborn architecture understanding
- Plot hierarchy concept
- Automated visualization system
- Multi-variable analysis
- EDA workflow design

---

# 🧠 Key Concepts (Quick Revision)

- Axes-level → single plot control
- Figure-level → multi-plot system
- relplot → relationship analysis
- displot → distribution analysis
- catplot → categorical analysis
- pairplot → full dataset view
- jointplot → 2-variable deep analysis

---

# 📝 Notes

## 📌 Mistakes

- axes vs figure confusion
- unnecessary manual styling in figure-level plots

## 📌 Optimization Tips

- Use figure-level for EDA
- Use axes-level for fine control
- Always choose based on complexity

---

# 📌 Next Day Preview

## 📅 Day 27 — Pandas + Seaborn Workflow

- Real CSV analysis
- Groupby visualization
- EDA workflow automation
- Practical data projects

---

# ⭐ Bonus

## 🔥 Improvements Ideas

- Full EDA dashboard design
- Automated report generation
- Multi-dataset comparison system

---

## 🧪 Practice Ideas

- Same dataset axes vs figure-level compare করো
- pairplot + heatmap combine করো
- EDA workflow নিজে build করো
