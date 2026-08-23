# 📅 Day 16 — Pair Plot

---

# 🎯 Objective

- Seaborn-এর সবচেয়ে powerful EDA tool শেখা
- `sns.pairplot()` ব্যবহার করে full dataset relationship analysis করা
- variable-to-variable relationship visualize করা
- class-based separation (hue) বোঝা
- correlation pattern detect করা

---

# 📚 Topics Covered

- `sns.pairplot()`
- Pairwise relationships
- Multivariable analysis
- `hue` based class separation
- `diag_kind` (hist / kde)
- Feature selection (`vars`)
- `corner=True` cleaner layout
- Correlation discovery

---

# 📁 Project Structure

```bash id="day16"
day-16/
│── 01_basic_pairplot.py
│── 02_hue_pairplot.py
│── 03_diag_kind_hist.py
│── 04_diag_kind_kde.py
│── 05_vars_subset_pairplot.py
│── 06_corner_pairplot.py
│── 07_real_world_insight_pairplot.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (`iris`)
- **Source:** Seaborn built-in dataset
- **Loaded Using:** `sns.load_dataset("iris")`

---

## 📌 Description

Iris dataset যেখানে different flower species-এর sepal এবং petal measurements থাকে।
এটি classification + pattern analysis এর জন্য খুব famous dataset।

---

## 📌 Columns

- `sepal_length` → sepal length measurement
- `sepal_width` → sepal width measurement
- `petal_length` → petal length measurement
- `petal_width` → petal width measurement
- `species` → flower class (setosa, versicolor, virginica)

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_pairplot.py

## 🔹 Purpose

- basic pairplot ব্যবহার করা
- full variable relationship দেখা

---

## 🧾 Code

```python id="pp1"
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.pairplot(iris)

plt.show()
```

---

## 🧠 Explanation

- `pairplot()`
  - সব numeric column একে অপরের সাথে compare করে

- diagonal এ distribution show করে
- off-diagonal এ scatter relationship দেখায়

---

# 📄 2. 02_hue_pairplot.py

## 🔹 Purpose

- class-based visualization

---

## 🧾 Code

```python id="pp2"
sns.pairplot(
    iris,
    hue="species"
)
```

---

## 🧠 Explanation

- `hue="species"`
  - প্রতিটি class আলাদা color পায়

- class separation easily দেখা যায়

---

# 📄 3. 03_diag_kind_hist.py

## 🔹 Purpose

- diagonal distribution as histogram

---

## 🧾 Code

```python id="pp3"
sns.pairplot(
    iris,
    hue="species",
    diag_kind="hist"
)
```

---

## 🧠 Explanation

- diagonal plots → histogram
- feature-wise frequency distribution দেখা যায়

---

# 📄 4. 04_diag_kind_kde.py

## 🔹 Purpose

- smooth distribution visualization

---

## 🧾 Code

```python id="pp4"
sns.pairplot(
    iris,
    hue="species",
    diag_kind="kde"
)
```

---

## 🧠 Explanation

- KDE = smooth density curve
- distribution shape clearer হয়

---

# 📄 5. 05_vars_subset_pairplot.py

## 🔹 Purpose

- selected features analysis

---

## 🧾 Code

```python id="pp5"
sns.pairplot(
    iris,
    vars=["sepal_length", "sepal_width", "petal_length"],
    hue="species"
)
```

---

## 🧠 Explanation

- only selected columns analyze করা
- noise কমে insight clearer হয়

---

# 📄 6. 06_corner_pairplot.py

## 🔹 Purpose

- clean visualization layout

---

## 🧾 Code

```python id="pp6"
sns.pairplot(
    iris,
    hue="species",
    corner=True
)
```

---

## 🧠 Explanation

- upper triangle hide করা হয়
- cleaner EDA view পাওয়া যায়

---

# 📄 7. 07_real_world_insight_pairplot.py

## 🔹 Purpose

- real-world correlation analysis

---

## 🧾 Code

```python id="pp7"
sns.pairplot(
    iris,
    hue="species",
    diag_kind="kde",
    corner=True
)
```

---

## 🧠 Explanation

- class separation + correlation analysis
- best EDA visualization for ML preprocessing

---

# ⚙️ Implementation Flow

- dataset load করা হয়েছে
- numerical features select করা হয়েছে
- `pairplot()` দিয়ে relationship matrix তৈরি করা হয়েছে
- `hue` দিয়ে class separation করা হয়েছে
- `diag_kind` দিয়ে distribution shape দেখা হয়েছে
- `corner=True` দিয়ে layout clean করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- সব feature একসাথে compare করা যায়
- class separation visually clear হয়
- correlation pattern easily detect করা যায়
- distribution + relationship একসাথে দেখা যায়
- EDA fast এবং powerful হয়

---

# 🚀 What I Learned

- multivariable relationship analysis
- correlation visualization
- classification insight detection
- EDA automation using pairplot
- feature interaction understanding

---

# 🧠 Key Concepts (Quick Revision)

- `pairplot()` → full dataset relationship matrix
- `hue` → class separation
- `diag_kind` → histogram/KDE distribution
- `vars` → feature selection
- `corner` → clean layout

---

# 📝 Notes

## 📌 Common Mistakes

- large dataset এ slow performance
- irrelevant columns include করা
- hue ভুল column ব্যবহার করা

## 📌 Optimization Tips

- only numeric columns use করা
- `vars` দিয়ে feature reduce করা
- corner mode use করলে readability বাড়ে

---

# 📌 Next Day Preview

## 📅 Day 17 — Joint Plot

আগামী দিনে শিখবো:

- `sns.jointplot()`
- scatter + distribution combine analysis
- correlation strength visualization
- KDE, hex, regression joint plots
- deep relationship analysis

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- iris dataset এ feature engineering try করো
- different hue compare করো
- pairplot vs catplot comparison করো

---

## 🧪 Practice Ideas

- sepal vs petal relationship analyze করো
- species separation check করো
- strongest correlated feature identify করো
