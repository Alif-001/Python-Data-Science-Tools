# 📅 Day 17 — Joint Plot

---

# 🎯 Objective

- Seaborn-এর focused 2-variable deep analysis tool শেখা
- `sns.jointplot()` ব্যবহার করে relationship + distribution একসাথে দেখা
- `kind="scatter"`, `kind="kde"`, `kind="hex"`, `kind="reg"` বুঝা
- Two-variable correlation analysis করা
- Real-world trend discovery করা

---

# 📚 Topics Covered

- `sns.jointplot()`
- Scatter + distribution visualization
- `kind="scatter"`
- `kind="kde"`
- `kind="hex"`
- `kind="reg"`
- `hue` based comparison
- Jointplot vs Pairplot

---

# 📁 Project Structure

```bash id="day17"
day-17/
│── 01_basic_jointplot.py
│── 02_jointplot_kde.py
│── 03_jointplot_hex.py
│── 04_regression_jointplot.py
│── 05_jointplot_hue.py
│── 06_real_world_joint_analysis.py
│── 07_jointplot_vs_pairplot.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (`tips`)
- **Source:** Seaborn built-in dataset
- **Loaded Using:** `sns.load_dataset("tips")`

---

## 📌 Description

Restaurant tipping dataset যেখানে `total_bill`, `tip`, `sex`, `smoker`, `day`, `time`, `size` ইত্যাদি information থাকে।
এই dataset দুই variable-এর relationship বোঝার জন্য খুব useful।

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

# 📄 1. 01_basic_jointplot.py

## 🔹 Purpose

- Basic jointplot তৈরি করা
- দুই variable-এর relationship দেখা

---

## 🧾 Code

```python id="jp1"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip",
    kind="scatter"
)

plt.show()
```

---

## 🧠 Explanation

- `sns.jointplot()`
  - middle plot এ দুই variable-এর relationship দেখায়

- side plots এ each variable-এর distribution দেখায়
- `kind="scatter"`
  - raw point relationship visualize করে

---

# 📄 2. 02_jointplot_kde.py

## 🔹 Purpose

- Density-based relationship analysis করা

---

## 🧾 Code

```python id="jp2"
sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip",
    kind="kde",
    fill=True
)
```

---

## 🧠 Explanation

- `kind="kde"`
  - density contour দেখায়

- `fill=True`
  - density area fill করে

- বেশি dense region = বেশি data points

---

# 📄 3. 03_jointplot_hex.py

## 🔹 Purpose

- Large data-friendly visualization করা

---

## 🧾 Code

```python id="jp3"
sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip",
    kind="hex"
)
```

---

## 🧠 Explanation

- `kind="hex"`
  - hexagonal bins দিয়ে density দেখায়

- বড় dataset এ খুব useful
- point overlap problem কমে যায়

---

# 📄 4. 04_regression_jointplot.py

## 🔹 Purpose

- Trend line সহ analysis করা

---

## 🧾 Code

```python id="jp4"
sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip",
    kind="reg"
)
```

---

## 🧠 Explanation

- `kind="reg"`
  - regression line add করে

- relationship-এর direction বোঝা যায়
- positive correlation আছে কিনা identify করা যায়

---

# 📄 5. 05_jointplot_hue.py

## 🔹 Purpose

- Group-based comparison করা

---

## 🧾 Code

```python id="jp5"
sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    kind="scatter"
)
```

---

## 🧠 Explanation

- `hue="sex"`
  - male/female different color এ দেখায়

- same relationship-এর মধ্যে subgroup analysis possible হয়

---

# 📄 6. 06_real_world_joint_analysis.py

## 🔹 Purpose

- Real-world business insight বের করা

---

## 🧾 Code

```python id="jp6"
sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip",
    kind="reg"
)
```

---

## 🧠 Explanation

- bigger bill হলে bigger tip আসে কিনা দেখা যায়
- business correlation analysis করা হয়
- practical insight discover করা যায়

---

# 📄 7. 07_jointplot_vs_pairplot.py

## 🔹 Purpose

- Jointplot vs Pairplot compare করা

---

## 🧾 Code

```python id="jp7"
sns.pairplot(tips[["total_bill", "tip", "size"]])

sns.jointplot(
    data=tips,
    x="total_bill",
    y="tip",
    kind="scatter"
)
```

---

## 🧠 Explanation

- `pairplot()`
  - সব variable একসাথে overview দেয়

- `jointplot()`
  - শুধু 2 variable deep dive করে

- overview vs focused analysis difference বোঝা যায়

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Two numeric columns select করা হয়েছে
- `jointplot()` দিয়ে relationship visualize করা হয়েছে
- Different `kind` ব্যবহার করে বিভিন্ন analysis করা হয়েছে
- `hue` দিয়ে group comparison করা হয়েছে
- Pairplot-এর সাথে jointplot compare করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- দুই variable-এর relationship সহজে বোঝা যায়
- Distribution + correlation একসাথে দেখা যায়
- regression line trend analysis help করে
- hex এবং kde density view দেয়
- jointplot focused deep analysis tool হিসেবে কাজ করে

---

# 🚀 What I Learned

- Two-variable deep analysis
- Scatter, KDE, Hex, Regression visualization
- Distribution + relationship একসাথে দেখার technique
- `hue` based subgroup analysis
- Jointplot vs Pairplot difference

---

# 🧠 Key Concepts (Quick Revision)

- `jointplot()` → 2 variable focused analysis
- `kind="scatter"` → raw points
- `kind="kde"` → density map
- `kind="hex"` → hexbin density
- `kind="reg"` → trend line
- `hue` → group separation

---

# 📝 Notes

## 📌 Common Mistakes

- wrong columns ব্যবহার করা
- large data এ scatter overlap ignore করা
- `kind` ভুলভাবে choose করা

## 📌 Optimization Tips

- deep dive analysis-এর জন্য jointplot use করো
- dense data এর জন্য `hex` or `kde` better
- correlation check করতে `reg` useful

---

# 📌 Next Day Preview

## 📅 Day 18 — Regression Visualization

আগামী দিনে শিখবো:

- `sns.regplot()`
- `sns.lmplot()`
- regression line analysis
- polynomial regression
- confidence interval
- residual understanding

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- different variable pairs test করো
- hue compare করো
- jointplot vs scatterplot compare করো

---

## 🧪 Practice Ideas

- `total_bill` vs `tip` relationship analyze করো
- `size` vs `tip` correlation দেখো
- smoker vs non-smoker pattern compare করো
- `kind="kde"` and `kind="hex"` compare করো
