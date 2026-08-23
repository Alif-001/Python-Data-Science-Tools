# 📅 Day 18 — Regression Visualization

---

# 🎯 Objective

- Data relationship এর সাথে regression thinking শেখা
- `sns.regplot()` এবং `sns.lmplot()` ব্যবহার করা
- Regression line দিয়ে trend বুঝা
- Confidence interval interpret করা
- Polynomial regression concept শেখা
- Residual plot দিয়ে error intuition তৈরি করা

---

# 📚 Topics Covered

- `sns.regplot()`
- `sns.lmplot()`
- Regression line
- Polynomial regression
- Confidence interval
- Residual understanding
- Group-wise regression
- ML-style visualization insight

---

# 📁 Project Structure

```bash
day-18/
│── 01_basic_regplot.py
│── 02_confidence_interval.py
│── 03_no_ci.py
│── 04_polynomial_regression.py
│── 05_lmplot_basic.py
│── 06_lmplot_hue.py
│── 07_residual_understanding.py
│── 08_real_world_ml_intuition.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (`tips`)
- **Description:** Restaurant tipping dataset যেখানে `total_bill`, `tip`, `sex`, `smoker`, `day`, `time`, `size` ইত্যাদি আছে
- **Columns:**
  - `total_bill` → মোট বিল
  - `tip` → টিপ amount
  - `sex` → gender
  - `smoker` → smoker status
  - `day` → সপ্তাহের দিন
  - `time` → lunch/dinner
  - `size` → group size

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_regplot.py

## 🔹 Purpose

- Basic regression line visualization করা
- data points এবং best fit line একসাথে দেখা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.regplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title("Regression: Bill vs Tip")
plt.show()
```

## 🧠 Explanation

- `sns.regplot()`
  - scatter points এর উপর regression line আঁকে

- `x="total_bill"`
  - total bill independent variable

- `y="tip"`
  - tip dependent variable

- line থেকে trend বোঝা যায়

---

# 📄 2. 02_confidence_interval.py

## 🔹 Purpose

- Confidence interval concept বোঝা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.regplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title("Regression with Confidence Interval")
plt.show()
```

## 🧠 Explanation

- regression line এর চারপাশে shaded region থাকে
- shaded region uncertainty বোঝায়
- wide region মানে বেশি uncertainty
- narrow region মানে trend বেশি reliable

---

# 📄 3. 03_no_ci.py

## 🔹 Purpose

- Confidence interval ছাড়া clean regression line দেখা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.regplot(
    data=tips,
    x="total_bill",
    y="tip",
    ci=None
)

plt.title("Regression Line Only (No CI)")
plt.show()
```

## 🧠 Explanation

- `ci=None`
  - confidence interval বন্ধ করে

- only line focus করা যায়
- cleaner visualization পাওয়া যায়

---

# 📄 4. 04_polynomial_regression.py

## 🔹 Purpose

- Non-linear relationship fitting শেখা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.regplot(
    data=tips,
    x="total_bill",
    y="tip",
    order=2
)

plt.title("Polynomial Regression (Order 2)")
plt.show()
```

## 🧠 Explanation

- `order=2`
  - quadratic curve fit করে

- relationship যদি straight line না হয়, তখন useful
- higher order দিয়ে curve capture করা যায়

---

# 📄 5. 05_lmplot_basic.py

## 🔹 Purpose

- figure-level regression plot শেখা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.lmplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title("LM Plot Regression")
plt.show()
```

## 🧠 Explanation

- `sns.lmplot()`
  - figure-level regression plot

- `regplot()` থেকে বেশি flexible
- full figure control পায়

---

# 📄 6. 06_lmplot_hue.py

## 🔹 Purpose

- Group-wise regression comparison করা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.lmplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex"
)

plt.title("Regression by Gender")
plt.show()
```

## 🧠 Explanation

- `hue="sex"`
  - male এবং female এর জন্য আলাদা trend line

- group-wise behavior compare করা যায়
- subgroup pattern বোঝা সহজ হয়

---

# 📄 7. 07_residual_understanding.py

## 🔹 Purpose

- Residual / error intuition তৈরি করা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.residplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title("Residual Plot (Error Visualization)")
plt.show()
```

## 🧠 Explanation

- `sns.residplot()`
  - actual value আর predicted value এর difference দেখায়

- residual = actual - predicted
- zero line এর উপরে/নিচে থাকা points error বোঝায়

---

# 📄 8. 08_real_world_ml_intuition.py

## 🔹 Purpose

- ML-style prediction insight দেখা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.lmplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="smoker"
)

plt.title("ML Style Regression Insight")
plt.show()
```

## 🧠 Explanation

- smoker vs non-smoker এর trend compare করা হয়
- relationship strength দেখা যায়
- prediction thinking develop হয়

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Numerical columns select করা হয়েছে
- Regression plot তৈরি করা হয়েছে
- Confidence interval দেখা হয়েছে
- Polynomial regression test করা হয়েছে
- Group-wise regression করা হয়েছে
- Residual analysis করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- `total_bill` এবং `tip` এর মধ্যে positive trend দেখা যায়
- confidence interval uncertainty বোঝায়
- residual plot model error intuition দেয়
- group-wise regression different behavior দেখায়

---

# 🚀 What I Learned

- Regression visualization
- Trend line interpretation
- Confidence interval concept
- Polynomial relationship fitting
- Residual analysis
- ML-style exploratory thinking

---

# 🧠 Key Concepts (Quick Revision)

- `regplot()` → axes-level regression plot
- `lmplot()` → figure-level regression plot
- `ci` → confidence interval
- `order` → polynomial curve degree
- `residplot()` → error visualization
- `hue` → group-based regression

---

# 📝 Notes

## 📌 Common Mistakes

- `regplot()` and `lmplot()` confuse করা
- residual কে trend line ভাবা
- `order` বেশি দিয়ে overfitting-like curve বানানো

## 📌 Optimization Tips

- simple trend এর জন্য `regplot()` use করো
- grouped regression এর জন্য `lmplot()` better
- error analysis করতে residual plot helpful

---

# 📌 Next Day Preview

## 📅 Day 19 — Residual Plot

আগামী দিনে শিখবো:

- `sns.residplot()`
- error analysis
- model fitness visualization
- residual interpretation
- prediction quality understanding

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- real CSV dataset এ regression try করো
- `hue` দিয়ে more group analysis করো
- linear vs polynomial regression compare করো

---

## 🧪 Practice Ideas

- `total_bill` vs `tip` regression analyze করো
- `size` vs `tip` relationship দেখো
- `smoker` based regression compare করো
- `ci=None` and default plot compare করো
