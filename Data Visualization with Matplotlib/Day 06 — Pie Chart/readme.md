# 📅 Day 6 — Pie Chart

## 🎯 Objective

- আজকে Pie Chart কী সেটা শিখবো
- Part-to-whole relationship visualize করা শিখবো
- Labels, percentage, explode, shadow, colors ব্যবহার শিখবো
- Donut chart এবং real dataset visualization বুঝবো

---

## 📚 Topics Covered

- Pie chart basics
- labels
- autopct
- explode
- shadow
- Start angle
- Custom colors
- Donut chart
- Pie chart limitations

---

## 📁 Project Structure

```bash
day-6/
│── 01_basic_pie_chart.py
│── 02_labels_autopct.py
│── 03_explode_pie.py
│── 04_shadow_startangle_colors.py
│── 05_donut_chart.py
│── 06_pie_chart_limitation.py
│── 07_real_dataset_pie_chart.py
│── market_share.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** market_share.csv
- **Description:** Company market share dataset used to visualize percentage distribution

### Columns:

- company → Company name
- share → Market share percentage

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry)

### 🔹 Purpose

- Pie chart concept বোঝা
- Part-to-whole visualization idea পাওয়া

### 🧾 Code

```python id="pie_main6"
print("Pie Chart Day 6 📊")
```

### 🧠 Explanation

- Pie chart পুরো data কে percentage আকারে দেখায়
- Total = 100%

---

## 📄 2. analysis.py

### 🔹 Purpose

- Percentage distribution logic বোঝানো

### 🧾 Code

```python id="pie_analysis6"
def distribution():
    return "Part-to-whole percentage analysis"
```

### 🧠 Explanation

- Data কে ভাগে ভাগে দেখায়
- Business analytics এ খুব ব্যবহার হয়

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper function

### 🧾 Code

```python id="pie_utils6"
def format_label(label):
    return label.upper()
```

### 🧠 Explanation

- Labels clean এবং readable করে
- Reusable helper logic

---

## 📄 4. 01_basic_pie_chart.py

### 🔹 Purpose

- Basic pie chart তৈরি করা

### 🧾 Code

```python id="pie1"
import matplotlib.pyplot as plt

activities = ["Study", "Sleep", "Play", "Others"]
hours = [6, 8, 4, 6]

plt.pie(hours)

plt.title("Basic Pie Chart")
plt.show()
```

### 🧠 Explanation

- `plt.pie()` → percentage-based chart তৈরি করে
- Whole data কে slices এ ভাগ করে

---

## 📄 5. 02_labels_autopct.py

### 🔹 Purpose

- Labels এবং percentage দেখানো

### 🧾 Code

```python id="pie2"
plt.pie(
    hours,
    labels=activities,
    autopct="%1.1f%%"
)
```

### 🧠 Explanation

- `labels` → category name দেখায়
- `autopct` → percentage দেখায়

---

## 📄 6. 03_explode_pie.py

### 🔹 Purpose

- Highlight slice করা

### 🧾 Code

```python id="pie3"
explode = [0.1, 0, 0, 0]

plt.pie(
    hours,
    labels=activities,
    autopct="%1.1f%%",
    explode=explode
)
```

### 🧠 Explanation

- `explode` → slice আলাদা করে highlight করে
- Important category emphasize করতে ব্যবহার হয়

---

## 📄 7. 04_shadow_startangle_colors.py

### 🔹 Purpose

- Advanced styling শেখা

### 🧾 Code

```python id="pie4"
plt.pie(
    hours,
    labels=activities,
    autopct="%1.1f%%",
    colors=colors,
    shadow=True,
    startangle=90
)
```

### 🧠 Explanation

- `shadow=True` → 3D effect দেয়
- `startangle` → rotation control করে
- `colors` → custom design

---

## 📄 8. 05_donut_chart.py

### 🔹 Purpose

- Donut chart তৈরি করা

### 🧾 Code

```python id="pie5"
plt.pie(
    hours,
    labels=activities,
    autopct="%1.1f%%",
    wedgeprops={"width": 0.4}
)
```

### 🧠 Explanation

- মাঝখানে hole তৈরি হয়
- Modern dashboard visualization এ ব্যবহার হয়

---

## 📄 9. 06_pie_chart_limitation.py

### 🔹 Purpose

- Pie chart limitation বোঝা

### 🧾 Code

```python id="pie6"
plt.pie(values, labels=labels, autopct="%1.1f%%")
```

### 🧠 Explanation

- অনেক category হলে readability কমে যায়
- Similar values compare করা কঠিন

---

## 📄 10. 07_real_dataset_pie_chart.py

### 🔹 Purpose

- Real market share analysis

### 🧾 Code

```python id="pie7"
import csv
import matplotlib.pyplot as plt

companies = []
shares = []

with open("market_share.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        companies.append(row["company"])
        shares.append(int(row["share"]))

colors = ["gold", "skyblue", "lightgreen", "orange", "lightgray"]

plt.pie(
    shares,
    labels=companies,
    autopct="%1.1f%%",
    colors=colors,
    startangle=140,
    shadow=True
)

plt.title("Market Share Distribution")
plt.show()
```

### 🧠 Explanation

- Company market share visualize করা হয়েছে
- Business insight পাওয়া যায়
- Percentage comparison সহজ হয়

---

## ⚙️ Implementation Flow

- Pie chart concept শেখা হয়েছে
- Part-to-whole visualization বোঝা হয়েছে
- Labels এবং percentage add করা হয়েছে
- Explode effect ব্যবহার করা হয়েছে
- Styling (shadow, colors, rotation) শেখা হয়েছে
- Real dataset analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Pie chart percentage distribution দেখায়
- Market share easily compare করা যায়
- Explode highlight করতে সাহায্য করে
- Too many slices হলে readability কমে

---

## 🚀 What I Learned

- Pie chart কীভাবে কাজ করে
- Percentage representation concept
- Explode effect
- Donut chart structure
- Real-world market share analysis

---

## 🧠 Key Concepts (Quick Revision)

- `plt.pie()` → percentage chart
- labels → category name
- autopct → percentage show
- explode → highlight slice
- shadow → 3D effect
- startangle → rotation control
- donut chart → hole in center

---

## 📝 Notes

- Too many categories হলে pie chart avoid করা ভালো
- Percentage calculation automatically normalized হয়
- Colors carefully choose করতে হয়
- Large datasets এ bar chart better

---

## 📌 Next Day Preview

- Figure & Axes deep understanding
- Subplots system
- Multiple charts in one figure
- Layout control
- Professional dashboard design

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Animated pie chart তৈরি করা
- Interactive dashboard বানানো
- Real business report design করা
- More categories add করা

### 🧪 Practice Ideas

- Daily time usage pie chart বানাও
- Expense breakdown visualize করো
- Population distribution chart তৈরি করো
- App usage percentage analysis করো
