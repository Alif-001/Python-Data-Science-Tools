# 📅 Day 7 — Figure & Axes Deep Understanding

## 🎯 Objective

- আজকে Figure এবং Axes কী সেটা গভীরভাবে বুঝবো
- Subplot system ব্যবহার করা শিখবো
- Multiple plots এক figure এ তৈরি করা শিখবো
- Figure size, DPI, layout control শেখা
- Real dashboard style visualization বানানো শিখবো

---

## 📚 Topics Covered

- figure()
- axes()
- subplot()
- Figure size
- DPI
- Multiple plots in one figure
- Tight layout
- Saving figures (concept)

---

## 📁 Project Structure

```bash
day-7/
│── 01_figure_basic.py
│── 02_axes_understanding.py
│── 03_subplot_basic.py
│── 04_subplot_grid.py
│── 05_figure_size_dpi.py
│── 06_multiple_plots_one_figure.py
│── 07_tight_layout.py
│── 08_real_dashboard_style.py
│── student_performance.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** student_performance.csv
- **Description:** Student subject-wise performance dataset used for dashboard visualization

### Columns:

- student → Student name/ID
- math → Math marks
- science → Science marks
- english → English marks

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry)

### 🔹 Purpose

- Figure concept বোঝা
- Canvas (page) idea বোঝা

### 🧾 Code

```python id="fig_main7"
print("Figure & Axes Day 7 📊")
```

### 🧠 Explanation

- Figure = পুরো canvas
- সব plots এই canvas এর ভিতরে থাকে

---

## 📄 2. analysis.py

### 🔹 Purpose

- Plot structure analysis

### 🧾 Code

```python id="fig_analysis7"
def structure():
    return "Figure contains multiple axes"
```

### 🧠 Explanation

- Data visualization structure বোঝায়
- Figure → Axes relationship define করে

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper function

### 🧾 Code

```python id="fig_utils7"
def format_title(title):
    return title.upper()
```

### 🧠 Explanation

- Titles clean এবং consistent করে
- Reusable formatting logic

---

## 📄 4. 01_figure_basic.py

### 🔹 Purpose

- Basic figure তৈরি করা

### 🧾 Code

```python id="fig1"
import matplotlib.pyplot as plt

plt.figure()

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)
plt.title("Basic Figure Example")

plt.show()
```

### 🧠 Explanation

- `plt.figure()` → empty canvas তৈরি করে
- সব plots এই figure এর ভিতরে থাকে

---

## 📄 5. 02_axes_understanding.py

### 🔹 Purpose

- Axes concept বোঝা

### 🧾 Code

```python id="fig2"
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

ax.plot(x, y)
```

### 🧠 Explanation

- Axes = actual plotting area
- `add_axes()` manually position control করে

---

## 📄 6. 03_subplot_basic.py

### 🔹 Purpose

- Subplot basics

### 🧾 Code

```python id="fig3"
plt.subplot(2, 1, 1)
plt.plot(x, y1)

plt.subplot(2, 1, 2)
plt.plot(x, y2)
```

### 🧠 Explanation

- এক figure এ multiple plots
- Row-wise layout তৈরি হয়

---

## 📄 7. 04_subplot_grid.py

### 🔹 Purpose

- Grid subplot system

### 🧾 Code

```python id="fig4"
plt.subplot(2, 2, 1)
plt.subplot(2, 2, 2)
plt.subplot(2, 2, 3)
plt.subplot(2, 2, 4)
```

### 🧠 Explanation

- 2x2 grid layout
- Dashboard style visualization

---

## 📄 8. 05_figure_size_dpi.py

### 🔹 Purpose

- Figure quality control

### 🧾 Code

```python id="fig5"
plt.figure(figsize=(8, 4), dpi=120)
```

### 🧠 Explanation

- `figsize` → size control
- `dpi` → image quality control

---

## 📄 9. 06_multiple_plots_one_figure.py

### 🔹 Purpose

- Modern subplot system (axes object)

### 🧾 Code

```python id="fig6"
fig, ax = plt.subplots(2, 2)

ax[0, 0].plot([1, 2, 3], [1, 4, 9])
ax[0, 1].plot([1, 2, 3], [2, 4, 6])
```

### 🧠 Explanation

- `subplots()` → clean modern approach
- Each axis separately control করা যায়

---

## 📄 10. 07_tight_layout.py

### 🔹 Purpose

- Overlap fix করা

### 🧾 Code

```python id="fig7"
plt.tight_layout()
```

### 🧠 Explanation

- Text overlap fix করে
- Clean layout তৈরি করে

---

## 📄 11. 08_real_dashboard_style.py

### 🔹 Purpose

- Real dashboard visualization

### 🧾 Code

```python id="fig8"
fig, ax = plt.subplots(1, 3)

ax[0].bar(students, math)
ax[1].bar(students, science)
ax[2].bar(students, english)
```

### 🧠 Explanation

- 3 subject comparison dashboard
- Real analytics style visualization

---

## ⚙️ Implementation Flow

- Figure concept শেখা হয়েছে
- Axes structure বোঝা হয়েছে
- Subplot system ব্যবহার করা হয়েছে
- Grid layout তৈরি করা হয়েছে
- Figure size + DPI control করা হয়েছে
- Dashboard style visualization তৈরি করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Figure = full canvas
- Axes = plotting area
- Subplots = multiple visualization in one screen
- Dashboard style analysis possible
- Layout control important for readability

---

## 🚀 What I Learned

- Figure vs Axes difference
- Subplot system usage
- Modern `subplots()` method
- Layout optimization
- Dashboard-style plotting

---

## 🧠 Key Concepts (Quick Revision)

- `figure()` → canvas
- `axes()` → plot area
- `subplot()` → multiple plots
- `subplots()` → modern multi-plot system
- `tight_layout()` → spacing fix
- `figsize` → size control
- `dpi` → resolution

---

## 📝 Notes

- Overlapping text হলে `tight_layout()` ব্যবহার করতে হয়
- Large dashboard এ `subplots()` best
- DPI increase করলে file size বাড়ে
- Figure size properly choose করা জরুরি

---

## 📌 Next Day Preview

- Subplots mastery deep dive
- Advanced styling system
- Text & annotation
- Axis customization
- Professional dashboard design

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Interactive dashboard তৈরি করা
- Multi-page figure design
- Export high-quality reports
- Animated subplots

### 🧪 Practice Ideas

- Student vs subject dashboard বানাও
- Sales vs profit multi-chart বানাও
- Weather dashboard design করো
- Multi-metric comparison system তৈরি করো
