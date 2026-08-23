# 📅 Day 9 — Count Plot

---

# 🎯 Objective

- Categorical data কিভাবে count করা হয় তা শেখা
- `sns.countplot()` ব্যবহার করে frequency visualization বোঝা
- Different categories compare করা শিখা
- `hue` ব্যবহার করে subgroup analysis করা
- Category ordering control করা
- Real-world categorical insight বের করা

---

# 📚 Topics Covered

- `sns.countplot()`
- Categorical frequency visualization
- `hue` comparison
- `order` (category sorting)
- `hue_order`
- Horizontal count plot
- Multi-variable category analysis
- Business-style categorical insights

---

# 📁 Project Structure

```bash
day-9/
│── 01_basic_countplot.py
│── 02_countplot_hue.py
│── 03_ordering_categories.py
│── 04_hue_order.py
│── 05_horizontal_countplot.py
│── 06_multi_variable_count.py
│── 07_real_world_count_analysis.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (tips)
- **Source:** Seaborn built-in dataset
- **Loaded Using:** `sns.load_dataset("tips")`

---

## 📌 Description

Restaurant tipping dataset যেখানে customer behavior, bill, tip, day, gender, smoker status ইত্যাদি তথ্য থাকে।

---

## 📌 Columns

- `total_bill` → মোট বিল
- `tip` → টিপের amount
- `sex` → gender
- `smoker` → smoker কিনা
- `day` → day of week
- `time` → lunch/dinner
- `size` → group size

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_countplot.py

## 🔹 Purpose

- Basic categorical count visualization
- প্রতিটি category কতবার আছে তা দেখা

---

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.countplot(
    data=tips,
    x="day"
)

plt.title("Count of Customers per Day")
plt.show()
```

---

## 🧠 Explanation

- `sns.countplot()`
  - প্রতিটি category automatically count করে bar chart বানায়

- `x="day"`
  - day অনুযায়ী count দেখায়

- `plt.show()`
  - plot display করে

---

# 📄 2. 02_countplot_hue.py

## 🔹 Purpose

- Category ভেতরে subgroup comparison করা

---

## 🧾 Code

```python
sns.countplot(
    data=tips,
    x="day",
    hue="smoker"
)
```

---

## 🧠 Explanation

- `hue="smoker"`
  - smoker vs non-smoker আলাদা করে দেখায়

- একই day এর মধ্যে comparison করা যায়

---

# 📄 3. 03_ordering_categories.py

## 🔹 Purpose

- Category order control করা

---

## 🧾 Code

```python
sns.countplot(
    data=tips,
    x="day",
    order=["Thur", "Fri", "Sat", "Sun"]
)
```

---

## 🧠 Explanation

- `order`
  - manual category sorting

- default alphabetical order replace করা হয়

---

# 📄 4. 04_hue_order.py

## 🔹 Purpose

- hue categories এর order control করা

---

## 🧾 Code

```python
sns.countplot(
    data=tips,
    x="day",
    hue="smoker",
    hue_order=["Yes", "No"]
)
```

---

## 🧠 Explanation

- `hue_order`
  - subgroup order fix করে

- consistent visualization তৈরি হয়

---

# 📄 5. 05_horizontal_countplot.py

## 🔹 Purpose

- Horizontal bar chart তৈরি করা

---

## 🧾 Code

```python
sns.countplot(
    data=tips,
    y="day"
)
```

---

## 🧠 Explanation

- `y="day"`
  - horizontal count plot তৈরি হয়

- long labels সহজে পড়া যায়

---

# 📄 6. 06_multi_variable_count.py

## 🔹 Purpose

- Multiple category comparison

---

## 🧾 Code

```python
sns.countplot(
    data=tips,
    x="day",
    hue="sex"
)
```

---

## 🧠 Explanation

- `hue="sex"`
  - male vs female comparison

- multi-variable insight পাওয়া যায়

---

# 📄 7. 07_real_world_count_analysis.py

## 🔹 Purpose

- Real-world style categorical analysis

---

## 🧾 Code

```python
sns.countplot(
    data=tips,
    x="time",
    hue="smoker"
)
```

---

## 🧠 Explanation

- lunch vs dinner comparison
- smoker behavior analysis
- business insight style visualization

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Categorical variables select করা হয়েছে
- `countplot()` দিয়ে frequency analysis করা হয়েছে
- `hue` দিয়ে subgroup comparison করা হয়েছে
- Ordering customize করা হয়েছে
- Real-world insights বের করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- প্রতিটি category কতটা frequent তা সহজে দেখা যায়
- Subgroup comparison (smoker/gender) clear হয়
- Ordered visualization storytelling improve করে
- Business analysis style insight পাওয়া যায়

---

# 🚀 What I Learned

- Categorical frequency analysis
- `sns.countplot()` usage
- `hue` based comparison
- Category ordering control
- Real-world dataset interpretation

---

# 🧠 Key Concepts (Quick Revision)

- `countplot()` → category count visualization
- `hue` → subgroup comparison
- `order` → category sorting
- `hue_order` → subgroup ordering
- Categorical analysis = business insights tool

---

# 📝 Notes

## 📌 Common Mistakes

- Column name ভুল লেখা
- `hue` ভুল category দেয়া
- order mismatch করা

## 📌 Optimization Tips

- Always meaningful order set করো
- hue ব্যবহার করলে insight বেশি পাওয়া যায়
- horizontal plot readability improve করে

---

# 📌 Next Day Preview

## 📅 Day 10 — Bar Plot

আগামী দিনে শিখবো:

- `sns.barplot()`
- Mean/median visualization
- Statistical aggregation
- Error bars
- Group comparison

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- Different datasets এ countplot try করো
- Multiple hue variables experiment করো
- Business-style analysis practice করো

---

## 🧪 Practice Ideas

- `sex` vs `day` countplot বানাও
- `time` vs `size` analysis করো
- `smoker` distribution compare করো
- Real-life survey dataset try করো
