# 📅 Day 10 — Bar Plot

---

# 🎯 Objective

- Statistical visualization বোঝা (count না, এখন average/summary)
- `sns.barplot()` ব্যবহার করে mean visualization করা
- Different statistical functions (mean, median, max, min) বোঝা
- Group-wise comparison করা
- Error bars কী এবং কেন দরকার তা শেখা
- Real-world business analysis style visualization করা

---

# 📚 Topics Covered

- `sns.barplot()`
- Mean visualization (default behavior)
- `estimator` function (mean, median, max, min)
- Group comparison using `hue`
- Error bars (CI, SD, None)
- Statistical summary vs frequency
- Business analytics style plotting

---

# 📁 Project Structure

```bash
day-10/
│── 01_basic_barplot_mean.py
│── 02_estimator_basics.py
│── 03_max_min_barplot.py
│── 04_group_comparison_hue.py
│── 05_error_bars.py
│── 06_multiple_group_analysis.py
│── 07_real_world_business_analysis.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (tips)
- **Source:** Seaborn built-in dataset
- **Loaded Using:** `sns.load_dataset("tips")`

---

## 📌 Description

Restaurant tipping dataset যেখানে customer behavior, bill amount, tip, gender, smoking status, day, time ইত্যাদি তথ্য আছে।

---

## 📌 Columns

- `total_bill` → মোট বিল
- `tip` → টিপ amount
- `sex` → gender
- `smoker` → smoker কিনা
- `day` → day of week
- `time` → lunch/dinner
- `size` → group size

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_barplot_mean.py

## 🔹 Purpose

- Basic average visualization করা
- প্রতিটি category এর mean value দেখানো

---

## 🧾 Code

```python id="bar1"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.barplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title("Average Total Bill per Day")
plt.show()
```

---

## 🧠 Explanation

- `sns.barplot()`
  - প্রতিটি category এর **mean value** দেখায়

- `x="day"`
  - category axis

- `y="total_bill"`
  - numerical value

---

# 📄 2. 02_estimator_basics.py

## 🔹 Purpose

- Different statistical functions ব্যবহার করা

---

## 🧾 Code

```python id="bar2"
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")

sns.barplot(
    data=tips,
    x="day",
    y="total_bill",
    estimator=np.mean
)
```

---

## 🧠 Explanation

- `estimator`
  - কিভাবে aggregation হবে তা define করে

- `np.mean`
  - default average calculation

- `np.median`
  - middle value based summary

---

# 📄 3. 03_max_min_barplot.py

## 🔹 Purpose

- Max / Min value analysis করা

---

## 🧾 Code

```python id="bar3"
sns.barplot(
    data=tips,
    x="day",
    y="total_bill",
    estimator=np.max
)
```

---

## 🧠 Explanation

- `np.max` → highest bill per group
- `np.min` → lowest bill per group
- extreme value analysis করা যায়

---

# 📄 4. 04_group_comparison_hue.py

## 🔹 Purpose

- Gender based comparison করা

---

## 🧾 Code

```python id="bar4"
sns.barplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex"
)
```

---

## 🧠 Explanation

- `hue="sex"`
  - male vs female comparison

- side-by-side grouped bars তৈরি হয়

---

# 📄 5. 05_error_bars.py

## 🔹 Purpose

- Data variability বোঝা

---

## 🧾 Code

```python id="bar5"
sns.barplot(
    data=tips,
    x="day",
    y="total_bill",
    errorbar="ci"
)
```

---

## 🧠 Explanation

- `errorbar="ci"`
  - confidence interval দেখায়

- `errorbar="sd"`
  - standard deviation দেখায়

- `errorbar=None`
  - error bars বন্ধ করে

---

# 📄 6. 06_multiple_group_analysis.py

## 🔹 Purpose

- Multi-category comparison করা

---

## 🧾 Code

```python id="bar6"
sns.barplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="smoker"
)
```

---

## 🧠 Explanation

- smoker vs non-smoker comparison
- group-wise behavior analysis

---

# 📄 7. 07_real_world_business_analysis.py

## 🔹 Purpose

- Real-world business insight তৈরি করা

---

## 🧾 Code

```python id="bar7"
sns.barplot(
    data=tips,
    x="time",
    y="tip",
    hue="sex"
)
```

---

## 🧠 Explanation

- lunch vs dinner tipping behavior
- gender-based customer insight
- business decision making support

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Categorical + numerical variables select করা হয়েছে
- Mean-based aggregation করা হয়েছে
- `estimator` দিয়ে statistical function apply করা হয়েছে
- `hue` দিয়ে subgroup comparison করা হয়েছে
- Error bars দিয়ে variability analysis করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Bar plot শুধু count না, **statistical summary** দেখায়
- Mean, median, max, min সহজে compare করা যায়
- Error bars data variability বোঝায়
- Group comparison business insight দেয়

---

# 🚀 What I Learned

- Statistical visualization concept
- `sns.barplot()` usage
- Aggregation functions (mean, median, max, min)
- Error bars interpretation
- Group-wise analysis

---

# 🧠 Key Concepts (Quick Revision)

- `barplot()` → statistical summary visualization
- `estimator` → calculation method define করে
- `hue` → subgroup comparison
- `errorbar` → uncertainty/variability দেখায়
- Mean ≠ count (important difference)

---

# 📝 Notes

## 📌 Common Mistakes

- `estimator` ভুলভাবে ব্যবহার করা
- categorical vs numerical confusion
- errorbars ignore করা

## 📌 Optimization Tips

- Business analysis এ always `hue` use করো
- errorbars দিয়ে data reliability check করো
- median sometimes mean থেকে better insight দেয়

---

# 📌 Next Day Preview

## 📅 Day 11 — Box Plot

আগামী দিনে শিখবো:

- `sns.boxplot()`
- quartiles & IQR
- outlier detection
- distribution comparison
- statistical spread visualization

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- different estimators compare করো
- real dataset (CSV) দিয়ে barplot practice করো
- business KPI analysis try করো

---

## 🧪 Practice Ideas

- `tip` vs `day` median compare করো
- `size` vs `total_bill` analysis করো
- smoker vs non-smoker spending pattern বের করো
