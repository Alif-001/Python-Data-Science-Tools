# 📅 Day 13 — Violin Plot

## 🎯 Objective

- আজকে Violin Plot এর concept শিখবো
- Data distribution এর shape বুঝতে শিখবো
- Density-based visualization analyze করা শিখবো
- Multiple category compare করা শিখবো
- Box plot vs Violin plot পার্থক্য বুঝবো
- Real dataset দিয়ে student performance analyze করা শিখবো

---

## 📚 Topics Covered

- Violin plot concept
- Distribution shape visualization
- Category comparison
- Violin plot styling
- Box plot vs violin plot comparison
- Real dataset analysis

---

## 📁 Project Structure

```bash
day-13/
│── 01_basic_violin_plot.py
│── 02_distribution_shape.py
│── 03_compare_categories.py
│── 04_violin_styling.py
│── 05_box_vs_violin.py
│── 06_real_dataset_violin.py
│── student_scores.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** student_scores.csv
- **Description:** Students subject-wise marks used for distribution analysis

### Columns:

- student → Student name
- math → Math score
- science → Science score
- english → English score

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py

### 🔹 Purpose

- Violin plot concept introduction
- Distribution visualization idea বোঝা

### 🧾 Code

```python id="p2l8zq"
print("Day 13 - Violin Plot 🎻")
```

### 🧠 Explanation

- Violin plot = distribution + density visualization
- Data shape বুঝতে সাহায্য করে

---

## 📄 2. analysis.py

### 🔹 Purpose

- Data spread analysis

### 🧾 Code

```python id="g8h3qk"
def get_stats(data):
    return min(data), max(data)
```

### 🧠 Explanation

- Minimum এবং maximum value বের করে
- Distribution range বুঝতে সাহায্য করে

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper functions

### 🧾 Code

```python id="xk2m9a"
def normalize(value):
    return float(value)
```

### 🧠 Explanation

- Data normalize করতে সাহায্য করে
- CSV value handling সহজ করে

---

## 📄 4. 01_basic_violin_plot.py

### 🔹 Purpose

- Basic violin plot তৈরি করা

### 🧾 Code

```python id="v1a2b3"
plt.violinplot(data)
```

### 🧠 Explanation

- Data distribution দেখায়
- Density কোথায় বেশি তা বুঝা যায়

---

## 📄 5. 02_distribution_shape.py

### 🔹 Purpose

- Distribution shape compare করা

### 🧾 Code

```python id="c9d8e7"
plt.violinplot([data1, data2])
```

### 🧠 Explanation

- দুইটা dataset এর shape compare করা হয়
- Spread এবং concentration দেখা যায়

---

## 📄 6. 03_compare_categories.py

### 🔹 Purpose

- Multiple category comparison

### 🧾 Code

```python id="m3n4p5"
plt.violinplot(data)
plt.xticks([1, 2, 3], ["Class A", "Class B", "Class C"])
```

### 🧠 Explanation

- Different classes compare করা হয়েছে
- Performance distribution বোঝা যায়

---

## 📄 7. 04_violin_styling.py

### 🔹 Purpose

- Violin plot styling করা

### 🧾 Code

```python id="s7t8u9"
vp = plt.violinplot(data, showmeans=True, showmedians=True)

for body in vp['bodies']:
    body.set_facecolor("lightblue")
    body.set_edgecolor("black")
```

### 🧠 Explanation

- Mean এবং median show করা হয়েছে
- Color styling করা হয়েছে
- Better visualization তৈরি হয়

---

## 📄 8. 05_box_vs_violin.py

### 🔹 Purpose

- Box plot vs Violin plot comparison

### 🧾 Code

```python id="b1v2c3"
plt.subplot(1, 2, 1)
plt.boxplot(data)

plt.subplot(1, 2, 2)
plt.violinplot(data)
```

### 🧠 Explanation

- Box plot → summary view
- Violin plot → detailed distribution shape
- দুটো একসাথে compare করা হয়েছে

---

## 📄 9. 06_real_dataset_violin.py

### 🔹 Purpose

- Real student score analysis

### 🧾 Code

```python id="r8s9t0"
import csv

math = []
science = []
english = []

with open("student_scores.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        math.append(int(row["math"]))
        science.append(int(row["science"]))
        english.append(int(row["english"]))

plt.violinplot([math, science, english])
```

### 🧠 Explanation

- CSV থেকে subject-wise data load করা হয়েছে
- Math, Science, English distribution analyze করা হয়েছে
- Student performance pattern বোঝা যায়

---

## ⚙️ Implementation Flow

- Violin plot concept শিখা হয়েছে
- Distribution shape analyze করা হয়েছে
- Multiple categories compare করা হয়েছে
- Styling apply করা হয়েছে
- Box plot vs violin plot compare করা হয়েছে
- Real dataset analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Violin plot data density দেখায়
- Distribution shape easily visualize করা যায়
- Multiple groups compare করা যায়
- Box plot থেকে বেশি detailed insight পাওয়া যায়
- Student performance pattern বোঝা যায়

---

## 🚀 What I Learned

- Violin plot concept (distribution + density)
- Category-wise comparison
- Styling violin plots
- Box vs violin difference
- Real dataset visualization

---

## 🧠 Key Concepts (Quick Revision)

- Violin plot → distribution shape visualization
- Density → data concentration
- `plt.violinplot()` → main function
- `showmeans=True` → mean show করে
- `showmedians=True` → median show করে
- Box plot → summary view
- Violin plot → detailed view

---

## 📝 Notes

- Small dataset হলে violin plot misleading হতে পারে
- Density interpretation practice দরকার
- Box plot simpler কিন্তু less detailed
- Violin plot powerful for analysis
- Over-styling avoid করা উচিত

---

## 📌 Next Day Preview

- Area Plot
- Stack Plot
- Cumulative visualization
- Multi-series trend analysis
- Business growth charts

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Student performance analytics dashboard
- Automatic distribution detector
- Subject comparison tool
- Interactive violin plot viewer

### 🧪 Practice Ideas

- Exam score distribution system
- Salary distribution analysis
- Product rating distribution
- Class performance comparison tool
