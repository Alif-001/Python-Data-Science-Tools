# � Day 31 — Exploratory Data Analysis (EDA)

---

# 🎯 Objective

- একটি real-world dataset দিয়ে full EDA workflow শেখা
- Data বুঝে নেওয়া (structure + summary)
- Distribution analysis করা
- Correlation relationships খুঁজে বের করা
- Outlier detection করা
- Multi-variable insights তৈরি করা
- Business-style data storytelling শেখা

---

# 📚 Topics Covered

- Data loading & overview (`pandas`)
- Summary statistics (`describe`, `info`)
- Distribution analysis (`histplot`)
- Correlation analysis (`heatmap`)
- Outlier detection (`boxplot`)
- Relationship analysis (`scatterplot`)
- Multivariate analysis (`pairplot`)
- Full EDA pipeline
- Insight storytelling

---

# 📁 Dataset

## 📌 File Name: `company_data.csv`

## 📌 Description

একটি simulated company dataset যেখানে employee performance, salary, experience এবং productivity সম্পর্কিত তথ্য রয়েছে।

## 📌 Columns

- `employee` → employee ID
- `experience` → কাজের অভিজ্ঞতা (years)
- `salary` → monthly salary
- `performance` → performance score
- `projects` → completed projects
- `absent_days` → absence count

---

# 📁 Project Structure

```bash
day-31/
│── company_data.csv
│── 01_basic_eda_overview.py
│── 02_distribution_analysis.py
│── 03_correlation_analysis.py
│── 04_outlier_detection_boxplot.py
│── 05_relationship_analysis.py
│── 06_multivariate_eda.py
│── 07_real_world_eda_report.py
│── 08_final_insight_story.py
│── README.md
```

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_eda_overview.py

## 🔹 Purpose

- Dataset প্রথমে বুঝে নেওয়া
- Structure + statistics check করা

## 🧾 Code

```python
import pandas as pd

df = pd.read_csv("company_data.csv")

print(df.head())
print(df.info())
print(df.describe())
```

## 🧠 Explanation

- `read_csv()` → dataset load করে
- `head()` → প্রথম 5 rows দেখায়
- `info()` → columns + data types দেখায়
- `describe()` → statistical summary দেয়

---

# 📄 2. 02_distribution_analysis.py

## 🔹 Purpose

- Salary distribution বোঝা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("company_data.csv")

sns.histplot(data=df, x="salary", kde=True)

plt.title("Salary Distribution")
plt.show()
```

## 🧠 Explanation

- `histplot()` → distribution দেখায়
- `kde=True` → smooth curve যোগ করে
- Salary spread বোঝা যায়

---

# 📄 3. 03_correlation_analysis.py

## 🔹 Purpose

- Features এর মধ্যে relationship বোঝা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("company_data.csv")

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)

plt.title("Feature Correlation Heatmap")
plt.show()
```

## 🧠 Explanation

- `corr()` → correlation matrix তৈরি করে
- `heatmap()` → relationship visualize করে
- Strong + / - relationship বোঝা যায়

---

# 📄 4. 04_outlier_detection_boxplot.py

## 🔹 Purpose

- Outliers detect করা

## 🧾 Code

```python
sns.boxplot(data=df, y="salary")
```

## 🧠 Explanation

- Boxplot median + spread দেখায়
- Whisker এর বাইরে → outlier

---

# 📄 5. 05_relationship_analysis.py

## 🔹 Purpose

- Salary vs Experience relationship বোঝা

## 🧾 Code

```python
sns.scatterplot(
    data=df,
    x="experience",
    y="salary",
    hue="performance",
    size="projects"
)
```

## 🧠 Explanation

- Experience increase → salary pattern
- `hue` → performance effect দেখায়
- `size` → projects impact দেখায়

---

# 📄 6. 06_multivariate_eda.py

## 🔹 Purpose

- সব relationships একসাথে দেখা

## 🧾 Code

```python
sns.pairplot(df)
plt.show()
```

## 🧠 Explanation

- Pairwise relationship plot করে
- All variables correlation explore করা যায়

---

# 📄 7. 07_real_world_eda_report.py

## 🔹 Purpose

- Full EDA pipeline একসাথে করা

## 🧾 Code Flow

- overview → describe
- correlation → heatmap
- distribution → histogram
- outlier → boxplot

## 🧠 Explanation

- Complete analysis workflow
- Beginner → Data Scientist style report

---

# 📄 8. 08_final_insight_story.py

## 🔹 Purpose

- Business insight storytelling

## 🧾 Code

```python
sns.scatterplot(
    data=df,
    x="experience",
    y="salary",
    hue="performance",
    size="projects"
)

plt.title("Final EDA Insight: Salary Growth Pattern")
plt.grid(True)
plt.show()
```

## 🧠 Explanation

- Experience → salary growth pattern
- Performance adds extra impact
- Projects influence salary scaling

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Basic structure check করা হয়েছে
- Distribution analysis করা হয়েছে
- Correlation matrix তৈরি করা হয়েছে
- Outliers detect করা হয়েছে
- Multi-variable relationships explore করা হয়েছে
- Final insight visualization তৈরি করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Experience strongly affects salary
- Performance also influences salary growth
- Projects increase earning potential
- No extreme anomalies in dataset (low outliers)
- Strong positive correlation between experience & salary

---

# 🚀 What I Learned

- Real-world EDA workflow
- Data understanding before modeling
- Pattern recognition in data
- Correlation interpretation
- Outlier detection techniques
- Business insight extraction

---

# 🧠 Key Concepts (Quick Revision)

- EDA = Explore + Understand + Visualize
- `describe()` → statistics summary
- `heatmap()` → correlation view
- `boxplot()` → outlier detection
- `pairplot()` → multivariate relationships
- Seaborn = fast EDA tool

---

# 📝 Notes

## 📌 Common Mistakes

- correlation না বুঝে feature remove করা
- outliers blindly delete করা
- visualization ছাড়া decision নেওয়া

## 📌 Optimization Tips

- EDA always before ML
- Always combine stats + plots
- Business perspective always keep in mind

---

# 📌 Next Day Preview

## 📅 Day 32 — Business Analytics Visualization

আগামী দিনে শিখবে:

- Sales analysis
- Customer segmentation
- Revenue trends
- KPI dashboards
- Business storytelling with Seaborn

---

# ⭐ Bonus

## 🔥 Improvement Ideas

- Real Kaggle dataset try করা
- Industry-level EDA report তৈরি করা
- Dashboard-style visualization বানানো

---

## 🧪 Practice Ideas

- salary vs absent_days relation plot করো
- performance vs projects analyze করো
- correlation থেকে top 3 features বের করো
