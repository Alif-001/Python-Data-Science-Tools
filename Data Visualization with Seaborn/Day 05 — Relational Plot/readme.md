# 📅 Day 5 — Relational Plot

---

# 🎯 Objective

- `sns.relplot()` ব্যবহার শেখা
- Figure-level plotting বোঝা
- `kind="scatter"` ও `kind="line"` ব্যবহার করা
- Multi-variable visualization তৈরি করা
- Faceting concept বোঝা
- Row ও column based subplot তৈরি করা
- Data storytelling এর জন্য multi-panel visualization তৈরি করা

---

# 📚 Topics Covered

- `sns.relplot()`
- Figure-level plotting
- `kind='line'`
- `kind='scatter'`
- Faceting basics
- Multi-variable visualization

---

# 📁 Project Structure

```bash id="u8m2qf"
day-5/
│── 01_basic_relplot_scatter.py
│── 02_relplot_line.py
│── 03_hue_style_size_relplot.py
│── 04_faceting_basics.py
│── 05_faceting_row_col.py
│── 06_faceting_line_analysis.py
│── README.md
```

---

# 📊 Dataset

## 📌 Dataset 1: `tips`

- **Source:** Built-in Seaborn Dataset
- **Loaded Using:** `sns.load_dataset("tips")`

### 📌 Description

Restaurant tipping dataset যেখানে customer bill, tip, gender, smoker status এবং lunch/dinner information রয়েছে।

### 📌 Columns

- `total_bill` → মোট বিল
- `tip` → tip amount
- `sex` → customer gender
- `smoker` → smoker কি না
- `time` → lunch/dinner
- `size` → group size

---

## 📌 Dataset 2: `flights`

- **Source:** Built-in Seaborn Dataset
- **Loaded Using:** `sns.load_dataset("flights")`

### 📌 Description

Airline passenger trend dataset যেখানে year-wise passenger information রয়েছে।

### 📌 Columns

- `year` → year value
- `month` → month name
- `passengers` → passenger count

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_relplot_scatter.py

## 🔹 Purpose

- Basic `relplot()` ব্যবহার শেখা
- Figure-level scatter visualization তৈরি করা

---

## 🧾 Code

```python id="h3k7wr"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.relplot(
    data=tips,
    x="total_bill",
    y="tip",
    kind="scatter"
)

plt.title("Relplot - Scatter Example")

plt.show()
```

---

## 🧠 Explanation

- `sns.relplot()`
  - Figure-level plotting function

- `kind="scatter"`
  - Scatter plot mode activate করে

- Automatically figure layout manage করে

---

## 📌 Key Idea

- `relplot()` = plotting + figure management

---

# 📄 2. 02_relplot_line.py

## 🔹 Purpose

- Line visualization using `relplot()`
- Trend analysis করা

---

## 🧾 Code

```python id="m5v8qs"
import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

sns.relplot(
    data=flights,
    x="year",
    y="passengers",
    kind="line"
)

plt.title("Relplot - Line Plot Example")

plt.show()
```

---

## 🧠 Explanation

- `kind="line"`
  - Line plot তৈরি করে

- Time-series trend visualize করা হয়েছে

- Passenger growth over years analyze করা হয়েছে

---

## 📌 Key Idea

- Line plots trends বোঝার জন্য useful

---

# 📄 3. 03_hue_style_size_relplot.py

## 🔹 Purpose

- Multi-variable visualization তৈরি করা
- `hue`, `style`, `size` combine করা

---

## 🧾 Code

```python id="k9t1zc"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.relplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    size="size",
    style="time",
    kind="scatter"
)

plt.title("Multi-variable Relplot")

plt.show()
```

---

## 🧠 Explanation

- `hue`
  - Color grouping

- `size`
  - Bubble size control

- `style`
  - Marker style control

- Multiple variables একসাথে visualize করা হয়েছে

---

## 📌 Key Idea

- One plot এ ৪টি variables visualize করা যায়

---

# 📄 4. 04_faceting_basics.py

## 🔹 Purpose

- Faceting concept শেখা
- Category-wise subplot তৈরি করা

