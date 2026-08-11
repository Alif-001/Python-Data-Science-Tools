# 📅 Day 11 — Axis Customization

## 🎯 Objective

- আজকে Matplotlib-এর axis control system শিখবো
- Graph-এর view range customize করা শিখবো
- Tick labels format ও rotate করা শিখবো
- Log scale ও scientific notation ব্যবহার শিখবো
- Dual axis plot তৈরি করা শিখবো
- Real dataset দিয়ে professional axis customization শিখবো

---

## 📚 Topics Covered

- Axis limits (`xlim()`, `ylim()`)
- Tick formatting
- Tick rotation
- Log scale
- Scientific notation
- Dual axis plot
- Real-world axis customization

---

## 📁 Project Structure

```bash
day-11/
│── 01_axis_limits.py
│── 02_tick_formatting.py
│── 03_tick_rotation.py
│── 04_log_scale.py
│── 05_scientific_notation.py
│── 06_dual_axis_plot.py
│── 07_real_axis_customization.py
│── company_metrics.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** company_metrics.csv
- **Description:** Company monthly revenue and user growth data used for axis customization practice

### Columns:

- month → Business month
- revenue → Monthly revenue
- users → Active users

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry)

### 🔹 Purpose

- Axis customization concept বোঝা
- Graph view control idea শেখা

### 🧾 Code

```python
print("Day 11 - Axis Customization 📊")
```

### 🧠 Explanation

- Axis control = data visualization precision control
- Proper axis = better readability

---

## 📄 2. analysis.py

### 🔹 Purpose

- Data scaling analysis

### 🧾 Code

```python
def analyze_range(data):
    return min(data), max(data)
```

### 🧠 Explanation

- Data range বুঝতে সাহায্য করে
- Axis limit সেট করতে useful

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper functions for formatting

### 🧾 Code

```python
def format_label(label):
    return str(label).upper()
```

### 🧠 Explanation

- Labels clean এবং consistent করে
- Reusable utility function

---

## 📄 4. 01_axis_limits.py

### 🔹 Purpose

- Graph view range control করা

### 🧾 Code

```python
plt.xlim(1, 5)
plt.ylim(0, 60)
```

### 🧠 Explanation

- `xlim()` → X-axis range control করে
- `ylim()` → Y-axis range control করে
- Data zoom in/out করা যায়

---

## 📄 5. 02_tick_formatting.py

### 🔹 Purpose

- Tick label customize করা

### 🧾 Code

```python
plt.xticks([1, 2, 3, 4, 5], ["A", "B", "C", "D", "E"])
```

### 🧠 Explanation

- Numbers এর বদলে custom labels show করে
- Readability improve হয়

---

## 📄 6. 03_tick_rotation.py

### 🔹 Purpose

- Overlapping labels fix করা

### 🧾 Code

```python
plt.xticks(rotation=45)
```

### 🧠 Explanation

- Long labels rotate করে readable করা হয়
- Dashboard-style charts clean থাকে

---

## 📄 7. 04_log_scale.py

### 🔹 Purpose

- Large range data visualize করা

### 🧾 Code

```python
plt.yscale("log")
```

### 🧠 Explanation

- Exponential data compress করে দেখায়
- Financial / growth data analysis-এ useful

---

## 📄 8. 05_scientific_notation.py

### 🔹 Purpose

- Large numbers readable format-এ দেখানো

### 🧾 Code

```python
plt.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))
```

### 🧠 Explanation

- Scientific notation automatically apply হয়
- Large dataset cleaner দেখায়

---

## 📄 9. 06_dual_axis_plot.py

### 🔹 Purpose

- দুইটা different metric একই graph-এ দেখানো

### 🧾 Code

```python
ax1 = plt.subplots()[1]
ax2 = ax1.twinx()
```

### 🧠 Explanation

- Temperature এবং humidity একসাথে plot করা হয়েছে
- Different units এক graph-এ compare করা যায়

---

## 📄 10. 07_real_axis_customization.py

### 🔹 Purpose

- Real business dataset visualization

### 🧾 Code

```python
plt.plot(months, revenue, marker="o")
plt.xticks(rotation=45)
plt.ylim(0, 9000)
```

### 🧠 Explanation

- Monthly revenue trend analysis
- Labels rotate করে readability improve করা হয়েছে
- Axis limit + scientific notation applied

---

## ⚙️ Implementation Flow

- Axis range control করা হয়েছে
- Tick labels customize করা হয়েছে
- Tick rotation ব্যবহার করা হয়েছে
- Log scale applied করা হয়েছে
- Scientific notation enabled করা হয়েছে
- Dual axis plot তৈরি করা হয়েছে
- Real dataset visualization করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Axis control improves clarity
- Tick formatting improves readability
- Log scale handles big data effectively
- Dual axis helps compare different metrics
- Real dataset shows business insights clearly

---

## 🚀 What I Learned

- Axis range control (`xlim`, `ylim`)
- Tick customization techniques
- Log scale usage
- Scientific notation concept
- Dual axis plotting

---

## 🧠 Key Concepts (Quick Revision)

- `xlim()` → X-axis limit
- `ylim()` → Y-axis limit
- `xticks()` → label customization
- `rotation` → label angle
- `yscale("log")` → log scale
- `ticklabel_format()` → scientific notation
- `twinx()` → dual axis

---

## 📝 Notes

- Over zoom করলে data misleading হতে পারে
- Log scale carefully use করতে হয়
- Dual axis avoid করা উচিত যদি confusing হয়
- Label readability খুব important

---

## 📌 Next Day Preview

- Box Plot
- Quartile analysis
- Outlier detection
- Distribution comparison
- Statistical visualization

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Auto axis scaling system
- Smart tick generator
- Interactive dual-axis dashboard
- Business KPI visualization tool

### 🧪 Practice Ideas

- Stock price vs volume dual axis chart
- Sales trend with log scale
- User growth analysis dashboard
- Multi-metric comparison chart
