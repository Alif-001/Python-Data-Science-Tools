# 📅 Day 10 — Text & Annotation

## 🎯 Objective

- আজকে graph-এর মধ্যে text add করা শিখবো
- Important point highlight করতে annotation ব্যবহার করা শিখবো
- Arrow দিয়ে specific point দেখানো শিখবো
- Data storytelling improve করা শিখবো
- Real dataset chart-এ insight explain করা শিখবো

---

## 📚 Topics Covered

- `plt.text()`
- `annotate()`
- Arrow annotation
- Highlighting points
- Dynamic labeling
- Watermarking
- Custom positioning

---

## 📁 Project Structure

```bash
day-10/
│── 01_basic_text.py
│── 02_annotate_basic.py
│── 03_arrow_annotation.py
│── 04_highlight_points.py
│── 05_dynamic_labels.py
│── 06_watermark.py
│── 07_custom_positioning.py
│── 08_real_storytelling_chart.py
│── sales_growth.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** sales_growth.csv
- **Description:** Monthly sales and profit growth data used for annotation and storytelling visualization

### Columns:

- month → Month name
- sales → Monthly sales amount
- profit → Monthly profit amount

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry)

### 🔹 Purpose

- Text and annotation concept বোঝা
- Chart-এর ভিতরে explanation add করা শেখা

### 🧾 Code

```python
print("Text & Annotation Day 10 📊")
```

### 🧠 Explanation

- Visualization শুধু graph না, explanationও হতে পারে
- Text add করলে chart আরও meaningful হয়

---

## 📄 2. analysis.py

### 🔹 Purpose

- Important points identify করা

### 🧾 Code

```python
def find_peak(values):
    return max(values)
```

### 🧠 Explanation

- Highest value বের করতে সাহায্য করে
- Annotation দেওয়ার আগে useful analysis করে

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper functions

### 🧾 Code

```python
def format_label(text):
    return text.upper()
```

### 🧠 Explanation

- Text formatting সহজ করে
- Reusable helper হিসেবে কাজ করে

---

## 📄 4. 01_basic_text.py

### 🔹 Purpose

- Graph-এর উপর simple text add করা

### 🧾 Code

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y, marker="o")

plt.text(2, 20, "Mid Point", fontsize=12, color="red")

plt.title("Basic Text Example")
plt.show()
```

### 🧠 Explanation

- `plt.text()` নির্দিষ্ট position-এ text বসায়
- `x=2, y=20` position-এ “Mid Point” লেখা হয়েছে
- Graph-এর explanation দিতে useful

---

## 📄 5. 02_annotate_basic.py

### 🔹 Purpose

- Specific point highlight করা

### 🧾 Code

```python
plt.annotate(
    "Peak Point",
    xy=(4, 25),
    xytext=(2, 30),
    arrowprops=dict(facecolor="black", arrowstyle="->")
)
```

### 🧠 Explanation

- `xy` → highlight করা point
- `xytext` → text কোথায় বসবে
- `arrowprops` → arrow draw করে
- Important data point explain করা সহজ হয়

---

## 📄 6. 03_arrow_annotation.py

### 🔹 Purpose

- Arrow দিয়ে change point দেখানো

### 🧾 Code

```python
plt.annotate(
    "Increase Point",
    xy=(2, 8),
    xytext=(3, 12),
    arrowprops=dict(
        arrowstyle="->",
        color="red",
        lw=2
    )
)
```

### 🧠 Explanation

- Arrow important movement দেখায়
- Trend change বা event highlight করতে ব্যবহার হয়

---

## 📄 7. 04_highlight_points.py

### 🔹 Purpose

- Important point visually highlight করা

### 🧾 Code

```python
plt.scatter([4], [25], color="red", s=100)
plt.text(4, 25, "Max Value", fontsize=12, color="red")
```

### 🧠 Explanation

- Max value আলাদা করে দেখানো হয়েছে
- Scatter marker + text combination use করা হয়েছে

---

## 📄 8. 05_dynamic_labels.py

### 🔹 Purpose

- প্রতিটি point-এর label automatically দেখানো

### 🧾 Code

```python
for i in range(len(x)):
    plt.text(x[i], y[i] + 0.5, str(y[i]), ha="center")
```

