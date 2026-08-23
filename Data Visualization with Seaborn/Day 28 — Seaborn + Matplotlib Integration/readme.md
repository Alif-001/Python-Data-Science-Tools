# � Day 28 — Seaborn + Matplotlib Integration

---

# 🎯 Objective

- Seaborn এর সাথে Matplotlib একসাথে ব্যবহার করা শেখা
- Custom styling, figure size, labels, ticks, annotation control করা
- Professional-quality plot তৈরি করা
- Dashboard-style multi-plot visualization বোঝা

---

# 📚 Topics Covered

- Seaborn + Matplotlib integration
- Custom figure size
- Subplots
- Annotation
- Style control
- Axis labels and ticks
- Dashboard-style plotting
- Publication-quality visualization

---

# 📁 Project Structure

```bash
day-28/
│── 01_basic_integration.py
│── 02_custom_figsize.py
│── 03_subplot_integration.py
│── 04_advanced_annotation.py
│── 05_custom_style_control.py
│── 06_custom_ticks_and_labels.py
│── 07_real_world_dashboard_style.py
│── 08_professional_final_plot.py
│── performance.csv
│── README.md
```

---

# 📊 Dataset

## 📌 File Name: `performance.csv`

## 📌 Description

এই dataset এ team-wise sales এবং profit data দেওয়া আছে, যা business-style visualization এবং dashboard design শেখার জন্য ব্যবহার করা হয়েছে।

---

## 📌 Columns

- `team` → team name
- `month` → month name
- `sales` → sales amount
- `profit` → profit amount

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_integration.py

## 🔹 Purpose

- Seaborn plot এর উপর Matplotlib customization apply করা
- Basic integration বোঝা

## 🧾 Code

```python
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")

plt.title("Seaborn + Matplotlib Integration")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()
```

## 🧠 Explanation

- `sns.scatterplot()` → মূল plot তৈরি করে
- `plt.title()` → title সেট করে
- `plt.xlabel()` / `plt.ylabel()` → axis label customize করে
- Seaborn plotting + Matplotlib styling together কাজ করছে

---

# 📄 2. 02_custom_figsize.py

## 🔹 Purpose

- Figure size control করা
- Plot canvas এর dimension modify করা

## 🧾 Code

```python
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Custom Figure Size Boxplot")
plt.show()
```

## 🧠 Explanation

- `plt.figure(figsize=(10, 6))` → plot size নির্ধারণ করে
- বড় figure হলে plot readability বাড়ে
- Presentation-ready plot তৈরি হয়

---

# 📄 3. 03_subplot_integration.py

## 🔹 Purpose

- এক figure এ multiple plots রাখা
- Subplot layout শেখা

## 🧾 Code

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.scatterplot(data=tips, x="total_bill", y="tip", ax=axes[0])
axes[0].set_title("Scatter Plot")

sns.histplot(data=tips, x="total_bill", kde=True, ax=axes[1])
axes[1].set_title("Distribution")

plt.tight_layout()
plt.show()
```

## 🧠 Explanation

- `plt.subplots()` → multiple axes তৈরি করে
- `ax=axes[0]` এবং `ax=axes[1]` → নির্দিষ্ট subplot এ plot বসায়
- Multiple insight একসাথে দেখা যায়

---

# 📄 4. 04_advanced_annotation.py

## 🔹 Purpose

- Plot এ annotation যোগ করা
- গুরুত্বপূর্ণ region highlight করা

## 🧾 Code

```python
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.text(30, 6, "High Bill High Tip Zone", fontsize=10, color="red")
plt.title("Scatter with Annotation")
plt.show()
```

## 🧠 Explanation

- `plt.text()` → plot এ লেখা যোগ করে
- Important area highlight করা যায়
- Storytelling আরও strong হয়

---

# 📄 5. 05_custom_style_control.py

## 🔹 Purpose

- Matplotlib style ব্যবহার করা
- Plot theme change করা

## 🧾 Code

```python
plt.style.use("ggplot")
sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Styled Plot (ggplot style)")
plt.show()
```

## 🧠 Explanation

- `plt.style.use()` → overall style বদলায়
- পুরো plot এর look পরিবর্তন হয়
- Consistent visual theme পাওয়া যায়

---

# 📄 6. 06_custom_ticks_and_labels.py

## 🔹 Purpose

- Axis ticks এবং labels fine-tune করা
- Plot readability improve করা

## 🧾 Code

```python
sns.boxplot(data=tips, x="day", y="total_bill")