---

## 🧾 Code

```python id="q2f6nw"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.relplot(
    data=tips,
    x="total_bill",
    y="tip",
    col="sex"
)

plt.show()
```

---

## 🧠 Explanation

- `col="sex"`
  - Gender অনুযায়ী আলাদা subplot তৈরি করে

- Male এবং Female data visually compare করা যায়

---

## 📌 Key Idea

- Faceting = data split into multiple plots

---

# 📄 5. 05_faceting_row_col.py

## 🔹 Purpose

- Advanced faceting শেখা
- Row + column subplot visualization তৈরি করা

---

## 🧾 Code

```python id="v4m8ry"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.relplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="time",
    col="sex",
    row="smoker",
    kind="scatter"
)

plt.show()
```

---

## 🧠 Explanation

- `row="smoker"`
  - Vertical subplot split করে

- `col="sex"`
  - Horizontal subplot split করে

- Multiple mini graphs তৈরি হয়

---

## 📌 Key Idea

- Row = vertical split
- Col = horizontal split

---

# 📄 6. 06_faceting_line_analysis.py

## 🔹 Purpose

- Faceted line analysis করা
- Month-wise trend comparison করা

---

## 🧾 Code

```python id="y7n2kp"
import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

sns.relplot(
    data=flights,
    x="year",
    y="passengers",
    hue="month",
    col="month",
    kind="line",
    col_wrap=4
)

plt.show()
```

---

## 🧠 Explanation

- `col="month"`
  - প্রতিটি month এর জন্য আলাদা plot তৈরি করে

- `col_wrap=4`
  - প্রতি row তে ৪টি subplot রাখে

- Month-wise trends compare করা যায়

---

## 📌 Key Idea

- Faceting complex analysis সহজ করে

---

# ⚙️ Implementation Flow

- Built-in datasets load করা হয়েছে
- `relplot()` ব্যবহার করা হয়েছে
- Scatter ও line relational plots তৈরি করা হয়েছে
- Multi-variable visualization করা হয়েছে
- Faceting apply করা হয়েছে
- Row/column subplot তৈরি করা হয়েছে
- Trend comparison করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- `relplot()` figure-level visualization সহজ করে
- Faceting category comparison improve করে
- Multi-panel plots complex analysis সহজ করে
- `hue`, `style`, `size` multi-variable storytelling improve করে
- Line relational plots trend analysis এর জন্য powerful

---

# 🚀 What I Learned

- `sns.relplot()`
- Figure-level plotting
- Scatter relational plots
- Line relational plots
- Faceting
- Multi-variable visualization
- Row/column subplot design
- Data storytelling

---

# 🧠 Key Concepts (Quick Revision)

- `relplot()` → figure-level plot
- `kind="scatter"` → scatter relational plot
- `kind="line"` → line relational plot
- `col` → horizontal faceting
- `row` → vertical faceting
- `col_wrap` → subplot wrapping

---

# 📝 Notes

## 📌 Common Mistakes

- Too many facets তৈরি করা
- Small figure size রাখা
- Legend overlap হওয়া
- Too many variables এক plot এ ব্যবহার করা

---

## 📌 Optimization Tips

- `col_wrap` ব্যবহার করে layout সুন্দর রাখো
- Small datasets এ faceting বেশি useful
- `hue` ও `style` carefully ব্যবহার করো
- Figure-level plots presentation এর জন্য excellent

---

# 📌 Next Day Preview

## 📅 Day 6 — Histogram

আগামী দিনে শিখবো:

- `sns.histplot()`
- Frequency distribution
- `bins`
- `multiple`
- `element`
- Density histogram
- Stacked histogram

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- Sales dashboard relational plots তৈরি করা
- Customer segmentation faceting করা
- Time-series faceted analysis তৈরি করা
- Multi-panel EDA dashboard তৈরি করা

---

## 🧪 Practice Ideas

- `fmri` dataset দিয়ে `relplot()` তৈরি করো
- Different faceting combinations try করো
- `kind="line"` ও `kind="scatter"` compare করো
- `col_wrap` change করে layout observe করো
