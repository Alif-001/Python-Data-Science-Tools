# 📅 Day 5 — Bar Chart

## 🎯 Objective

- আজকে Bar Chart শিখবো
- Category-based data compare করা শিখবো
- Vertical, Horizontal, Grouped, Stacked bar chart বুঝবো
- Real dataset থেকে business-style visualization করা শিখবো

---

## 📚 Topics Covered

- Vertical bar chart
- Horizontal bar chart
- Grouped bar chart
- Stacked bar chart
- Color customization
- Width control
- Category visualization
- Real dataset examples

---

## 📁 Project Structure

```bash
day-5/
│── 01_basic_vertical_bar.py
│── 02_horizontal_bar.py
│── 03_bar_color_width.py
│── 04_grouped_bar_chart.py
│── 05_stacked_bar_chart.py
│── 06_category_visualization.py
│── 07_real_dataset_bar_chart.py
│── company_sales.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** company_sales.csv
- **Description:** Monthly sales data of multiple products used for comparison analysis

### Columns:

- month → Month name
- product_a → Product A sales
- product_b → Product B sales
- product_c → Product C sales

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry)

### 🔹 Purpose

- Bar chart concept বোঝা
- Category comparison idea পাওয়া

### 🧾 Code

```python id="main_bar5"
print("Bar Chart Day 5 📊")
```

### 🧠 Explanation

- Bar chart category-based comparison দেখায়
- Business analytics এ খুব important

---

## 📄 2. analysis.py

### 🔹 Purpose

- Category analysis logic বোঝানো

### 🧾 Code

```python id="analysis_bar5"
def compare_categories():
    return "Compare values across categories"
```

### 🧠 Explanation

- Different categories তুলনা করার base concept
- Decision making এ সাহায্য করে

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper functions

### 🧾 Code

```python id="utils_bar5"
def format_label(label):
    return label.upper()
```

### 🧠 Explanation

- Labels clean এবং readable করে
- Reusable utility function

---

## 📄 4. 01_basic_vertical_bar.py

### 🔹 Purpose

- Basic vertical bar chart তৈরি করা

### 🧾 Code

```python id="bar1"
import matplotlib.pyplot as plt

products = ["A", "B", "C", "D"]
sales = [20, 35, 30, 50]

plt.bar(products, sales)

plt.title("Basic Vertical Bar Chart")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()
```

### 🧠 Explanation

- `plt.bar()` → vertical bar তৈরি করে
- Category vs value comparison করা হয়

---

## 📄 5. 02_horizontal_bar.py

### 🔹 Purpose

- Horizontal bar chart তৈরি করা

### 🧾 Code

```python id="bar2"
plt.barh(products, sales)
```

### 🧠 Explanation

- `barh()` → horizontal bar তৈরি করে
- Long labels থাকলে বেশি readable

---

## 📄 6. 03_bar_color_width.py

### 🔹 Purpose

- Bar styling শেখা

### 🧾 Code

```python id="bar3"
plt.bar(
    products,
    sales,
    color="orange",
    width=0.5
)
```

### 🧠 Explanation

- `color` → bar color change করে
- `width` → bar thickness control করে

---

## 📄 7. 04_grouped_bar_chart.py

### 🔹 Purpose

- Grouped comparison chart

### 🧾 Code

```python id="bar4"
x = np.arange(len(subjects))
width = 0.35

plt.bar(x - width/2, boys, width)
plt.bar(x + width/2, girls, width)
```

### 🧠 Explanation

- Boys vs Girls side-by-side comparison
- Grouped visualization useful for analysis

---

## 📄 8. 05_stacked_bar_chart.py

### 🔹 Purpose

- Stacked bar concept শেখা

### 🧾 Code

```python id="bar5"
plt.bar(months, online_sales)
plt.bar(months, offline_sales, bottom=online_sales)
```

### 🧠 Explanation

- এক bar এর উপর আরেক bar stack হয়
- Total + breakdown analysis করা যায়

---

## 📄 9. 06_category_visualization.py

### 🔹 Purpose

- Real-life category visualization

### 🧾 Code

```python id="bar6"
plt.bar(categories, expenses, color="purple")
```

### 🧠 Explanation

- Expense breakdown দেখায়
- Business dashboard style chart

---

## 📄 10. 07_real_dataset_bar_chart.py

### 🔹 Purpose

- Real dataset analysis (multi-product sales)

### 🧾 Code

```python id="bar7"
import csv
import numpy as np

months = []
product_a = []
product_b = []
product_c = []

with open("company_sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        months.append(row["month"])
        product_a.append(int(row["product_a"]))
        product_b.append(int(row["product_b"]))
        product_c.append(int(row["product_c"]))

x = np.arange(len(months))
width = 0.25

plt.bar(x - width, product_a, width, label="Product A")
plt.bar(x, product_b, width, label="Product B")
plt.bar(x + width, product_c, width, label="Product C")

plt.xticks(x, months)
plt.legend()
plt.show()
```

### 🧠 Explanation

- Multiple product performance compare করা হয়েছে
- Grouped bar chart used for business insight
- Monthly trend analysis করা যায়

---

## ⚙️ Implementation Flow

- Bar chart concept শেখা হয়েছে
- Category comparison করা হয়েছে
- Vertical এবং horizontal chart তৈরি করা হয়েছে
- Grouped এবং stacked chart ব্যবহার করা হয়েছে
- Real dataset analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Product comparison সহজভাবে বোঝা যায়
- Grouped bar → side-by-side analysis
- Stacked bar → total + breakdown insight
- Business decision making সহজ হয়

---

## 🚀 What I Learned

- Bar chart types
- Category-based comparison
- Grouped vs stacked difference
- Real dataset visualization
- Business analytics basics

---

## 🧠 Key Concepts (Quick Revision)

- `plt.bar()` → vertical bar
- `plt.barh()` → horizontal bar
- grouped bar → comparison
- stacked bar → cumulative view
- category visualization → business data

---

## 📝 Notes

- Too many categories হলে graph clutter হয়
- Grouped bar spacing ঠিক রাখা দরকার
- CSV data type conversion important
- Label missing থাকলে confusion হয়

---

## 📌 Next Day Preview

- Pie chart basics
- Percentage visualization
- Donut chart concept
- Category proportion analysis
- Real dataset pie visualization

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Interactive dashboard বানানো
- More product categories add করা
- Revenue vs profit comparison করা
- Styled business report chart তৈরি করা

### 🧪 Practice Ideas

- Student marks category bar chart বানাও
- Monthly expense comparison করো
- 4 products vs 12 months analysis করো
- Sales growth bar chart তৈরি করো
