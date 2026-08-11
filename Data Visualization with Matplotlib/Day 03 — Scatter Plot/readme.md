# 📅 Day 3 — Scatter Plot

## 🎯 Objective

- আজকে Scatter Plot শিখবো
- দুইটা variable এর relationship visualize করা শিখবো
- Correlation (positive, negative, no relation) বুঝবো
- Size (s), Color (c), Marker, Alpha ব্যবহার শিখবো
- Real dataset দিয়ে scatter analysis করা শিখবো

---

## 📚 Topics Covered

- Basic scatter plot
- Relationship visualization
- Positive correlation
- Negative correlation
- No correlation
- `s` (size)
- `c` (color)
- `marker`
- `alpha`
- Multiple scatter plots
- Bubble chart concept

---

## 📁 Project Structure

```bash
day-3/
│── 01_basic_scatter.py
│── 02_positive_negative_no_correlation.py
│── 03_size_s_and_color_c.py
│── 04_marker_alpha.py
│── 05_multiple_scatter.py
│── 06_bubble_chart.py
│── 07_real_scatter_dataset.py
│── student_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** student_data.csv
- **Description:** Student performance dataset used to analyze relationship between study hours, marks, and attendance

### Columns:

- study_hours → কত ঘন্টা পড়াশোনা করা হয়েছে
- marks → পরীক্ষার নম্বর
- attendance → ক্লাস উপস্থিতি (%)

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept entry)

### 🔹 Purpose

- Scatter plot concept বোঝা
- Data relationship visualize করা

### 🧾 Code

```python
print("Scatter Plot Day 3 🚀")
```

### 🧠 Explanation

- Scatter plot দিয়ে দুই variable এর relation দেখা হয়
- Each point = one observation

---

## 📄 2. analysis.py

### 🔹 Purpose

- Correlation concept বুঝানো

### 🧾 Code

```python
def correlation_type():
    return "Positive / Negative / No correlation"
```

### 🧠 Explanation

- Data relation বুঝার base function
- Visualization logic support করে

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper logic

### 🧾 Code

```python
def format_label(label):
    return label.upper()
```

### 🧠 Explanation

- Labels clean & readable করতে সাহায্য করে
- Reusable helper function

---

## 📄 4. 01_basic_scatter.py

### 🔹 Purpose

- Basic scatter plot তৈরি করা

### 🧾 Code

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.scatter(x, y)

plt.title("Basic Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()
```

### 🧠 Explanation

- `plt.scatter()` → point-based graph তৈরি করে
- X-Y relation visualize করা হয়
- Each dot = one data point

---

## 📄 5. 02_positive_negative_no_correlation.py

### 🔹 Purpose

- Correlation types compare করা

### 🧾 Code

```python
plt.subplot(1, 3, 1)
plt.scatter(x1, y1)

plt.subplot(1, 3, 2)
plt.scatter(x2, y2)

plt.subplot(1, 3, 3)
plt.scatter(x3, y3)
```

### 🧠 Explanation

- Positive correlation → দুইটা variable একসাথে বাড়ে
- Negative correlation → এক বাড়লে অন্য কমে
- No correlation → কোনো pattern নাই

---

## 📄 6. 03_size_s_and_color_c.py

### 🔹 Purpose

- Size এবং color দিয়ে data represent করা

### 🧾 Code

```python
plt.scatter(
    x, y,
    s=sizes,
    c=colors,
    cmap="viridis"
)
```

### 🧠 Explanation

- `s` → point size (importance দেখায়)
- `c` → color intensity
- `cmap` → color theme

---

## 📄 7. 04_marker_alpha.py

### 🔹 Purpose

- Marker style + transparency শেখা

### 🧾 Code

```python
plt.scatter(
    x, y,
    marker="o",
    alpha=0.5,
    s=200
)
```

### 🧠 Explanation

- `marker` → shape of point
- `alpha` → transparency control
- Overlap visualization clear করে

---

## 📄 8. 05_multiple_scatter.py

### 🔹 Purpose

- Multiple dataset compare করা

### 🧾 Code

```python
plt.scatter(x1, y1, color="blue", label="Group A")
plt.scatter(x2, y2, color="red", label="Group B")

plt.legend()
```

### 🧠 Explanation

- এক graph এ multiple group compare করা যায়
- `legend()` দিয়ে identify করা হয়

---

## 📄 9. 06_bubble_chart.py

### 🔹 Purpose

- Bubble chart concept বোঝা

### 🧾 Code

```python
plt.scatter(x, y, s=sizes, alpha=0.5, color="green")
```

### 🧠 Explanation

- Bubble size = importance
- Bigger value → bigger circle
- Business analytics এ খুব use হয়

---

## 📄 10. 07_real_scatter_dataset.py

### 🔹 Purpose

- Real dataset analysis (study vs marks)

### 🧾 Code

```python
import matplotlib.pyplot as plt
import csv

study_hours = []
marks = []
attendance = []

with open("student_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        study_hours.append(int(row["study_hours"]))
        marks.append(int(row["marks"]))
        attendance.append(int(row["attendance"]))

plt.scatter(
    study_hours,
    marks,
    s=attendance,
    alpha=0.6,
    color="purple"
)

plt.title("Study Hours vs Marks (Bubble = Attendance)")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()
```

### 🧠 Explanation

- Study hours increase হলে marks increase দেখা যায়
- Attendance কে bubble size হিসেবে ব্যবহার করা হয়েছে
- Real-world correlation analysis করা হয়েছে

---

## ⚙️ Implementation Flow

- Scatter plot concept শেখা হয়েছে
- Correlation types visualize করা হয়েছে
- Size, color, marker ব্যবহার করা হয়েছে
- Multiple dataset compare করা হয়েছে
- Bubble chart তৈরি করা হয়েছে
- Real dataset analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Study hours vs marks → positive correlation
- Scatter plot relationship বুঝতে best tool
- Bubble chart extra dimension add করে
- Transparency overlapping data clear করে

---

## 🚀 What I Learned

- Scatter plot কিভাবে কাজ করে
- Correlation concept (positive/negative/no relation)
- Size and color mapping
- Real dataset analysis
- Bubble chart concept

---

## 🧠 Key Concepts (Quick Revision)

- `plt.scatter()` → point graph
- Positive correlation → both increase
- Negative correlation → one increases other decreases
- `s` → size
- `c` → color
- `alpha` → transparency
- `marker` → shape
- Bubble chart → size-based scatter

---

## 📝 Notes

- Data type integer না হলে error হতে পারে
- Large dataset এ scatter slow হতে পারে
- Legend না দিলে multiple group confusing হয়
- Size scaling careful করতে হয়

---

## 📌 Next Day Preview

- Histogram basics
- Distribution understanding
- Frequency visualization
- Bins concept
- Real-world data distribution

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Different datasets compare করা
- Interactive scatter chart
- Regression line add করা
- Color mapping improve করা

### 🧪 Practice Ideas

- Height vs weight scatter plot বানাও
- Temperature vs ice cream sales plot করো
- Attendance vs marks bubble chart extend করো
- Add 3rd dataset compare করো
