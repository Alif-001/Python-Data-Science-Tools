# 📅 Day 24 — Statistical Visualization

---

# 🎯 Objective

- Mean vs median ধারণা বোঝা
- Confidence interval visualization শেখা
- Distribution comparison করা
- Boxplot দিয়ে statistical summary বোঝা
- Data storytelling skill develop করা

---

# 📚 Topics Covered

- Mean visualization (`barplot`)
- Median vs Mean comparison
- Confidence interval concept
- Distribution comparison (`histplot`)
- Statistical summary (`boxplot`)
- Statistical storytelling

---

# 📁 Project Structure

```bash id="d24-structure"
day-24/
│── 01_mean_barplot.py
│── 02_median_comparison.py
│── 03_confidence_interval_plot.py
│── 04_distribution_comparison.py
│── 05_boxplot_story.py
│── 06_student_scores_analysis.py
│── 07_real_world_storytelling.py
│── student_scores.csv
│── README.md
```

---

# 📊 Dataset

## 📌 File Name: `student_scores.csv`

## 📌 Description

এই dataset এ students এর বিভিন্ন subject এর marks দেওয়া আছে, যা statistical analysis শেখার জন্য ব্যবহার করা হয়েছে।

---

## 📌 Columns

- `student` → student name
- `math` → mathematics score
- `physics` → physics score
- `chemistry` → chemistry score

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_mean_barplot.py

## 🔹 Purpose

- Mean value visualize করা
- Basic statistical aggregation বোঝা

## 🧾 Code

```python id="d24-1"
sns.barplot(data=tips, x="day", y="total_bill")
```

## 🧠 Explanation

- প্রতিদিনের average bill দেখায়
- Bar height = mean value
- Default estimator = mean

---

# 📄 2. 02_median_comparison.py

## 🔹 Purpose

- Mean vs median তুলনা করা
- Skewness ধারণা বোঝা

## 🧾 Code

```python id="d24-2"
mean_vals = tips.groupby("day")["total_bill"].mean()
median_vals = tips.groupby("day")["total_bill"].median()
```

## 🧠 Explanation

- Mean sensitive to outliers
- Median robust measure
- Difference = data distribution insight

---

# 📄 3. 03_confidence_interval_plot.py

## 🔹 Purpose

- Confidence interval বোঝা
- Uncertainty visualization

## 🧾 Code

```python id="d24-3"
sns.lineplot(data=tips, x="day", y="total_bill")
```

## 🧠 Explanation

- Shaded area = confidence interval
- Data uncertainty represent করে
- Trend reliability বোঝায়

---

# 📄 4. 04_distribution_comparison.py

## 🔹 Purpose

- Male vs Female spending distribution compare করা

## 🧾 Code

```python id="d24-4"
sns.histplot(
    data=tips,
    x="total_bill",
    hue="sex",
    kde=True,
    multiple="stack"
)
```

## 🧠 Explanation

- Distribution shape compare করা হয়
- KDE = smooth curve
- Stack = group-wise comparison

---

# 📄 5. 05_boxplot_story.py

## 🔹 Purpose

- Full statistical summary visualization

## 🧾 Code

```python id="d24-5"
sns.boxplot(data=tips, x="day", y="total_bill")
```

## 🧠 Explanation

- Median line দেখায়
- IQR (spread) দেখায়
- Outliers detect করে

---

# 📄 6. 06_student_scores_analysis.py

## 🔹 Purpose

- Real dataset analysis
- Subject-wise performance compare করা

## 🧾 Code

```python id="d24-6"
mean_scores = df[["math", "physics", "chemistry"]].mean()

sns.barplot(x=mean_scores.index, y=mean_scores.values)
```

## 🧠 Explanation

- Subject-wise average score বের করা হয়েছে
- Hardest vs easiest subject বোঝা যায়

---

# 📄 7. 07_real_world_storytelling.py

## 🔹 Purpose

- Statistical storytelling তৈরি করা
- Boxplot + raw data combine করা

## 🧾 Code

```python id="d24-7"
sns.boxplot(data=tips, x="day", y="total_bill")
sns.stripplot(data=tips, x="day", y="total_bill", alpha=0.4)
```

## 🧠 Explanation

- Box = summary
- Points = actual data
- Combined view = full story

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Groupby analysis করা হয়েছে
- Mean/median calculate করা হয়েছে
- Distribution compare করা হয়েছে
- Statistical plots তৈরি করা হয়েছে
- Story-based visualization করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Mean vs median difference skewness বুঝায়
- Boxplot data spread clearly দেখায়
- Distribution comparison pattern reveal করে
- Confidence interval uncertainty দেখায়

---

# 🚀 What I Learned

- Mean vs median concept
- Statistical visualization techniques
- Distribution analysis
- Confidence interval interpretation
- Data storytelling skills

---

# 🧠 Key Concepts (Quick Revision)

- Mean → average value
- Median → middle value
- Boxplot → full distribution summary
- Histogram → distribution shape
- CI → uncertainty range

---

# 📝 Notes

## 📌 Mistakes

- Outliers ignore করলে wrong mean interpretation হয়
- KDE ছাড়া distribution unclear হতে পারে

## 📌 Optimization Tips

- Always compare mean + median together
- Boxplot + stripplot = best storytelling combo

---

# 📌 Next Day Preview

## 📅 Day 25 — Advanced Color Palettes

- Color theory in visualization
- Sequential vs diverging palettes
- Custom palette creation
- Better visual storytelling design

---

# ⭐ Bonus

## 🔥 Improvements Ideas

- Real company sales data analyze করা
- Exam result analysis project বানানো
- Customer spending distribution study করা

---

## 🧪 Practice Ideas

- Different days compare করো
- Male vs Female spending deeper analysis করো
- Boxplot vs violin plot compare করো
