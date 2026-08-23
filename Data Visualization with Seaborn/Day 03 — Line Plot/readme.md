# � Day 3 — Line Plot

---

# 🎯 Objective

- `sns.lineplot()` ব্যবহার শেখা
- Trend visualization বোঝা
- Time-series data visualize করা
- Multiple line plots তৈরি করা
- `hue`, `style`, `size` ব্যবহার শেখা
- Confidence interval (CI) বোঝা
- Error bars visualization শেখা
- Statistical trend analysis করা

---

# 📚 Topics Covered

- `sns.lineplot()`
- Trend visualization
- Multiple line plots
- `hue`
- `style`
- `size`
- Confidence interval
- Error bars
- Time-series plotting

---

# 📁 Project Structure

```bash id="9k2x7n"
day-3/
│── 01_basic_lineplot.py
│── 02_multiple_lines_hue.py
│── 03_style_size_lineplot.py
│── 04_confidence_interval.py
│── 05_error_bars_advanced.py
│── README.md
```

---

# 📊 Dataset

## 📌 Dataset 1: flights

- **Source:** Built-in Seaborn Dataset
- **Loaded Using:** `sns.load_dataset("flights")`

### 📌 Description

Airline passenger dataset যেখানে বিভিন্ন বছরের passenger trend দেখানো হয়েছে।

### 📌 Columns

- `year` → year value
- `month` → month name
- `passengers` → passenger count

---

## 📌 Dataset 2: tips

- **Source:** Built-in Seaborn Dataset
- **Loaded Using:** `sns.load_dataset("tips")`

### 📌 Description

Restaurant tipping dataset statistical visualization এর জন্য ব্যবহার করা হয়েছে।

### 📌 Columns

- `total_bill` → total bill amount
- `tip` → tip amount
- `day` → weekday
- `size` → total people
- `sex` → customer gender

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_lineplot.py

## 🔹 Purpose

- Basic line plot তৈরি করা
- Trend visualization বোঝা

---

## 🧾 Code

```python id="d7m1qk"
import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

sns.lineplot(
    data=flights,
    x="year",
    y="passengers"
)

plt.title("Passengers Over Years")
plt.show()
```

---

## 🧠 Explanation

- `sns.lineplot()`
  - Line chart তৈরি করে

- `x="year"`
  - Time axis হিসেবে year ব্যবহার করা হয়েছে

- `y="passengers"`
  - Passenger count visualize করা হয়েছে

- Plot এর line overall trend দেখায়

---

# 📄 2. 02_multiple_lines_hue.py

## 🔹 Purpose

- Multiple line visualization শেখা
- `hue` ব্যবহার করা

---

## 🧾 Code

```python id="k3m7pw"
import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

sns.lineplot(
    data=flights,
    x="year",
    y="passengers",
    hue="month"
)

plt.title("Passenger Trends by Month")

plt.legend(bbox_to_anchor=(1.05, 1))

plt.show()
```

---

## 🧠 Explanation

- `hue="month"`
  - প্রতিটি month এর জন্য আলাদা line তৈরি করে

- Different colors different categories represent করে

- `plt.legend()`
  - Legend position customize করে

---

## 📌 Key Idea

- `hue` = category-based color grouping

---

# 📄 3. 03_style_size_lineplot.py

## 🔹 Purpose

- `style` এবং `size` ব্যবহার শেখা
- Advanced line customization করা

---

## 🧾 Code

```python id="x8m0ql"
import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

sns.lineplot(
    data=flights,
    x="year",
    y="passengers",
    hue="month",
    style="month",
    size="month"
)

plt.title("Style + Size Line Plot")

plt.legend(bbox_to_anchor=(1.05, 1))

plt.show()
```

---

## 🧠 Explanation

- `hue`
  - Different colors দেয়

- `style`
  - Different line patterns দেয়

- `size`
  - Line thickness পরিবর্তন করে

---

## 📌 Key Idea

