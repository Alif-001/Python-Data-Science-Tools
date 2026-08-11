# 📅 Day 14 — Area & Stack Plot

## 🎯 Objective

- আজকে Area Chart এবং Stack Plot শিখবো
- Trend visualization এবং cumulative growth বুঝবো
- Multiple category data একসাথে analyze করা শিখবো
- Business-level growth visualization তৈরি করা শিখবো
- Line vs Area chart পার্থক্য বুঝবো

---

## 📚 Topics Covered

- Area chart (fill_between)
- Stack plot concept
- Cumulative visualization
- Multi-category area chart
- Trend analysis
- Business growth visualization

---

## 📁 Project Structure

```bash id="day14struct"
day-14/
│── 01_basic_area_chart.py
│── 02_stack_plot.py
│── 03_cumulative_visualization.py
│── 04_multi_category_area.py
│── 05_area_vs_line.py
│── 06_real_stack_area.py
│── company_growth_area.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** company_growth_area.csv
- **Description:** Company product-wise monthly sales data used for area and stack visualization

### Columns:

- month → Month name
- product_a → Product A sales
- product_b → Product B sales
- product_c → Product C sales

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py

### 🔹 Purpose

- Area chart এবং stack plot concept introduction

### 🧾 Code

```python id="main14"
print("Day 14 - Area & Stack Plot 📊")
```

### 🧠 Explanation

- Area chart = trend + filled region visualization
- Stack plot = multiple category contribution analysis

---

## 📄 2. analysis.py

### 🔹 Purpose

- Trend analysis helper

### 🧾 Code

```python id="analysis14"
def total_growth(*values):
    return sum(values)
```

### 🧠 Explanation

- Multiple values যোগ করে total growth বের করে
- Cumulative analysis support করে

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper functions

### 🧾 Code

```python id="utils14"
def format_month(month):
    return month.upper()
```

### 🧠 Explanation

- Month formatting clean করে
- Visualization consistency maintain করে

---

## 📄 4. 01_basic_area_chart.py

### 🔹 Purpose

- Basic area chart তৈরি করা

### 🧾 Code

```python id="area1"
plt.fill_between(x, y, color="skyblue", alpha=0.5)
plt.plot(x, y)
```

### 🧠 Explanation

- Line plot এর নিচে area fill করা হয়
- Growth trend visually highlight হয়

---

## 📄 5. 02_stack_plot.py

### 🔹 Purpose

- Multiple category stack visualization

### 🧾 Code

```python id="stack2"
plt.stackplot(x, y1, y2, y3, labels=["A", "B", "C"], alpha=0.7)
```

### 🧠 Explanation

- একাধিক data series একসাথে stack করা হয়
- Contribution comparison সহজ হয়

---

## 📄 6. 03_cumulative_visualization.py

### 🔹 Purpose

- Cumulative growth visualization

### 🧾 Code

```python id="cum3"
plt.stackplot(x, sales_online, sales_offline)
```

### 🧠 Explanation

- Online + Offline sales combined growth দেখায়
- Total performance trend বোঝা যায়

---

## 📄 7. 04_multi_category_area.py

### 🔹 Purpose

- Multiple product performance compare করা

### 🧾 Code

```python id="multi4"
plt.stackplot(months, product_a, product_b, product_c)
```

### 🧠 Explanation

- Multiple product contribution একসাথে দেখানো হয়
- Business analysis সহজ হয়

---

## 📄 8. 05_area_vs_line.py

### 🔹 Purpose

- Line plot vs Area plot comparison

### 🧾 Code

```python id="compare5"
plt.plot(x, y)
plt.fill_between(x, y)
```

### 🧠 Explanation

- Line plot শুধু trend দেখায়
- Area plot trend + volume বুঝায়

---

## 📄 9. 06_real_stack_area.py

### 🔹 Purpose

- Real company dataset visualization

### 🧾 Code

```python id="real6"
import csv

with open("company_growth_area.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product_a.append(int(row["product_a"]))
        product_b.append(int(row["product_b"]))
        product_c.append(int(row["product_c"]))

plt.stackplot(months, product_a, product_b, product_c)
```

### 🧠 Explanation

- CSV থেকে real business data load করা হয়েছে
- Product-wise growth analyze করা হয়েছে
- Stack plot দিয়ে contribution visualize করা হয়েছে

---

## ⚙️ Implementation Flow

- Area chart concept শিখা হয়েছে
- Stack plot ব্যবহার করা হয়েছে
- Cumulative visualization তৈরি করা হয়েছে
- Multi-category comparison করা হয়েছে
- Line vs area comparison করা হয়েছে
- Real dataset analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Area chart trend highlight করে
- Stack plot contribution বুঝায়
- Cumulative growth analysis সহজ হয়
- Multi-product comparison powerful
- Business performance clearly visualize হয়

---

## 🚀 What I Learned

- Area chart concept (fill_between)
- Stack plot usage
- Cumulative visualization idea
- Multi-category comparison
- Business growth analysis

---

## 🧠 Key Concepts (Quick Revision)

- `fill_between()` → area chart তৈরি করে
- `stackplot()` → multiple data stack করে
- cumulative → total growth representation
- alpha → transparency control
- trend → time-based change

---

## 📝 Notes

- Too many categories হলে stack plot confusing হতে পারে
- Area chart small dataset এ best কাজ করে
- Proper labeling খুব important
- Overlapping avoid করতে হবে

---

## 📌 Next Day Preview

- Error Bars
- Standard deviation visualization
- Confidence interval concept
- Scientific data plotting
- Uncertainty visualization

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Sales growth dashboard
- Product performance analyzer
- Revenue vs cost stack visualization
- Interactive business trend tool

### 🧪 Practice Ideas

- E-commerce sales tracking system
- Company profit breakdown chart
- Monthly subscription growth analysis
- Multi-product revenue dashboard
