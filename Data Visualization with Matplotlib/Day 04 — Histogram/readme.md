# 📅 Day 4 — Histogram

## 🎯 Objective

- আজকে Histogram কী সেটা শিখবো
- Data distribution কিভাবে বুঝতে হয় সেটা শিখবো
- Frequency-based visualization তৈরি করা শিখবো
- Bins, density, styling এবং real dataset analysis শিখবো

---

## 📚 Topics Covered

- Distribution understanding
- Frequency visualization
- bins
- Custom bins
- edgecolor
- Density histogram
- Multiple histograms
- Histogram styling
- Real-world examples

---

## 📁 Project Structure

```bash
day-4/
│── 01_basic_histogram.py
│── 02_bins_explained.py
│── 03_custom_bins.py
│── 04_edgecolor_styling.py
│── 05_density_histogram.py
│── 06_multiple_histograms.py
│── 07_histogram_styling.py
│── 08_real_world_histogram.py
│── exam_scores.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** exam_scores.csv
- **Description:** Students exam score distribution dataset used to analyze performance spread

### Columns:

- student → Student name/ID
- score → Exam marks

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept entry)

### 🔹 Purpose

- Histogram concept বোঝা
- Data distribution idea পাওয়া

### 🧾 Code

```python id="main_day4"
print("Histogram Day 4 📊")
```

### 🧠 Explanation

- Histogram data কে ranges এ ভাগ করে দেখায়
- Frequency distribution বুঝতে সাহায্য করে

---

## 📄 2. analysis.py

### 🔹 Purpose

- Distribution analysis concept

### 🧾 Code

```python id="analysis_day4"
def distribution_type():
    return "Frequency based data distribution"
```

### 🧠 Explanation

- Data কোন range এ কত আছে সেটা বুঝায়
- Statistical analysis এর base tool

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper functions

### 🧾 Code

```python id="utils_day4"
def format_label(text):
    return text.upper()
```

### 🧠 Explanation

- Labels clean & readable করতে সাহায্য করে
- Reusable helper function

---

## 📄 4. 01_basic_histogram.py

### 🔹 Purpose

- Basic histogram তৈরি করা

### 🧾 Code

```python id="hist1"
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
         95, 40, 42, 47, 53, 58, 62, 68, 72, 78]

plt.hist(marks)

plt.title("Basic Histogram")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")

plt.show()
```

### 🧠 Explanation

- `plt.hist()` → distribution show করে
- Data কতগুলো range এ ছড়ানো আছে বোঝা যায়
- Frequency = কতবার data এসেছে

---

## 📄 5. 02_bins_explained.py

### 🔹 Purpose

- Bins concept বোঝা

### 🧾 Code

```python id="bins1"
plt.hist(marks, bins=5, color="blue")
```

### 🧠 Explanation

- `bins` → data grouping interval
- কম bins = broad view
- বেশি bins = detailed view

---

## 📄 6. 03_custom_bins.py

### 🔹 Purpose

- Custom range define করা

### 🧾 Code

```python id="custom_bins"
bins = [0, 20, 40, 60, 80, 100]
plt.hist(marks, bins=bins, color="green", edgecolor="black")
```

### 🧠 Explanation

- নিজে range define করা যায়
- Real-world grading system এ ব্যবহার হয়

---

## 📄 7. 04_edgecolor_styling.py

### 🔹 Purpose

- Histogram styling improve করা

### 🧾 Code

```python id="edge"
plt.hist(
    marks,
    bins=6,
    color="orange",
    edgecolor="black"
)
```

### 🧠 Explanation

- `edgecolor` → bar border clear করে
- Graph readable হয়

---

## 📄 8. 05_density_histogram.py

### 🔹 Purpose

- Probability distribution শেখা

### 🧾 Code

```python id="density"
plt.hist(
    marks,
    bins=5,
    density=True,
    color="purple",
    alpha=0.7
)
```

### 🧠 Explanation

- `density=True` → frequency → probability
- Statistical analysis এ ব্যবহার হয়

---

## 📄 9. 06_multiple_histograms.py

### 🔹 Purpose

- দুই dataset compare করা

### 🧾 Code

```python id="multi_hist"
plt.hist(class_a, bins=5, alpha=0.6, label="Class A")
plt.hist(class_b, bins=5, alpha=0.6, label="Class B")
```

### 🧠 Explanation

- দুই distribution এক graph এ compare করা যায়
- `alpha` overlap clear করে

---

## 📄 10. 07_histogram_styling.py

### 🔹 Purpose

- Professional histogram styling

### 🧾 Code

```python id="style_hist"
plt.hist(
    data,
    bins=6,
    color="teal",
    edgecolor="black",
    alpha=0.8
)
plt.grid(True)
```

### 🧠 Explanation

- Grid add করলে readability বাড়ে
- Clean visualization তৈরি হয়

---

## 📄 11. 08_real_world_histogram.py

### 🔹 Purpose

- Real dataset analysis

### 🧾 Code

```python id="real_hist"
import csv
import matplotlib.pyplot as plt

scores = []

with open("exam_scores.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        scores.append(int(row["score"]))

plt.hist(
    scores,
    bins=[40, 50, 60, 70, 80, 90, 100],
    color="purple",
    edgecolor="black"
)

plt.title("Exam Score Distribution")
plt.show()
```

### 🧠 Explanation

- CSV থেকে real data read করা হয়েছে
- Score distribution visualize করা হয়েছে
- Education analytics এ useful

---

## ⚙️ Implementation Flow

- Histogram concept শেখা হয়েছে
- Data distribution visualize করা হয়েছে
- Bins concept ব্যবহার করা হয়েছে
- Density (probability) analysis করা হয়েছে
- Multiple dataset compare করা হয়েছে
- Real dataset analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Most students মাঝামাঝি score পায়
- Histogram data distribution বুঝতে best tool
- Bins change করলে view change হয়
- Real dataset analysis pattern বের করে

---

## 🚀 What I Learned

- Histogram কীভাবে কাজ করে
- Frequency distribution ধারণা
- Bins concept
- Density vs frequency difference
- Real dataset analysis

---

## 🧠 Key Concepts (Quick Revision)

- `plt.hist()` → distribution plot
- bins → grouping range
- frequency → count of values
- density → probability form
- edgecolor → bar border
- alpha → transparency

---

## 📝 Notes

- Too few bins → detail lose হয়
- Too many bins → noisy graph হয়
- Data type numeric হওয়া জরুরি
- CSV read করার সময় int conversion দরকার

---

## 📌 Next Day Preview

- Bar chart basics
- Category comparison
- Grouped bar chart
- Stacked bar chart
- Real dataset visualization

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Different bin strategies test করা
- Multiple datasets compare করা
- Normal distribution overlay করা
- Interactive histogram তৈরি করা

### 🧪 Practice Ideas

- Height distribution plot করো
- Class marks distribution analyze করো
- Age distribution histogram বানাও
- Sales range distribution visualize করো
