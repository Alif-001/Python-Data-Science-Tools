# 📅 Day 4 — Scatter Plot

---

# 🎯 Objective

- `sns.scatterplot()` ব্যবহার শেখা
- Correlation visualization বোঝা
- Positive ও negative relationship analyze করা
- `hue`, `style`, `size` ব্যবহার শেখা
- Bubble chart তৈরি করা
- Categorical scatter visualization করা
- Real-world data relationship visually analyze করা

---

# 📚 Topics Covered

- `sns.scatterplot()`
- Correlation visualization
- Positive/negative correlation
- `hue`
- `style`
- `size`
- Bubble chart
- Categorical scatter visualization

---

# 📁 Project Structure

```bash id="f2m8q1"
day-4/
│── 01_basic_scatterplot.py
│── 02_correlation_hue.py
│── 03_bubble_chart_size_style.py
│── 04_style_marker_scatter.py
│── 05_categorical_scatter_analysis.py
│── README.md
```

---

# 📊 Dataset

## 📌 Dataset Name: `tips`

- **Source:** Built-in Seaborn Dataset
- **Loaded Using:** `sns.load_dataset("tips")`

---

## 📌 Description

Restaurant tipping dataset যেখানে customer bill, tip amount, gender, lunch/dinner এবং group size সম্পর্কিত তথ্য রয়েছে।

---

## 📌 Columns

- `total_bill` → মোট বিল
- `tip` → tip amount
- `sex` → customer gender
- `smoker` → smoker কি না
- `day` → সপ্তাহের দিন
- `time` → lunch/dinner
- `size` → group size

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_scatterplot.py

## 🔹 Purpose

- Basic scatter plot তৈরি করা
- Variables এর relationship visualize করা
- Correlation concept বোঝা

---

## 🧾 Code

```python id="g7k1xp"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
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
  - Y-axis এ tip amount দেখানো হয়েছে

- প্রতিটি dot একজন customer represent করে

---

## 📌 Key Idea

- Variables এর relationship visually বোঝা যায়
- Positive trend দেখা যায়:
  - Bill বাড়লে tip ও বাড়ে

---

# 📄 2. 02_correlation_hue.py

## 🔹 Purpose

- Category-based scatter analysis করা
- `hue` ব্যবহার শেখা

---

## 🧾 Code

```python id="n8v2qc"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex"
)

plt.title("Correlation with Gender (Hue)")
plt.show()
```

---

## 🧠 Explanation

- `hue="sex"`
  - Male/Female অনুযায়ী different colors apply করে

- Different groups visually compare করা যায়

- Category-based patterns detect করা সহজ হয়

---

## 📌 Key Idea

- `hue` → category color encoding

---

# 📄 3. 03_bubble_chart_size_style.py

## 🔹 Purpose

- Bubble chart তৈরি করা
- Third variable visualize করা

---

## 🧾 Code

```python id="v5x9mb"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="time",
    size="size",
    sizes=(20, 200)
)

plt.title("Bubble Chart: Bill vs Tip vs Group Size")

plt.legend(bbox_to_anchor=(1.05, 1))

plt.show()
```

---

## 🧠 Explanation

- `size="size"`
  - Bubble size group size অনুযায়ী পরিবর্তন হয়

- `sizes=(20, 200)`
  - Bubble size range control করে

- `hue="time"`
  - Lunch/Dinner category color apply করে

---

## 📌 Key Idea

- X-axis → input feature
- Y-axis → output feature
- Size → importance/value
- Hue → category

---

# 📄 4. 04_style_marker_scatter.py

## 🔹 Purpose

- Marker style customization শেখা
- `style` parameter ব্যবহার করা

---

## 🧾 Code

```python id="r3t0wf"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    style="time"
)

plt.title("Scatter Plot with Style + Hue")

plt.show()
```

---

## 🧠 Explanation

- `hue`
  - Color difference তৈরি করে

- `style`
  - Different marker shapes ব্যবহার করে

- Different categories visually আলাদা করা সহজ হয়

---

## 📌 Key Idea

- `hue` → color grouping
- `style` → shape grouping

---

# 📄 5. 05_categorical_scatter_analysis.py

## 🔹 Purpose

- Real-world categorical analysis করা
- Multiple encodings combine করা

---

## 🧾 Code

```python id="t1q8zn"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
    data=tips,
    x="day",
    y="tip",
    hue="sex",
    style="time",
    size="total_bill",
    sizes=(20, 200)
)

plt.title("Categorical Scatter Analysis")

plt.show()
```

---

## 🧠 Explanation

- `x="day"`
  - Category-based visualization তৈরি করে

- `size="total_bill"`
  - Bubble size bill amount represent করে

- Multiple variables এক plot এ visualize করা হয়েছে

---

## 📌 Key Idea

- Real-world multi-variable analysis possible
- Category comparison সহজ হয়

---

# ⚙️ Implementation Flow

- Built-in dataset load করা হয়েছে
- Basic scatter plot তৈরি করা হয়েছে
- Correlation analyze করা হয়েছে
- `hue` ব্যবহার করে category comparison করা হয়েছে
- Bubble chart তৈরি করা হয়েছে
- `style` ব্যবহার করে marker customization করা হয়েছে
- Multi-variable categorical analysis করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Scatter plot variables এর relationship বুঝতে সাহায্য করে
- Positive correlation visually detect করা যায়
- `hue` category analysis সহজ করে
- Bubble charts third variable visualize করতে useful
- Multiple encodings complex insights বের করতে সাহায্য করে

---

# 🚀 What I Learned

- `sns.scatterplot()`
- Correlation analysis
- Bubble chart visualization
- `hue`
- `style`
- `size`
- Multi-variable visualization
- Categorical scatter analysis

---

# 🧠 Key Concepts (Quick Revision)

- Scatter plot → relationship visualization
- Positive correlation → both variables increase together
- Negative correlation → one increases, another decreases
- `hue` → color grouping
- `style` → marker shape
- `size` → bubble size encoding

---

# 📝 Notes

## 📌 Common Mistakes

- Too many categories ব্যবহার করা
- Overlapping points তৈরি হওয়া
- Wrong axis selection
- Bubble size খুব বড় রাখা

---

## 📌 Optimization Tips

- `alpha` ব্যবহার করে overlap কমানো যায়
- `hue` category comparison এর জন্য useful
- Bubble charts এ balanced size range ব্যবহার করো
- Legend outside রাখলে readability বাড়ে

---

# 📌 Next Day Preview

## 📅 Day 5 — Relational Plot

আগামী দিনে শিখবো:

- `sns.relplot()`
- Figure-level plotting
- `kind='line'`
- `kind='scatter'`
- Faceting basics
- Multi-variable visualization

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- Real stock market scatter analysis করা
- Sales vs profit visualization তৈরি করা
- Customer segmentation scatter analysis করা
- Multiple subplot scatter dashboard তৈরি করা

---

## 🧪 Practice Ideas

- `iris` dataset এ scatterplot তৈরি করো
- Bubble chart ব্যবহার করে custom visualization তৈরি করো
- Different `style` markers compare করো
- Positive ও negative correlation examples তৈরি করো