### 🧠 Explanation

- Loop ব্যবহার করে সব point label করা হয়েছে
- Dynamic labeling data বুঝতে সাহায্য করে

---

## 📄 9. 06_watermark.py

### 🔹 Purpose

- Watermark add করা

### 🧾 Code

```python
plt.text(
    2.5, 5,
    "CONFIDENTIAL",
    fontsize=30,
    color="gray",
    alpha=0.3,
    rotation=30
)
```

### 🧠 Explanation

- Watermark report/dashboard look দেয়
- `alpha` দিয়ে transparency control করা হয়েছে
- `rotation` text ঘুরিয়ে দিয়েছে

---

## 📄 10. 07_custom_positioning.py

### 🔹 Purpose

- Text-এর exact position control করা

### 🧾 Code

```python
plt.text(1, 3, "Start", fontsize=12)
plt.text(5, 15, "End", fontsize=12)
```

### 🧠 Explanation

- Beginning এবং ending point label করা হয়েছে
- Exact positioning storytelling improve করে

---

## 📄 11. 08_real_storytelling_chart.py

### 🔹 Purpose

- Real dataset-এ annotation ব্যবহার করে story বলা

### 🧾 Code

```python
import matplotlib.pyplot as plt
import csv

months = []
sales = []
profit = []

with open("sales_growth.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        months.append(row["month"])
        sales.append(int(row["sales"]))
        profit.append(int(row["profit"]))

plt.plot(months, sales, marker="o", label="Sales")
plt.plot(months, profit, marker="s", label="Profit")

max_index = sales.index(max(sales))

plt.scatter(months[max_index], sales[max_index], color="red", s=100)

plt.annotate(
    "Highest Sales",
    xy=(months[max_index], sales[max_index]),
    xytext=(1, 250),
    arrowprops=dict(arrowstyle="->", color="red")
)

plt.title("Sales Growth Storytelling")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()

plt.show()
```

### 🧠 Explanation

- CSV data থেকে sales/profit load করা হয়েছে
- Highest sales point automatically find করা হয়েছে
- Annotation দিয়ে insight explain করা হয়েছে
- Chart-এর মাধ্যমে story বলা হয়েছে

---

## ⚙️ Implementation Flow

- Simple text add করা হয়েছে
- Annotation দিয়ে point highlight করা হয়েছে
- Arrow ব্যবহার করে explanation দেওয়া হয়েছে
- Dynamic labels তৈরি করা হয়েছে
- Watermark এবং custom positioning শিখা হয়েছে
- Real dataset-এর উপর storytelling chart বানানো হয়েছে

---

## 📈 Output / Result

### Key findings:

- Text chart-কে readable করে
- Annotation insight explain করতে সাহায্য করে
- Arrow visual focus তৈরি করে
- Dynamic labels data clarity বাড়ায়
- Real chart storytelling business insight দেয়

---

## 🚀 What I Learned

- `plt.text()` ব্যবহার করে graph-এ text বসানো
- `annotate()` দিয়ে point explain করা
- Arrow annotation দিয়ে highlight করা
- Dynamic labeling concept
- Data storytelling with visualization

---

## 🧠 Key Concepts (Quick Revision)

- `plt.text()` → নির্দিষ্ট জায়গায় text বসায়
- `annotate()` → point explain করে
- `xy` → target point
- `xytext` → text position
- `arrowprops` → arrow style
- watermark → light background text
- dynamic labels → loop দিয়ে labels

---

## 📝 Notes

- Text overlap হতে পারে, তাই position carefully দিতে হয়
- Arrow style chart readable করতে সাহায্য করে
- বেশি annotation দিলে graph clutter হতে পারে
- Important point ছাড়া সব জায়গায় text দেওয়া উচিত না

---

## 📌 Next Day Preview

- Axis customization
- Axis limits
- Tick formatting
- Log scale
- Dual axis plotting

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Auto-detect peak points
- Multiple annotations add করা
- Business storytelling dashboard বানানো
- Color-coded insight labels ব্যবহার করা

### 🧪 Practice Ideas

- Sales chart-এ highest month highlight করো
- Marks chart-এ top student label করো
- Profit growth graph-এ change point annotate করো
- Watermark দিয়ে report-style chart বানাও
