# � Day 6 — Histogram

---

# 🎯 Objective

- `sns.histplot()` ব্যবহার শেখা
- Frequency distribution বোঝা
- Data distribution visually analyze করা
- `bins` ব্যবহার করে interval control করা
- Multiple distributions compare করা
- Density histogram বোঝা
- Stacked histogram তৈরি করা
- KDE curve এর basic understanding তৈরি করা

---

# 📚 Topics Covered

- `sns.histplot()`
- Frequency distribution
- `bins`
- `multiple`
- `element`
- Density histogram
- Stacked histogram

---

# 📁 Project Structure

```bash
day-6/
│── 01_basic_histogram.py
│── 02_bins_control.py
│── 03_multiple_histograms.py
│── 04_density_histogram.py
│── 05_stacked_histogram.py
│── 06_distribution_modes.py
│── README.md
```

---

# 📊 Dataset

## 📌 Dataset Name: `tips`

- **Source:** Built-in Seaborn Dataset
- **Loaded Using:** `sns.load_dataset("tips")`

---

## 📌 Description

Restaurant tipping dataset যেখানে customer bill, tip amount, smoker status এবং gender related information রয়েছে।

---

## 📌 Columns

- `total_bill` → মোট bill amount
- `tip` → tip amount
- `sex` → customer gender
- `smoker` → smoker/non-smoker
- `day` → week day
- `time` → lunch/dinner
- `size` → group size

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_histogram.py

## 🔹 Purpose

- Basic histogram তৈরি করা
- Frequency distribution visualize করা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(
    data=tips,
    x="total_bill"
)

plt.title("Distribution of Total Bill")

plt.show()
```

---

## 🧠 Explanation

- `sns.histplot()`
  - Histogram তৈরি করে

- `x="total_bill"`
  - Bill amount distribution analyze করে

- Histogram দেখায়:
  - কোন values কতবার এসেছে

---

## 📌 Key Idea

- Histogram = frequency visualization

---

# 📄 2. 02_bins_control.py

## 🔹 Purpose

- `bins` parameter বোঝা
- Distribution detail control করা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(
    data=tips,
    x="total_bill",
    bins=5
)

plt.title("Histogram with Few Bins")

plt.show()

sns.histplot(
    data=tips,
    x="total_bill",
    bins=30
)

plt.title("Histogram with Many Bins")

plt.show()
```

---

## 🧠 Explanation

- `bins=5`
  - কম intervals তৈরি করে

- `bins=30`
  - বেশি detailed intervals তৈরি করে

- Bins পরিবর্তন করলে visualization pattern change হয়

---

## 📌 Key Idea

- Low bins → smooth overview
- High bins → detailed distribution

---

# 📄 3. 03_multiple_histograms.py

## 🔹 Purpose

- Multiple distributions compare করা
- `hue` ব্যবহার শেখা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(
    data=tips,
    x="total_bill",
    hue="smoker"
)

plt.title("Smoker vs Non-Smoker Bill Distribution")

plt.show()
```

---

## 🧠 Explanation

- `hue="smoker"`
  - Smoker এবং non-smoker groups আলাদা color এ দেখায়

- Different distributions visually compare করা যায়

---

## 📌 Key Idea

- `hue` group comparison সহজ করে

---

# 📄 4. 04_density_histogram.py

## 🔹 Purpose

- Density histogram বোঝা
- KDE overlay ব্যবহার শেখা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(
    data=tips,
    x="total_bill",
    stat="density"
)

plt.title("Density Histogram")

plt.show()

sns.histplot(
    data=tips,
    x="total_bill",
    kde=True
)

plt.title("Histogram + KDE")

plt.show()
```

---

## 🧠 Explanation

- `stat="density"`
  - Count এর পরিবর্তে probability density দেখায়

- `kde=True`
  - Smooth KDE curve add করে

- KDE distribution এর smooth pattern বুঝতে সাহায্য করে

---

## 📌 Key Idea

- Density histogram probability understanding এর জন্য useful

---

# 📄 5. 05_stacked_histogram.py

## 🔹 Purpose

- Stacked histogram তৈরি করা
- Group contribution visualize করা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(
    data=tips,
    x="total_bill",
    hue="sex",
    multiple="stack"
)

plt.title("Stacked Histogram (Male vs Female)")

plt.show()
```

---

## 🧠 Explanation

- `multiple="stack"`
  - Categories stacked form এ show করে

- Male/Female contribution একসাথে দেখা যায়

---

## 📌 Key Idea

- Total distribution + category breakdown একসাথে visualize করা যায়

---

# 📄 6. 06_distribution_modes.py

## 🔹 Purpose

- Different histogram styles compare করা
- `element` parameter শেখা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(
    data=tips,
    x="total_bill",
    element="bars"
)

plt.title("Bars Mode")

plt.show()

sns.histplot(
    data=tips,
    x="total_bill",
    element="step"
)

plt.title("Step Mode")

plt.show()

sns.histplot(
    data=tips,
    x="total_bill",
    element="step",
    fill=True
)

plt.title("Filled Step Mode")

plt.show()
```

---

## 🧠 Explanation

- `element="bars"`
  - Default histogram bars

- `element="step"`
  - Outline style histogram

- `fill=True`
  - Filled step visualization তৈরি করে

---

## 📌 Key Idea

- Different styles different visualization feel দেয়

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Basic histogram তৈরি করা হয়েছে
- Bins customize করা হয়েছে
- Multiple distributions compare করা হয়েছে
- Density histogram তৈরি করা হয়েছে
- KDE curve যোগ করা হয়েছে
- Stacked histogram visualize করা হয়েছে
- Different histogram modes compare করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Histogram data distribution বুঝতে সাহায্য করে
- Bins distribution detail control করে
- KDE curve smooth trend visualize করে
- Stacked histogram category comparison improve করে
- Density histogram probability understanding improve করে

---

# 🚀 What I Learned

- `sns.histplot()`
- Frequency distribution
- Density visualization
- KDE curve
- Bins control
- Multiple distributions
- Stacked histograms
- Histogram styling

---

# 🧠 Key Concepts (Quick Revision)

- Histogram → frequency visualization
- `bins` → interval control
- `hue` → category split
- `multiple="stack"` → stacked categories
- `stat="density"` → probability density
- `kde=True` → smooth distribution curve

---

# 📝 Notes

## 📌 Common Mistakes

- Too many bins ব্যবহার করা
- Very low bins ব্যবহার করা
- Wrong variable histogram এ ব্যবহার করা
- Overlapping distributions unclear হওয়া

---

## 📌 Optimization Tips

- Moderate bins ব্যবহার করো
- KDE ব্যবহার করে smooth pattern দেখো
- Group comparison এ `hue` ব্যবহার করো
- Stacked histogram category analysis এর জন্য useful

---

# 📌 Next Day Preview

## 📅 Day 7 — KDE Plot

আগামী দিনে শিখবো:

- `sns.kdeplot()`
- Density estimation
- Smooth distribution
- `fill=True`
- Multiple KDE plots
- Bandwidth understanding

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- Real sales distribution analysis করা
- Salary distribution histogram তৈরি করা
- Customer spending pattern analyze করা
- Custom KDE overlay dashboard তৈরি করা

---

## 🧪 Practice Ideas

- `penguins` dataset দিয়ে histogram তৈরি করো
- Different `bins` values compare করো
- KDE on/off করে difference observe করো
- Multiple category stacked histogram তৈরি করো