plt.xticks(rotation=45)
plt.yticks([10, 20, 30, 40])
plt.xlabel("Days of Week")
plt.ylabel("Total Bill ($)")
plt.title("Custom Axis Control")
plt.show()
```

## 🧠 Explanation

- `plt.xticks(rotation=45)` → x-axis label ঘুরিয়ে দেয়
- `plt.yticks()` → custom tick values দেয়
- Labels আরও clear হয়

---

# 📄 7. 07_real_world_dashboard_style.py

## 🔹 Purpose

- Dashboard-style business plot তৈরি করা
- Sales এবং profit compare করা

## 🧾 Code

```python
df = pd.read_csv("performance.csv")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.barplot(data=df, x="team", y="sales", ax=axes[0])
axes[0].set_title("Team Sales")

sns.barplot(data=df, x="team", y="profit", ax=axes[1])
axes[1].set_title("Team Profit")

plt.tight_layout()
plt.show()
```

## 🧠 Explanation

- এক figure এ দুইটা business metric দেখানো হয়েছে
- Dashboard style analysis করা হয়েছে
- Compare করা সহজ হয়

---

# 📄 8. 08_professional_final_plot.py

## 🔹 Purpose

- Professional-quality plot তৈরি করা
- Final polished visualization বোঝা

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

plt.title("Professional Seaborn + Matplotlib Plot")
plt.xlabel("Total Bill")
plt.ylabel("Tip Amount")
plt.grid(True)
plt.show()
```

## 🧠 Explanation

- `hue` → category-based color
- `style` → shape-based distinction
- `s=80` → point size control
- `plt.grid(True)` → readability improve করে

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Seaborn plot তৈরি করা হয়েছে
- Matplotlib দিয়ে styling করা হয়েছে
- Figure size customize করা হয়েছে
- Subplots ব্যবহার করা হয়েছে
- Annotation এবং axis control যোগ করা হয়েছে
- Final professional plot তৈরি করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Seaborn plotting দ্রুত এবং সহজ
- Matplotlib customization খুব powerful
- Subplots দিয়ে dashboard বানানো যায়
- Annotation plot storytelling improve করে

---

# 🚀 What I Learned

- Seaborn + Matplotlib integration
- Figure and axis control
- Subplot layout
- Annotation usage
- Professional visualization design

---

# 🧠 Key Concepts (Quick Revision)

- Seaborn → statistical plotting
- Matplotlib → fine-grained control
- `plt.figure()` → canvas size
- `plt.subplots()` → multi-plot layout
- `plt.text()` → annotation
- `plt.style.use()` → style control

---

# 📝 Notes

## 📌 Mistakes

- Subplot এ `ax=` না দিলে ভুল axis এ plot যেতে পারে
- Figure size ছোট হলে plot crowded দেখায়
- Annotation position ভুল হলে text overlap হতে পারে

## 📌 Optimization Tips

- Always use `tight_layout()`
- Readability বাড়াতে consistent style ব্যবহার করো
- Dashboard বানাতে subplot use করো

---

# 📌 Next Day Preview

## 📅 Day 29 — Advanced Customization

- Titles
- Labels
- Legends
- Tick customization
- Layout optimization
- Publication-style plotting

---

# ⭐ Bonus

## 🔥 Improvements Ideas

- Full business dashboard তৈরি করা
- Multiple metrics এক figure এ দেখানো
- Presentation-ready report বানানো

---

## 🧪 Practice Ideas

- Different `plt.style.use()` try করো
- 2x2 subplot dashboard বানাও
- Annotation দিয়ে insight highlight করো
