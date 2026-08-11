# 📅 Day 8 — Subplots Mastery

## 🎯 Objective

- আজকে Subplots system deeply শিখবো
- Multiple charts এক figure এ কিভাবে organize করা যায় বুঝবো
- Row/column layout design করা শিখবো
- Shared axes concept বুঝবো
- Real dashboard style visualization বানানো শিখবো

---

## 📚 Topics Covered

- plt.subplot()
- plt.subplots()
- Row/column layout
- Shared axes
- Multiple visualization dashboard
- Subplot customization
- Looping through axes

---

## 📁 Project Structure

```bash
day-8/
│── 01_subplot_basic.py
│── 02_subplots_function.py
│── 03_row_column_layout.py
│── 04_shared_axes.py
│── 05_dashboard_layout.py
│── 06_subplot_customization.py
│── 07_loop_through_axes.py
│── 08_real_dashboard.py
│── sales_dashboard.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** sales_dashboard.csv
- **Description:** Business sales and advertisement spending dataset used for dashboard visualization

### Columns:

- month → Month name
- online → Online sales
- offline → Offline sales
- ads → Advertisement spending

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry)

### 🔹 Purpose

- Subplot concept introduction
- Multiple visualization idea বোঝা

### 🧾 Code

```python id="sub_main8"
print("Subplots Mastery Day 8 📊")
```

### 🧠 Explanation

- Subplots = multiple charts in one figure
- Dashboard visualization foundation

---

## 📄 2. analysis.py

### 🔹 Purpose

- Data relationship analysis

### 🧾 Code

```python id="sub_analysis8"
def compare():
    return "Multiple dataset comparison using subplots"
```

### 🧠 Explanation

- Different metrics একসাথে compare করা যায়
- Business insight তৈরি হয়

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper utilities

### 🧾 Code

```python id="sub_utils8"
def clean_label(text):
    return text.title()
```

### 🧠 Explanation

- Labels format clean করে
- Visualization readable করে

---

## 📄 4. 01_subplot_basic.py

### 🔹 Purpose

- Basic subplot usage

### 🧾 Code

```python id="sub1"
plt.subplot(2, 1, 1)
plt.plot(x, y)

plt.subplot(2, 1, 2)
plt.plot(y, x)
```

### 🧠 Explanation

- 2 rows, 1 column layout
- Multiple graphs in single figure

---

## 📄 5. 02_subplots_function.py

### 🔹 Purpose

- Modern subplot system

### 🧾 Code

```python id="sub2"
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(x, y)
```

### 🧠 Explanation

- Clean object-based approach
- Each axis separately control করা যায়

---

## 📄 6. 03_row_column_layout.py

### 🔹 Purpose

- Row-wise layout system

### 🧾 Code

```python id="sub3"
fig, ax = plt.subplots(3, 1)
ax[0].plot(x, y)
```

### 🧠 Explanation

- Vertical layout তৈরি হয়
- Sequential comparison সহজ হয়

---

## 📄 7. 04_shared_axes.py

### 🔹 Purpose

- Shared axis concept

### 🧾 Code

```python id="sub4"
fig, ax = plt.subplots(2, 1, sharex=True)
```

### 🧠 Explanation

- Same scale comparison
- Data consistency maintain হয়

---

## 📄 8. 05_dashboard_layout.py

### 🔹 Purpose

- Multi-type dashboard

### 🧾 Code

```python id="sub5"
ax[0, 0].plot(x, y)
ax[0, 1].bar(x, y)
ax[1, 0].scatter(x, y)
ax[1, 1].hist(y)
```

### 🧠 Explanation

- Line, bar, scatter, histogram একসাথে
- BI dashboard style visualization

---

## 📄 9. 06_subplot_customization.py

### 🔹 Purpose

- Styling subplots

### 🧾 Code

```python id="sub6"
ax[0].plot(x, y, marker="o")
ax[1].bar(x, y)
```

### 🧠 Explanation

- Each subplot আলাদা style পায়
- Better readability

---

## 📄 10. 07_loop_through_axes.py

### 🔹 Purpose

- Dynamic subplot generation

### 🧾 Code

```python id="sub7"
for row in ax:
    for col in row:
        col.plot(x, data[i])
```

### 🧠 Explanation

- Loop ব্যবহার করে multiple charts generate
- Scalable visualization system

---

## 📄 11. 08_real_dashboard.py

### 🔹 Purpose

- Real business dashboard

### 🧾 Code

```python id="sub8"
fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(months, online)
ax[0, 1].plot(months, offline)
ax[1, 0].bar(months, ads)
ax[1, 1].plot(months, online)
ax[1, 1].plot(months, offline)
```

### 🧠 Explanation

- Sales + ads analysis
- Real business intelligence dashboard

---

## ⚙️ Implementation Flow

- Subplot concept শেখা হয়েছে
- Row/column layout বোঝা হয়েছে
- Multiple chart system তৈরি করা হয়েছে
- Shared axis ব্যবহার করা হয়েছে
- Loop-based subplot automation শেখা হয়েছে
- Real dashboard visualization বানানো হয়েছে

---

## 📈 Output / Result

### Key findings:

- Subplots = multiple visualization system
- Dashboard analysis possible
- Shared axes improve comparison
- Looping makes scalable plotting
- Business data analysis easier

---

## 🚀 What I Learned

- Subplot vs subplots difference
- Grid layout system
- Shared axes concept
- Dashboard design thinking
- Automated plotting using loops

---

## 🧠 Key Concepts (Quick Revision)

- `subplot()` → manual layout
- `subplots()` → modern approach
- `sharex/sharey` → same scale
- `tight_layout()` → spacing fix
- `axes object` → individual control
- `loop axes` → scalable design

---

## 📝 Notes

- Large dashboard এ `subplots()` best
- Shared axis comparison improve clarity
- Looping reduces repeated code
- Layout planning important for readability

---

## 📌 Next Day Preview

- Styling & Themes
- Advanced visualization aesthetics
- Text & annotation system
- Professional chart design
- Axis customization techniques

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Interactive dashboard (Plotly style)
- Real-time data dashboard
- Auto report generation
- Multi-page analytics system

### 🧪 Practice Ideas

- Sales vs profit dashboard বানাও
- Student performance comparison dashboard
- Weather analytics dashboard
- Stock market mini dashboard তৈরি করো
