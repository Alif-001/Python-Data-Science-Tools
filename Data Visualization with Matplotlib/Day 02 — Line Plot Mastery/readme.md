# 📅 Day 2 — Line Plot Mastery

## 🎯 Objective

- আজকে Multiple Line Plot শিখবো
- Graph customization (color, style, marker) শিখবো
- Data comparison visualization বুঝবো
- Real dataset (CSV) থেকে plot করা শিখবো

## 📚 Topics Covered

- Multiple line plots
- color
- linewidth
- linestyle
- marker
- markersize
- alpha
- legend()
- grid()
- Custom ticks
- Real dataset line plotting

## 📁 Project Structure

```bash
day-2/
│── 01_multiple_line_plots.py
│── 02_colors_and_linewidth.py
│── 03_linestyle_marker.py
│── 04_alpha_transparency.py
│── 05_legend_grid.py
│── 06_custom_ticks.py
│── 07_real_dataset_plot.py
│── sales_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** sales_data.csv
- **Description:** Monthly sales and profit data used to visualize trends using line plots

### Columns:

- month → Month name (Jan, Feb, etc.)
- sales → Total sales value
- profit → Profit value

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Optional concept entry)

> (এই project এ আলাদা main file না থাকলেও concept flow বোঝার জন্য রাখা যায়)

#### 🔹 Purpose

- Overall plotting concept বোঝা
- Multiple plots একসাথে কিভাবে কাজ করে idea পাওয়া

#### 🧾 Code

```python
# Concept only - no execution logic
print("Line Plot Mastery Day 2 🚀")
```

#### 🧠 Explanation

- Line plots ব্যবহার করে data compare করা হয়
- Visualization trends বুঝতে সাহায্য করে

---

## 📄 2. analysis.py (Concept helper)

#### 🔹 Purpose

- Plotting data analysis logic বোঝানো

#### 🧾 Code

```python
# Concept explanation only

def compare_data(a, b):
    return "Comparing two datasets visually"
```

#### 🧠 Explanation

- Function ব্যবহার করা হয়েছে concept বুঝানোর জন্য
- Real plotting এ একই logic visualization হয়

---

## 📄 3. utils.py (if any)

#### 🔹 Purpose

- Helper logic for plotting concepts

#### 🧾 Code

```python
def format_label(text):
    return text.upper()
```

#### 🧠 Explanation

- Reusable formatting function
- Labels clean করার জন্য ব্যবহার করা যায়

---

## 📄 4. `01_multiple_line_plots.py`

#### 🔹 Purpose

- একাধিক line এক graph এ plot করা

#### 🧾 Code

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1)
plt.plot(x, y2)

plt.title("Multiple Line Plot Example")
plt.show()
```

#### 🧠 Explanation

- একাধিক dataset এক graph এ compare করা যায়
- `plt.plot()` multiple times ব্যবহার করা হয়েছে
- Trend comparison সহজ হয়

---

## 📄 5. `02_colors_and_linewidth.py`

#### 🔹 Purpose

- Line styling শিখা (color + thickness)

#### 🧾 Code

```python
plt.plot(x, y, color="red", linewidth=3)
```

#### 🧠 Explanation

- `color` → line এর color change করে
- `linewidth` → line মোটা/পাতলা করে
- Visualization clearer হয়

---

## 📄 6. `03_linestyle_marker.py`

#### 🔹 Purpose

- Line style এবং marker add করা

#### 🧾 Code

```python
plt.plot(
    x, y,
    color="blue",
    linestyle="--",
    marker="o",
    markersize=8
)
```

#### 🧠 Explanation

- `linestyle="--"` → dashed line
- `marker="o"` → data points highlight করে
- `markersize` → point size control করে

---

## 📄 7. `04_alpha_transparency.py`

#### 🔹 Purpose

- Transparency control শেখা

#### 🧾 Code

```python
plt.plot(x, y, color="green", alpha=0.4, linewidth=4)
```

#### 🧠 Explanation

- `alpha=0.4` → line semi-transparent
- Overlapping graph বুঝতে সাহায্য করে

---

## 📄 8. `05_legend_grid.py`

#### 🔹 Purpose

- Legend এবং grid add করা

#### 🧾 Code

```python
plt.plot(x, y1, label="Line A")
plt.plot(x, y2, label="Line B")

plt.legend()
plt.grid(True)
```

#### 🧠 Explanation

- `legend()` → কোন line কী তা identify করে
- `grid()` → background reference lines দেয়

---

## 📄 9. `06_custom_ticks.py`

#### 🔹 Purpose

- Axis labels customize করা

#### 🧾 Code

```python
plt.xticks([1,2,3,4,5], ["A","B","C","D","E"])
```

#### 🧠 Explanation

- numeric axis কে meaningful label এ convert করা হয়
- readability বাড়ে

---

## 📄 10. `07_real_dataset_plot.py`

#### 🔹 Purpose

- CSV data থেকে real plotting করা

#### 🧾 Code

```python
import matplotlib.pyplot as plt
import csv

months = []
sales = []
profit = []

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        months.append(row["month"])
        sales.append(int(row["sales"]))
        profit.append(int(row["profit"]))

plt.plot(months, sales, label="Sales")
plt.plot(months, profit, label="Profit")

plt.legend()
plt.grid(True)
plt.show()
```

#### 🧠 Explanation

- CSV থেকে data read করা হয়েছে
- list এ store করা হয়েছে
- Sales vs Profit compare করা হয়েছে visually

---

## ⚙️ Implementation Flow

- Multiple line plotting শেখা হয়েছে
- Graph styling (color, marker, style) করা হয়েছে
- Transparency control করা হয়েছে
- Legend & grid add করা হয়েছে
- Axis customize করা হয়েছে
- CSV dataset থেকে real plotting করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Multiple lines দিয়ে comparison সহজ হয়
- Styling graph readability বাড়ায়
- Real dataset visualization business insight দেয়
- Legend ছাড়া multiple line confusing হয়

---

## 🚀 What I Learned

- Multiple line plot তৈরি করা
- Graph styling techniques
- Marker এবং linestyle ব্যবহার
- CSV data visualization
- Real-world trend analysis

---

## 🧠 Key Concepts (Quick Revision)

- `plt.plot()` → line graph
- Multiple `plot()` → comparison
- `color` → line color
- `linewidth` → thickness
- `marker` → data point highlight
- `alpha` → transparency
- `legend()` → line identify
- `grid()` → background reference
- CSV → real dataset plotting

---

## 📝 Notes

- Legend না দিলে multiple line confusing হয়
- CSV file path ঠিক রাখতে হয়
- Integer conversion (`int()`) গুরুত্বপূর্ণ
- Axis label না দিলে understanding কমে যায়

---

## 📌 Next Day Preview

- Scatter plot basics
- Correlation understanding
- Positive / negative relation
- Bubble chart concept
- Real dataset scatter visualization

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Different datasets compare করা
- Styling theme apply করা
- Interactive visualization try করা
- More than 2 lines compare করা

### 🧪 Practice Ideas

- Temperature vs humidity plot বানাও
- Study hours vs marks compare করো
- 3rd line add করে comparison করো
- Custom labels দিয়ে graph redesign করো
