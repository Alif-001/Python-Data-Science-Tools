# 📅 Day 19 — Residual Plot

---

# 🎯 Objective

- Regression model এর error বুঝা (residual analysis)
- `sns.residplot()` ব্যবহার করে prediction error visualize করা
- Model ভালো নাকি খারাপ তা identify করা
- Bias / pattern detection শেখা
- ML model validation intuition তৈরি করা

---

# 📚 Topics Covered

- `sns.residplot()`
- Residual (Error) concept
- Model fitness visualization
- Bias detection
- LOWESS smoothing
- Good vs bad model behavior
- Regression + error analysis

---

# 📁 Project Structure

```bash id="proj19"
day-19/
│── 01_basic_residplot.py
│── 02_understanding_residuals.py
│── 03_model_fitness_check.py
│── 04_good_vs_bad_model.py
│── 05_residual_with_regression.py
│── 06_group_residual_analysis.py
│── 07_real_world_model_check.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (`tips`)
- **Description:** Restaurant bill এবং tip সম্পর্কিত dataset
- **Columns:**
  - `total_bill` → মোট বিল
  - `tip` → টিপ amount
  - `sex` → gender
  - `smoker` → smoker status
  - `day` → day of week
  - `time` → lunch/dinner
  - `size` → group size

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_residplot.py

## 🔹 Purpose

- Basic residual plot তৈরি করা
- prediction error visualize করা

## 🧾 Code

```python id="r1"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.residplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title("Residual Plot: Bill vs Tip")
plt.show()
```

## 🧠 Explanation

- `sns.residplot()`
  - actual vs predicted error দেখায়

- residual = actual - predicted
- pattern থাকলে model weak

---

# 📄 2. 02_understanding_residuals.py

## 🔹 Purpose

- residual value interpret করা

## 🧾 Code

```python id="r2"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.residplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.axhline(0, color="red")

plt.title("Residual Meaning Visualization")
plt.show()
```

## 🧠 Explanation

- red line = perfect prediction (0 error)
- উপরের points = under-predicted
- নিচের points = over-predicted

---

# 📄 3. 03_model_fitness_check.py

## 🔹 Purpose

- model fit quality check করা

## 🧾 Code

```python id="r3"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.residplot(
    data=tips,
    x="total_bill",
    y="tip",
    lowess=True
)

plt.title("Model Fitness Check (LOWESS)")
plt.show()
```

## 🧠 Explanation

- `lowess=True`
  - smooth curve বানায়

- pattern থাকলে model biased
- randomness = good model

---

# 📄 4. 04_good_vs_bad_model.py

## 🔹 Purpose

- good vs bad model intuition

## 🧾 Code

```python id="r4"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.residplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title("Residuals (Check Randomness)")
plt.show()
```

## 🧠 Explanation

- good model → random scatter
- bad model → clear pattern
- pattern = missing relationship

---

# 📄 5. 05_residual_with_regression.py

## 🔹 Purpose

- regression + error comparison বোঝা

## 🧾 Code

```python id="r5"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.regplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title("Regression Line")
plt.show()

sns.residplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title("Residual Analysis")
plt.show()
```

## 🧠 Explanation

- regression = prediction line
- residual = prediction error
- দুইটা একসাথে model understanding দেয়

---

# 📄 6. 06_group_residual_analysis.py

## 🔹 Purpose

- error spread analyze করা

## 🧾 Code

```python id="r6"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.residplot(
    data=tips,
    x="total_bill",
    y="tip",
    scatter_kws={"alpha": 0.5}
)

plt.title("Residual Spread Analysis")
plt.show()
```

## 🧠 Explanation

- alpha reduce করলে overlap কমে
- error distribution clearly দেখা যায়

---

# 📄 7. 07_real_world_model_check.py

## 🔹 Purpose

- real ML model validation intuition

## 🧾 Code

```python id="r7"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.residplot(
    data=tips,
    x="total_bill",
    y="tip",
    lowess=True
)

plt.axhline(0, color="black")

plt.title("Model Error Pattern Check")
plt.show()
```

## 🧠 Explanation

- black line = zero error baseline
- pattern detect করলে model improve করতে হয়

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- regression assumption check করা হয়েছে
- residual plot তৈরি করা হয়েছে
- error pattern analyze করা হয়েছে
- model bias check করা হয়েছে
- LOWESS smoothing applied করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- residual random হলে model good
- pattern থাকলে model biased
- high bill → higher error variation possible
- LOWESS curve model weakness detect করে

---

# 🚀 What I Learned

- Residual concept (error = actual - predicted)
- Model evaluation basics
- Bias detection
- Regression limitation understanding
- ML validation intuition

---

# 🧠 Key Concepts (Quick Revision)

- `residplot()` → error visualization
- residual → actual - predicted
- randomness → good model
- pattern → bad model
- `lowess=True` → smooth trend check
- `axhline(0)` → perfect prediction line

---

# 📝 Notes

## 📌 Common Mistakes

- residual plot কে regression line ভাবা
- pattern ignore করা
- zero line meaning না বোঝা

## 📌 Optimization Tips

- always regression + residual together use করো
- large dataset এ alpha use করো
- LOWESS use করে bias check করো

---

# 📌 Next Day Preview

## 📅 Day 20 — Heatmap & Correlation

আগামী দিনে শিখবো:

- `sns.heatmap()`
- correlation matrix
- feature relationship analysis
- data insight extraction
- ML feature selection intuition

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- different datasets এ residual check করো
- categorical vs numerical error compare করো
- regression model improve করার চেষ্টা করো

---

## 🧪 Practice Ideas

- `total_bill → tip` residual analyze করো
- smoker group-wise error check করো
- time (lunch/dinner) based residual compare করো
- LOWESS vs normal residual compare করো
