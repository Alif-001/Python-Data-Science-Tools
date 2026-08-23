# 📅 Day 11 — Box Plot

---

# 🎯 Objective

- Data distribution কিভাবে visualize করা হয় তা শেখা
- `sns.boxplot()` ব্যবহার করে statistical summary বোঝা
- Quartiles (Q1, Q2, Q3) বুঝে data spread analyze করা
- IQR (Interquartile Range) concept বোঝা
- Outlier detection করা
- Group-wise distribution compare করা

---

# 📚 Topics Covered

- `sns.boxplot()`
- Quartiles (Q1, Q2, Q3)
- Median visualization
- IQR (Interquartile Range)
- Outlier detection
- Distribution comparison
- Horizontal boxplot
- Group-wise analysis using `hue`

---

# 📁 Project Structure

```bash id="bxp11"
day-11/
│── 01_basic_boxplot.py
│── 02_quartiles_explained.py
│── 03_iqr_understanding.py
│── 04_outlier_detection.py
│── 05_horizontal_boxplot.py
│── 06_group_comparison_boxplot.py
│── 07_real_world_analysis.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (tips)
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

# 📄 1. 01_basic_boxplot.py

## 🔹 Purpose

- Basic distribution visualization করা
- Data spread বোঝা

---

## 🧾 Code

```python id="bp1"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.boxplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title("Box Plot: Total Bill per Day")
plt.show()
```

---

## 🧠 Explanation

- `sns.boxplot()`
  - data distribution summarize করে

- Box plot দেখায়:
  - median
  - spread
  - range

---

# 📄 2. 02_quartiles_explained.py

## 🔹 Purpose

- Quartiles concept বোঝা

---

## 🧾 Code

```python id="bp2"
sns.boxplot(
    data=tips,
    x="day",
    y="tip"
)
```

---

## 🧠 Explanation

- Q1 → 25% data point
- Q2 → median (50%)
- Q3 → 75% data point
- Box = middle 50% data

---

# 📄 3. 03_iqr_understanding.py

## 🔹 Purpose

- IQR concept বোঝা

---

## 🧾 Code

```python id="bp3"
sns.boxplot(
    data=tips,
    x="time",
    y="total_bill"
)
```

---

## 🧠 Explanation

- IQR = Q3 - Q1
- middle 50% data spread
- box size = variability measure

---

# 📄 4. 04_outlier_detection.py

## 🔹 Purpose

- Outlier detect করা

---

## 🧾 Code

```python id="bp4"
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill"
)
```

---

## 🧠 Explanation

- whiskers এর বাইরে points = outliers
- extreme values automatically highlight হয়

---

# 📄 5. 05_horizontal_boxplot.py

## 🔹 Purpose

- Horizontal distribution visualization

---

## 🧾 Code

```python id="bp5"
sns.boxplot(
    data=tips,
    x="total_bill",
    y="day"
)
```

---

## 🧠 Explanation

- horizontal layout readability improve করে
- multiple categories easier to compare হয়

---

# 📄 6. 06_group_comparison_boxplot.py

## 🔹 Purpose

- Gender-wise distribution comparison

---

## 🧾 Code

```python id="bp6"
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex"
)
```

---

## 🧠 Explanation

- `hue="sex"`
  - male vs female distribution compare করে

- side-by-side boxplots তৈরি হয়

---

# 📄 7. 07_real_world_analysis.py

## 🔹 Purpose

- Real-world behavior analysis করা

---

## 🧾 Code

```python id="bp7"
sns.boxplot(
    data=tips,
    x="time",
    y="tip",
    hue="smoker"
)
```

---

## 🧠 Explanation

- lunch vs dinner tip distribution
- smoker behavior difference
- variability analysis

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Numerical + categorical variables select করা হয়েছে
- `boxplot()` ব্যবহার করে distribution visualize করা হয়েছে
- Quartiles এবং IQR analyze করা হয়েছে
- Outliers detect করা হয়েছে
- Group comparison করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Box plot distribution summarize করে
- Median, spread, outliers সহজে দেখা যায়
- IQR data variability বোঝায়
- Group comparison insight তৈরি করে

---

# 🚀 What I Learned

- Statistical distribution visualization
- Quartiles concept (Q1, Q2, Q3)
- IQR meaning and usage
- Outlier detection technique
- Group-wise analysis using boxplot

---

# 🧠 Key Concepts (Quick Revision)

- `boxplot()` → distribution summary
- median → center value
- IQR → middle 50% data
- whiskers → normal range
- outliers → extreme values
- `hue` → group comparison

---

# 📝 Notes

## 📌 Common Mistakes

- outlier ignore করা
- categorical variable mismatch
- wrong interpretation of box size

## 📌 Optimization Tips

- Always check outliers in real datasets
- median is better than mean for skewed data
- use `hue` for deeper insights

---

# 📌 Next Day Preview

## 📅 Day 12 — Violin Plot

আগামী দিনে শিখবো:

- `sns.violinplot()`
- distribution + density visualization
- boxplot vs violin plot difference
- split violin plots
- advanced distribution analysis

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- different columns এ boxplot compare করো
- outlier filtering practice করো
- real CSV dataset try করো

---

## 🧪 Practice Ideas

- `tip` distribution analyze করো
- `size` vs `total_bill` boxplot বানাও
- smoker vs non-smoker spread compare করো
