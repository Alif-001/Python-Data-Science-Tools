# 📅 Day 32 — EDA Visualization Project

## 🎯 Objective

- আজকে complete Exploratory Data Analysis (EDA) visualization শিখবো
- Data distribution, correlation, outlier, এবং category analysis practice করবো
- Real dataset থেকে meaningful insight বের করা শিখবো
- One dataset থেকে multiple EDA charts বানানোর workflow বুঝবো

---

## 📚 Topics Covered

- Complete exploratory data analysis
- Distribution analysis
- Correlation analysis
- Outlier analysis
- Pair relationship analysis
- Category analysis
- Insight report generation

---

## 📁 Project Structure

```bash
day-32/
│── 01_data_loading_overview.py
│── 02_distribution_analysis.py
│── 03_correlation_analysis.py
│── 04_pair_relationship_analysis.py
│── 05_outlier_detection_visual.py
│── 06_department_analysis.py
│── 07_complete_eda_dashboard.py
│── 08_insight_report_generator.py
│── eda_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `eda_data.csv`
- **Description:** Employee-style dataset used for complete EDA visualization and insight generation

### Columns:

- `age` → Person’s age
- `salary` → Salary amount
- `experience` → Years of work experience
- `score` → Performance or evaluation score
- `department` → Department/category name

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `01_data_loading_overview.py`

### 🔹 Purpose

- Dataset load করা
- Data structure বুঝা
- Basic summary analysis দেখা

### 🧾 Code

```python
df = pd.read_csv("eda_data.csv")
print(df.head())
print(df.info())
print(df.describe())
```

### 🧠 Explanation

- Line 1 → CSV file থেকে data load করছে
- Line 2 → প্রথম 5 rows দেখাচ্ছে
- Line 3 → data types, null info, memory usage দেখাচ্ছে
- Line 4 → numerical summary statistics দিচ্ছে
- Logic → dataset সম্পর্কে প্রথম overview নেওয়া হচ্ছে

---

## 📄 2. `02_distribution_analysis.py`

### 🔹 Purpose

- Salary এবং score-এর distribution বুঝা

### 🧾 Code

```python
plt.hist(df["salary"], bins=5, color="blue", edgecolor="black")
plt.hist(df["score"], bins=5, color="green", edgecolor="black")
```

### 🧠 Explanation

- Salary data কীভাবে spread হয়েছে তা দেখা হচ্ছে
- Score data-এর spread compare করা হচ্ছে
- Histogram ব্যবহার করে frequency distribution বোঝা যায়
- Logic → data normal, skewed, or clustered কিনা বোঝা

---

## 📄 3. `03_correlation_analysis.py`

### 🔹 Purpose

- Variables-এর মধ্যে relationship খুঁজে বের করা

### 🧾 Code

```python
numeric_df = df[["age", "salary", "experience", "score"]]
corr = numeric_df.corr()
plt.imshow(corr, cmap="coolwarm")
```

### 🧠 Explanation

- Numeric columns select করা হয়েছে
- Correlation matrix তৈরি করা হয়েছে
- Heatmap style plot দিয়ে relationship visualize করা হয়েছে
- Logic → কোন features একে অপরের সাথে related তা বোঝা

---

## 📄 4. `04_pair_relationship_analysis.py`

### 🔹 Purpose

- Two variables একসাথে compare করা

### 🧾 Code

```python
plt.scatter(df["experience"], df["salary"])
plt.scatter(df["age"], df["score"])
```

### 🧠 Explanation

- Experience vs Salary relationship দেখা হচ্ছে
- Age vs Score relationship compare করা হচ্ছে
- Scatter plot দিয়ে trend, clustering, correlation বোঝা যায়
- Logic → pair-wise relationship analysis করা

---

## 📄 5. `05_outlier_detection_visual.py`

### 🔹 Purpose

- Outlier visualization করা

### 🧾 Code

```python
plt.boxplot(df["salary"])
plt.boxplot(df["score"])
```

### 🧠 Explanation

- Boxplot ব্যবহার করে unusual values identify করা হয়েছে
- Salary এবং score-এর spread compare করা হয়েছে
- Outlier থাকলে তা visually detect করা যায়
- Logic → extreme value analysis করা

---

## 📄 6. `06_department_analysis.py`

### 🔹 Purpose

- Categorical data analysis করা

### 🧾 Code

```python
dept_counts = df["department"].value_counts()
plt.bar(dept_counts.index, dept_counts.values, color="orange")
```

### 🧠 Explanation

- Department অনুযায়ী count বের করা হয়েছে
- Bar chart দিয়ে category distribution দেখানো হয়েছে
- Logic → কোন department বেশি common তা বোঝা

---

## 📄 7. `07_complete_eda_dashboard.py`

### 🔹 Purpose

- Full EDA dashboard তৈরি করা

### 🧾 Code

```python
plt.hist(df["salary"], color="blue")
plt.scatter(df["experience"], df["salary"], color="green")
plt.boxplot(df["score"])
df["department"].value_counts().plot(kind="bar", color="purple")
```

### 🧠 Explanation

- এক figure-এর মধ্যে multiple EDA plots রাখা হয়েছে
- Distribution, relationship, outlier, category একসাথে দেখা যাচ্ছে
- Logic → complete overview dashboard তৈরি হয়েছে

---

## 📄 8. `08_insight_report_generator.py`

### 🔹 Purpose

- Text-based insight report তৈরি করা

### 🧾 Code

```python
print(df["salary"].mean())
print(df["salary"].max())
print(df["salary"].min())
print(df["experience"].mean())
print(df["department"].mode()[0])
print(df[["salary", "experience"]].corr())
```

### 🧠 Explanation

- Average, max, min salary বের করা হয়েছে
- Experience-এর average বের করা হয়েছে
- Most common department identify করা হয়েছে
- Salary vs experience correlation দেখা হয়েছে
- Logic → plots ছাড়াও written insight report তৈরি করা হয়েছে

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Data overview নেওয়া হয়েছে
- Distribution analysis করা হয়েছে
- Correlation analysis করা হয়েছে
- Pair relationship দেখা হয়েছে
- Outlier detect করা হয়েছে
- Categorical analysis করা হয়েছে
- Complete dashboard এবং insight report তৈরি করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Salary distribution visually understood
- Experience and salary relationship identified
- Outliers boxplot দিয়ে found করা হয়েছে
- Department frequency analysis করা হয়েছে
- Real EDA dashboard তৈরি করা সম্ভব হয়েছে

---

## 🚀 What I Learned

- EDA workflow কীভাবে কাজ করে
- Histogram, scatter, boxplot, bar chart use করা
- Correlation matrix interpret করা
- Numerical + categorical data analysis
- Plots থেকে insight generate করা

---

## 🧠 Key Concepts (Quick Revision)

- `head()` → প্রথম rows দেখায়
- `info()` → dataset structure দেখায়
- `describe()` → summary statistics দেয়
- `hist()` → distribution দেখায়
- `corr()` → correlation matrix দেয়
- `boxplot()` → outlier এবং spread দেখায়
- `value_counts()` → category count দেয়

---

## 📝 Notes

- EDA শুরু করার আগে data বুঝে নেওয়া জরুরি
- Missing values থাকলে analysis ভুল হতে পারে
- Correlation মানে causation না
- Different plot different insight দেয়

---

## 📌 Next Day Preview

- Final mastery revision
- All plot types quick review
- Plot selection strategy
- Best practices এবং common mistakes

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- automatic EDA report generator বানানো
- missing value handling add করা
- feature engineering visualization যোগ করা
- interactive dashboard তৈরি করা

### 🧪 Practice Ideas

- employee performance analysis করো
- salary vs experience report বানাও
- outlier detection challenge নাও
- department-wise comparison dashboard তৈরি করো
