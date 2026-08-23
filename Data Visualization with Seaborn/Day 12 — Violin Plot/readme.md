# 📅 Day 12 — Violin Plot

---

# 🎯 Objective

- Seaborn-এর মাধ্যমে distribution shape বুঝতে শেখা
- `sns.violinplot()` ব্যবহার করে full distribution visualize করা
- Box plot + KDE একসাথে কিভাবে কাজ করে তা বোঝা
- `split=True` ব্যবহার করে group comparison করা
- `inner` option দিয়ে quartiles, points, box display করা
- Real-world distribution analysis করা

---

# 📚 Topics Covered

- `sns.violinplot()`
- Density + boxplot combination
- Split violin plot
- Inner quartiles
- `hue` based group comparison
- Distribution shape analysis
- Box plot vs violin plot

---

# 📁 Project Structure

```bash
day-12/
│── 01_basic_violinplot.py
│── 02_violin_vs_box.py
│── 03_inner_quartiles.py
│── 04_split_violin.py
│── 05_density_understanding.py
│── 06_group_comparison_violin.py
│── 07_real_world_analysis.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (`tips`)
- **Description:** Restaurant tipping dataset যেখানে customer bill, tip, day, time, gender, smoker status ইত্যাদি information আছে
- **Loaded Using:** `sns.load_dataset("tips")`

## 📌 Columns

- `total_bill` → মোট bill amount
- `tip` → tip amount
- `sex` → gender
- `smoker` → smoker status
- `day` → week day
- `time` → lunch/dinner
- `size` → group size

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_violinplot.py

## 🔹 Purpose

- Basic violin plot তৈরি করা
- Distribution shape visualize করা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.violinplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title("Violin Plot: Total Bill per Day")
plt.show()
```

## 🧠 Explanation

- `sns.violinplot()`
  - data distribution-এর full shape দেখায়

- `x="day"`
  - day-wise category দেখায়

- `y="total_bill"`
  - numerical distribution দেখায়

- wide অংশ মানে বেশি data points, thin অংশ মানে কম data points

---

# 📄 2. 02_violin_vs_box.py

## 🔹 Purpose

- Box plot এবং violin plot compare করা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.boxplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title("Box Plot (Summary)")
plt.show()

sns.violinplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title("Violin Plot (Full Distribution)")
plt.show()
```

## 🧠 Explanation

- `boxplot()`
  - only summary statistics দেখায়

- `violinplot()`
  - full distribution shape দেখায়

- box = compact summary
- violin = deeper distribution view

---

# 📄 3. 03_inner_quartiles.py

## 🔹 Purpose

- Violin plot এর ভিতরে quartiles দেখানো

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.violinplot(
    data=tips,
    x="day",
    y="total_bill",
    inner="quartile"
)

plt.title("Violin Plot with Quartiles")
plt.show()
```

## 🧠 Explanation

- `inner="quartile"`
  - Q1, median, Q3 দেখায়

- distribution-এর সাথে summary line add হয়
- `inner="box"`, `inner="point"`, `inner=None` ব্যবহার করা যায়

---

# 📄 4. 04_split_violin.py

## 🔹 Purpose

- দুটি group একসাথে compare করা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.violinplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex",
    split=True
)

plt.title("Split Violin: Male vs Female")
plt.show()
```

## 🧠 Explanation

- `hue="sex"`
  - group তৈরি করে

- `split=True`
  - একই violin-এর দুই পাশে দুই group দেখায়

- left side = one group
- right side = another group

---

# 📄 5. 05_density_understanding.py

## 🔹 Purpose

- Density concept বোঝা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.violinplot(
    data=tips,
    x="time",
    y="tip",
    inner="point"
)

plt.title("Tip Distribution Density")
plt.show()
```

## 🧠 Explanation

- thick area = বেশি density
- thin area = কম density
- violin plot actually KDE-based shape show করে

---

# 📄 6. 06_group_comparison_violin.py

## 🔹 Purpose

- Different groups compare করা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.violinplot(
    data=tips,
    x="day",
    y="tip",
    hue="smoker"
)

plt.title("Smoker vs Non-Smoker Tip Distribution")
plt.show()
```

## 🧠 Explanation

- smoker vs non-smoker distribution compare করা হয়
- শুধু average না, পুরো shape দেখা যায়
- behavior pattern analysis এর জন্য useful

---

# 📄 7. 07_real_world_analysis.py

## 🔹 Purpose

- Real-world spending behavior analyze করা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.violinplot(
    data=tips,
    x="time",
    y="total_bill",
    hue="sex",
    split=True
)

plt.title("Lunch vs Dinner Spending Distribution")
plt.show()
```

## 🧠 Explanation

- lunch vs dinner spending pattern compare করা হয়
- gender-based split violin analysis করা হয়
- average-এর বাইরে full distribution behavior দেখা যায়

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Categorical এবং numerical data select করা হয়েছে
- `violinplot()` দিয়ে distribution shape visualize করা হয়েছে
- `inner` option দিয়ে quartiles বা points দেখানো হয়েছে
- `hue` এবং `split=True` দিয়ে group comparison করা হয়েছে
- Real-world distribution insight বের করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Violin plot distribution-এর full shape দেখায়
- Density বেশি হলে plot wide হয়
- Quartiles and median ভিতরে দেখা যায়
- Group comparison আরও informative হয়
- Box plot এর তুলনায় violin plot বেশি detailed

---

# 🚀 What I Learned

- Full distribution shape analysis
- Box plot vs violin plot difference
- KDE-based visualization
- Quartiles visualization inside violin
- Split violin technique
- Advanced group-wise comparison

---

# 🧠 Key Concepts (Quick Revision)

- `violinplot()` → distribution shape দেখায়
- wide area → বেশি density
- thin area → কম density
- `inner="quartile"` → quartile lines দেখায়
- `split=True` → দুই group একই plot এ compare করে
- `hue` → subgroup split করে

---

# 📝 Notes

## 📌 Common Mistakes

- boxplot আর violinplot confuse করা
- `split=True` ব্যবহার করতে ভুল করা
- wrong `hue` column দেওয়া

## 📌 Optimization Tips

- skewed data analyze করতে violin plot খুব useful
- distribution shape বুঝতে boxplot-এর সাথে compare করো
- business/customer behavior analysis এ apply করো

---

# 📌 Next Day Preview

## 📅 Day 13 — Strip Plot & Swarm Plot

আগামী দিনে শিখবো:

- `sns.stripplot()`
- `sns.swarmplot()`
- overlapping points handling
- jitter concept
- categorical scatter visualization

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- different datasets এ violin plot try করো
- `inner` options compare করো
- `split=True` vs `False` analysis করো

---

## 🧪 Practice Ideas

- `tip` distribution by `day` analyze করো
- `total_bill` by `time` compare করো
- smoker vs non-smoker violin plot বানাও
- `sex` অনুযায়ী spending shape compare করো
