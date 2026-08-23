# 📅 Day 29 — Advanced Customization

---

# 🎯 Objective

- Seaborn + Matplotlib দিয়ে professional-level visualization তৈরি করা
- Titles, labels, legends, ticks customize করা
- Annotation দিয়ে insights highlight করা
- Layout optimization শিখা
- Publication-ready plots তৈরি করা

---

# 📚 Topics Covered

- Titles & subtitles customization
- Axis labels formatting
- Legend control
- Tick customization
- Annotation in plots
- Layout optimization (`tight_layout`)
- Publication-style visualization
- Dashboard-style plotting

---

# 📁 Project Structure

```bash
day-29/
│── 01_basic_title_labels.py
│── 02_legend_control.py
│── 03_tick_customization.py
│── 04_annotation_example.py
│── 05_layout_optimization.py
│── 06_publication_style_plot.py
│── 07_business_dashboard_style.py
│── 08_final_master_plot.py
│── marketing.csv
│── README.md
```

---

# 📊 Dataset

## 📌 File Name: `marketing.csv`

## 📌 Description

এই dataset এ marketing performance data (ads spend, leads, sales) আছে, যা business analytics visualization এবং trend analysis এর জন্য ব্যবহার করা হয়েছে।

---

## 📌 Columns

- `month` → month name
- `ads` → advertising budget
- `leads` → generated leads
- `sales` → total sales

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_title_labels.py

## 🔹 Purpose

- Plot এ title এবং axis labels যোগ করা
- Basic storytelling setup করা

## 🧾 Code

```python
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")

plt.title("Relationship Between Bill and Tip", fontsize=14)
plt.xlabel("Total Bill Amount ($)", fontsize=12)
plt.ylabel("Tip Amount ($)", fontsize=12)
plt.show()
```

## 🧠 Explanation

- `plt.title()` → plot এর main story define করে
- `xlabel` / `ylabel` → axis meaning পরিষ্কার করে
- Seaborn plot + Matplotlib text styling combined

---

# 📄 2. 02_legend_control.py

## 🔹 Purpose

- Legend customize করা
- Category explanation improve করা

## 🧾 Code

```python
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")

plt.legend(title="Gender", loc="upper left")
plt.title("Legend Customization Example")
plt.show()
```

## 🧠 Explanation

- `plt.legend()` → categories explain করে
- `title="Gender"` → legend header
- `loc` → legend position control করে

---

# 📄 3. 03_tick_customization.py

## 🔹 Purpose

- Axis ticks customize করা
- Readability improve করা

## 🧾 Code

```python
sns.boxplot(data=tips, x="day", y="total_bill")

plt.xticks(rotation=45)
plt.yticks([10, 20, 30, 40, 50])
plt.title("Tick Customization Example")
plt.show()
```

## 🧠 Explanation

- `xticks(rotation=45)` → label rotate করে overlap কমায়
- `yticks()` → custom scale define করে
- Better readability + control

---

# 📄 4. 04_annotation_example.py

## 🔹 Purpose

- Plot এ insight highlight করা
- Annotation ব্যবহার শেখা

## 🧾 Code

```python
sns.scatterplot(data=tips, x="total_bill", y="tip")

plt.text(30, 6, "High spending customers", fontsize=10, color="red")
plt.title("Scatter Plot with Annotation")
plt.show()
```

## 🧠 Explanation

- `plt.text()` → plot এর মধ্যে label add করে
- Important pattern highlight করা হয়
- Data storytelling শক্তিশালী হয়

---

# 📄 5. 05_layout_optimization.py

## 🔹 Purpose

- Multiple plots clean layout এ সাজানো
- Overlapping fix করা

## 🧾 Code

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(tips["total_bill"], kde=True, ax=axes[0])
sns.boxplot(data=tips, x="day", y="total_bill", ax=axes[1])

plt.tight_layout()
plt.show()
```

## 🧠 Explanation

- `subplots()` → multiple chart layout তৈরি করে
- `tight_layout()` → spacing fix করে
- Professional dashboard feel তৈরি হয়

---

# 📄 6. 06_publication_style_plot.py

## 🔹 Purpose

- Publication-ready visualization তৈরি করা
- Full styling control শেখা

## 🧾 Code

```python
plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    style="time",
    s=80
)

plt.title("Publication-Style Analysis Plot", fontsize=16)
plt.xlabel("Total Bill ($)", fontsize=12)
plt.ylabel("Tip ($)", fontsize=12)

plt.legend(title="Categories")
plt.grid(True, linestyle="--", alpha=0.5)

plt.show()
```

## 🧠 Explanation

- `hue` + `style` → multiple dimension encoding
- `grid()` → readability increase করে
- Professional report-style output তৈরি হয়

---

# 📄 7. 07_business_dashboard_style.py

## 🔹 Purpose

- Business dashboard visualization তৈরি করা
- Multi-metric comparison করা

## 🧾 Code

```python
df = pd.read_csv("marketing.csv")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.lineplot(data=df, x="month", y="ads", ax=axes[0], marker="o")
sns.lineplot(data=df, x="month", y="sales", ax=axes[1], marker="o")

plt.suptitle("Marketing Performance Dashboard", fontsize=14)
plt.tight_layout()
plt.show()
```

## 🧠 Explanation

- `suptitle()` → global title
- subplot dashboard structure
- business performance comparison সহজ হয়

---

# 📄 8. 08_final_master_plot.py

## 🔹 Purpose

- Final polished visualization তৈরি করা
- Portfolio-ready plot বানানো

## 🧾 Code

```python
plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    style="time",
    s=100
)

plt.title("Final Professional Data Visualization", fontsize=18)
plt.xlabel("Total Bill Amount", fontsize=12)
plt.ylabel("Tip Amount", fontsize=12)

plt.legend(title="Category", loc="best")
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()
```

## 🧠 Explanation

- Final cleaned + styled visualization
- Fully readable + professional output
- Portfolio-ready graph

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Seaborn plot তৈরি করা হয়েছে
- Matplotlib styling যোগ করা হয়েছে
- Titles, labels, legends set করা হয়েছে
- Annotation যোগ করা হয়েছে
- Layout optimize করা হয়েছে
- Final professional visualization তৈরি করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Plot storytelling improve হয় titles + labels দিয়ে
- Legends categories explain করে
- Annotation insights highlight করে
- Layout optimization readability বাড়ায়

---

# 🚀 What I Learned

- Advanced plot customization
- Professional visualization design
- Dashboard-style plotting
- Annotation-based storytelling
- Publication-ready graph creation

---

# 🧠 Key Concepts (Quick Revision)

- `plt.title()` → main story
- `plt.xlabel()/ylabel()` → meaning
- `plt.legend()` → category explanation
- `plt.text()` → annotation
- `tight_layout()` → spacing fix
- `subplots()` → dashboard layout

---

# 📝 Notes

## 📌 Mistakes

- Overcrowded labels readability কমায়
- Annotation wrong position হলে confusion হয়
- Legend overlap হতে পারে without layout fix

## 📌 Optimization Tips

- Always use `tight_layout()`
- Keep font sizes consistent
- Use annotation only for key insights

---

# 📌 Next Day Preview

## 📅 Day 30 — Final Seaborn Master Project

- Full EDA project
- Real dataset analysis
- Dashboard + storytelling
- Portfolio-ready visualization system

---

# ⭐ Bonus

## 🔥 Improvements Ideas

- Full business report visualization
- Multi-dashboard layout design
- Presentation-ready charts

---

## 🧪 Practice Ideas

- 2x2 dashboard তৈরি করো
- Different annotation positions try করো
- Custom legend styling practice করো
