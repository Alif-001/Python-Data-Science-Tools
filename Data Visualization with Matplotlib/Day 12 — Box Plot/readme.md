# 📅 Day 12 — Box Plot

## 🎯 Objective

- আজকে Box Plot এর core concept শিখবো
- Data distribution বুঝতে শিখবো
- Quartile system (Q1, Q2, Q3) analyze করা শিখবো
- Outlier detect করা শিখবো
- Multiple group comparison শিখবো
- Real dataset দিয়ে salary analysis করা শিখবো

---

## 📚 Topics Covered

- Box plot basics
- Quartiles (Q1, Median, Q3)
- Outlier detection
- Multiple box plots
- Styling box plots
- Distribution comparison
- Real dataset analysis

---

## 📁 Project Structure

```bash
day-12/
│── 01_basic_boxplot.py
│── 02_boxplot_quartiles.py
│── 03_outlier_detection.py
│── 04_multiple_boxplots.py
│── 05_boxplot_styling.py
│── 06_distribution_comparison.py
│── 07_real_dataset_boxplot.py
│── employee_salary.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** employee_salary.csv
- **Description:** Employee salary data used for department-wise distribution analysis

### Columns:

- name → Employee name
- department → Department name (IT / HR / Sales)
- salary → Employee salary

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py

### 🔹 Purpose

- Box plot concept introduction
- Distribution visualization idea বোঝা

### 🧾 Code

```python
print("Day 12 - Box Plot 📦")
```

### 🧠 Explanation

- Box plot = statistical distribution visualization
- Data spread বুঝতে সাহায্য করে

---

## 📄 2. analysis.py

### 🔹 Purpose

- Data spread analysis helper

### 🧾 Code

```python
def get_range(data):
    return min(data), max(data)
```

### 🧠 Explanation

- Minimum এবং maximum value বের করে
- Spread analysis support করে

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper functions

### 🧾 Code

```python
def clean_data(value):
    return int(value)
```

### 🧠 Explanation

- Raw data clean করে integer বানায়
- CSV processing-এ useful

---

## 📄 4. 01_basic_boxplot.py

### 🔹 Purpose

- Simple box plot তৈরি করা

### 🧾 Code

```python
plt.boxplot(marks)
```

### 🧠 Explanation

- Median, quartiles, spread automatically দেখায়
- Student marks distribution বুঝতে সাহায্য করে

---

## 📄 5. 02_boxplot_quartiles.py

### 🔹 Purpose

- Quartile system visualize করা

### 🧾 Code

```python
plt.boxplot(data)
```

### 🧠 Explanation

- Q1 → 25% data point
- Q2 → Median
- Q3 → 75% data point
- Data distribution বুঝতে core concept

---

## 📄 6. 03_outlier_detection.py

### 🔹 Purpose

- Outlier detect করা

### 🧾 Code

```python
plt.boxplot(data)
```

### 🧠 Explanation

- Normal range থেকে দূরের value outlier
- 100 value আলাদা করে দেখানো হয়েছে

---

## 📄 7. 04_multiple_boxplots.py

### 🔹 Purpose

- Multiple group comparison

### 🧾 Code

```python
plt.boxplot(data)
plt.xticks([1, 2, 3], ["Class A", "Class B", "Class C"])
```

### 🧠 Explanation

- একাধিক group compare করা যায়
- Performance analysis সহজ হয়

---

## 📄 8. 05_boxplot_styling.py

### 🔹 Purpose

- Box plot styling করা

### 🧾 Code

```python
plt.boxplot(
    data,
    patch_artist=True,
    boxprops=dict(facecolor="lightblue"),
    medianprops=dict(color="red")
)
```

### 🧠 Explanation

- Color fill করা হয়েছে
- Median highlight করা হয়েছে
- Chart visually better হয়েছে

---

## 📄 9. 06_distribution_comparison.py

### 🔹 Purpose

- Different group distribution compare করা

### 🧾 Code

```python
plt.boxplot(data)
```

### 🧠 Explanation

- Group-wise spread compare করা হয়
- Business comparison analysis সহজ হয়

---

## 📄 10. 07_real_dataset_boxplot.py

### 🔹 Purpose

- Real employee salary analysis

### 🧾 Code

```python
import csv

it = []
hr = []
sales = []

with open("employee_salary.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        salary = int(row["salary"])

        if row["department"] == "IT":
            it.append(salary)
        elif row["department"] == "HR":
            hr.append(salary)
        elif row["department"] == "Sales":
            sales.append(salary)

plt.boxplot([it, hr, sales])
```

### 🧠 Explanation

- Department-wise salary split করা হয়েছে
- IT, HR, Sales compare করা হয়েছে
- Salary distribution analysis করা হয়েছে

---

## ⚙️ Implementation Flow

- Box plot concept শিখা হয়েছে
- Quartile system visualize করা হয়েছে
- Outlier detect করা হয়েছে
- Multiple groups compare করা হয়েছে
- Styling apply করা হয়েছে
- Real dataset analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Box plot data distribution clearly দেখায়
- Outliers easily detect করা যায়
- Group comparison খুব powerful
- Salary distribution analysis সহজ হয়
- Business insight extract করা যায়

---

## 🚀 What I Learned

- Box plot structure (min, Q1, median, Q3, max)
- Outlier detection concept
- Multiple dataset comparison
- Styling box plots
- Real-world salary analysis

---

## 🧠 Key Concepts (Quick Revision)

- Box plot → distribution visualization
- Median → middle value
- Quartiles → Q1, Q2, Q3
- Outlier → unusual value
- `plt.boxplot()` → main function
- `patch_artist` → color fill

---

## 📝 Notes

- Small dataset হলে box plot misleading হতে পারে
- Outlier analysis খুব important
- Business decision-এর জন্য distribution বুঝা জরুরি
- Clean data না হলে result wrong হতে পারে

---

## 📌 Next Day Preview

- Violin Plot
- Distribution shape analysis
- Box plot vs violin plot comparison
- Advanced statistical visualization

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Auto outlier detector system
- Salary analytics dashboard
- Department performance analyzer
- Interactive distribution tool

### 🧪 Practice Ideas

- Student marks comparison system
- Company salary analysis dashboard
- Product price distribution study
- Exam result analysis tool
