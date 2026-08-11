# 📅 Day 17 — Colormaps

---

## 🎯 Objective

- আজকে Matplotlib-এর colormap system শিখবো
- Sequential, diverging, qualitative colormap বুঝবো
- Custom colormap তৈরি করা শিখবো
- Data visualization-এ color meaning কীভাবে কাজ করে বুঝবো
- Real dataset দিয়ে heatmap analysis করা শিখবো

---

## 📚 Topics Covered

- Colormap understanding
- Sequential colormap
- Diverging colormap
- Qualitative colormap
- Custom colormap
- Color normalization

---

## 📁 Project Structure

```bash
day-17/
│── 01_colormap_basics.py
│── 02_sequential_colormap.py
│── 03_diverging_colormap.py
│── 04_qualitative_colormap.py
│── 05_custom_colormap.py
│── 06_color_normalization.py
│── 07_real_colormap_analysis.py
│── city_temperature.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** city_temperature.csv
- **Description:** বিভিন্ন শহরের মাসভিত্তিক temperature data, colormap দিয়ে pattern visualization করার জন্য ব্যবহৃত

### Columns:

- city → শহরের নাম
- jan → January temperature
- feb → February temperature
- mar → March temperature
- apr → April temperature
- may → May temperature
- jun → June temperature

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. 01_colormap_basics.py

### 🔹 Purpose

- Colormap কী এবং কীভাবে কাজ করে তা বোঝা
- Basic heatmap visualization শেখা

### 🧾 Code

```python
plt.imshow(data, cmap="viridis")
```

### 🧠 Explanation

- `imshow()` matrix data show করে
- `cmap="viridis"` color gradient apply করে
- low → high value color change করে represent করে

---

## 📄 2. 02_sequential_colormap.py

### 🔹 Purpose

- Sequential data visualization শেখা

### 🧾 Code

```python
plt.imshow(data, cmap="Blues")
```

### 🧠 Explanation

- Light → Dark color = low → high value
- Sales, marks, temperature type data-তে best use

---

## 📄 3. 03_diverging_colormap.py

### 🔹 Purpose

- Positive ও negative value visualization

### 🧾 Code

```python
plt.imshow(data, cmap="coolwarm")
```

### 🧠 Explanation

- Middle point (0) কে center ধরে color split হয়
- positive = warm color
- negative = cool color

---

## 📄 4. 04_qualitative_colormap.py

### 🔹 Purpose

- Category-based visualization শেখা

### 🧾 Code

```python
plt.imshow(data, cmap="Set3")
```

### 🧠 Explanation

- Different category = different color
- Numbers meaning না, group represent করে

---

## 📄 5. 05_custom_colormap.py

### 🔹 Purpose

- নিজের custom colormap তৈরি করা

### 🧾 Code

```python
LinearSegmentedColormap.from_list(
    "custom",
    ["green", "yellow", "red"]
)
```

### 🧠 Explanation

- green → low value
- yellow → medium value
- red → high value
- fully custom design system

---

## 📄 6. 06_color_normalization.py

### 🔹 Purpose

- Color scaling problem বোঝা

### 🧾 Code

```python
plt.imshow(data, cmap="viridis")
```

### 🧠 Explanation

- large range data থাকলে color imbalance হতে পারে
- normalization না করলে interpretation ভুল হতে পারে

---

## 📄 7. 07_real_colormap_analysis.py

### 🔹 Purpose

- Real dataset দিয়ে heatmap analysis

### 🧾 Code

```python
plt.imshow(data, cmap="coolwarm")
```

### 🧠 Explanation

- city vs month temperature matrix তৈরি করা হয়েছে
- pattern easily visualize করা যায়
- hot/cold region identify করা যায়

---

## ⚙️ Implementation Flow

- Matrix data তৈরি করা হয়েছে
- Different colormap apply করা হয়েছে
- Sequential vs diverging vs qualitative difference দেখা হয়েছে
- Custom colormap তৈরি করা হয়েছে
- Real temperature dataset heatmap বানানো হয়েছে

---

## 📈 Output / Result

### Key findings:

- Colormap data meaning visually show করে
- Sequential colormap trend বুঝতে সাহায্য করে
- Diverging colormap comparison সহজ করে
- Custom colormap branding-level visualization দেয়
- Heatmap pattern analysis powerful insight দেয়

---

## 🚀 What I Learned

- Colormap কীভাবে কাজ করে
- Different colormap types
- Data type অনুযায়ী color choose করা
- Custom colormap design
- Real-world heatmap analysis

---

## 🧠 Key Concepts (Quick Revision)

- `cmap` → color style
- `viridis` → default professional colormap
- `Blues` → sequential colormap
- `coolwarm` → diverging colormap
- `Set3` → categorical colormap
- `imshow()` → matrix visualization

---

## 📝 Notes

- Wrong colormap selection misleading result দিতে পারে
- Business chart-এ clean colormap best
- Over colorful chart avoid করা উচিত
- Data type অনুযায়ী colormap select করা গুরুত্বপূর্ণ

---

## 📌 Next Day Preview

- Image Visualization
- imshow deep usage
- RGB & grayscale image plotting
- Real image processing with Matplotlib

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Auto-colormap selector system
- Interactive heatmap dashboard
- Temperature analytics report generator
- Business KPI heatmap system

### 🧪 Practice Ideas

- Country-wise temperature heatmap বানাও
- Exam marks heatmap visualize করো
- Sales performance heatmap তৈরি করো
- Custom brand colormap design করো