- `hue` → color
- `style` → pattern
- `size` → thickness

---

# 📄 4. 04_confidence_interval.py

## 🔹 Purpose

- Confidence interval বোঝা
- Statistical uncertainty visualize করা

---

## 🧾 Code

```python id="m5d8sr"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.lineplot(
    data=tips,
    x="size",
    y="total_bill"
)

plt.title("Confidence Interval Example")
plt.show()

sns.lineplot(
    data=tips,
    x="size",
    y="total_bill",
    errorbar=None
)

plt.title("Without Confidence Interval")
plt.show()
```

---

## 🧠 Explanation

- Default lineplot shaded confidence interval দেখায়

- Shaded area:
  - Possible variation বোঝায়

- `errorbar=None`
  - Confidence interval remove করে

---

## 📌 Key Idea

- Line = average trend
- Shaded area = uncertainty range

---

# 📄 5. 05_error_bars_advanced.py

## 🔹 Purpose

- Error bars visualize করা
- Standard deviation ও CI compare করা

---

## 🧾 Code

```python id="r2f9wn"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.lineplot(
    data=tips,
    x="day",
    y="total_bill",
    errorbar="sd"
)

plt.title("Error Bars (Standard Deviation)")
plt.show()

sns.lineplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex",
    errorbar="ci"
)

plt.title("Grouped Trend with Error Bars")
plt.show()
```

---

## 🧠 Explanation

- `errorbar="sd"`
  - Standard deviation দেখায়

- `errorbar="ci"`
  - Confidence interval দেখায়

- `hue="sex"`
  - Male/Female group compare করে

---

## 📌 Error Bar Types

- `"ci"` → confidence interval
- `"sd"` → standard deviation
- `None` → remove error bars

---

# ⚙️ Implementation Flow

- Built-in dataset load করা হয়েছে
- Basic line plot তৈরি করা হয়েছে
- Multiple lines visualize করা হয়েছে
- `hue`, `style`, `size` apply করা হয়েছে
- Confidence interval visualize করা হয়েছে
- Error bars customize করা হয়েছে
- Statistical trend analysis করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Line plots trend analysis এর জন্য খুব useful
- `hue` multiple category comparison সহজ করে
- Confidence interval uncertainty বোঝাতে সাহায্য করে
- Error bars variability visualize করে
- Seaborn statistical plotting automatically handle করে

---

# 🚀 What I Learned

- `sns.lineplot()`
- Trend visualization
- Time-series plotting
- Multiple line grouping
- Statistical visualization
- Confidence interval
- Error bars
- Advanced line customization

---

# 🧠 Key Concepts (Quick Revision)

- `lineplot()` → trend visualization
- `hue` → color grouping
- `style` → line pattern
- `size` → line thickness
- CI → confidence interval
- Error bars → variability visualization

---

# 📝 Notes

## 📌 Common Mistakes

- Too many lines ব্যবহার করা
- Legend overlap হওয়া
- Wrong x-axis selection
- Time-series data properly sort না করা

---

## 📌 Optimization Tips

- `hue` ব্যবহার করে category comparison করো
- Large legends হলে outside position ব্যবহার করো
- Time-series data sorted রাখা ভালো
- Statistical plots এর ক্ষেত্রে CI useful

---

# 📌 Next Day Preview

## 📅 Day 4 — Scatter Plot

আগামী দিনে শিখবো:

- `sns.scatterplot()`
- Correlation visualization
- Positive/negative correlation
- `hue`
- `style`
- `size`
- Bubble chart
- Categorical scatter visualization

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- Real stock market data visualize করা
- Temperature trend analysis করা
- Sales trend dashboard তৈরি করা
- Multiple subplot trend analysis করা

---

## 🧪 Practice Ideas

- `fmri` dataset দিয়ে lineplot তৈরি করো
- Different error bars compare করো
- Monthly trend visualization তৈরি করো
- `style` ও `size` combine করে custom plot তৈরি করো
