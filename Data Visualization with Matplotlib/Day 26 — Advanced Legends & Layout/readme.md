# 📅 Day 26 — Advanced Legends & Layout

## 🎯 Objective

- আজকে Matplotlib legend system deep ভাবে শিখবো
- Custom legend design ও positioning practice করবো
- Multiple legends ব্যবহার করা শিখবো
- Subplot layout control এবং dashboard design শিখবো
- Real-world analytics dashboard তৈরি করা শিখবো

---

## 📚 Topics Covered

- Custom legends
- Legend positioning
- Multiple legends
- Figure layout control
- Complex dashboard layout

---

## 📁 Project Structure

```bash
day-26/
│── 01_custom_legend.py
│── 02_legend_positioning.py
│── 03_multiple_legends.py
│── 04_figure_layout_control.py
│── 05_subplot_layout.py
│── 06_professional_dashboard.py
│── 07_csv_dashboard_plot.py
│── sales_multi_product.csv
│── README.md
```

---

## 📊 Dataset

### 📄 File Name: `sales_multi_product.csv`

- **Description:** Multiple product sales data used for dashboard visualization

### Columns:

- `day` → Day index
- `product_A` → Product A sales
- `product_B` → Product B sales
- `product_C` → Product C sales

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `main.py` (Concept Entry)

### 🔹 Purpose

- legend system বোঝা
- plot labeling concept introduction

### 🧾 Code

```python id="lg1"
print("Day 26 - Advanced Legends & Layout 📊")
```

### 🧠 Explanation

- Legend প্রতিটি plot কে identify করে
- Multiple data compare করার জন্য খুব important

---

## 📄 2. `analysis.py`

### 🔹 Purpose

- plot elements analysis helper

### 🧾 Code

```python id="lg2"
def count_series(data):
    return len(data)
```

### 🧠 Explanation

- dataset কতটি series আছে তা detect করে
- multi-line plotting বুঝতে সাহায্য করে

---

## 📄 3. `utils.py`

### 🔹 Purpose

- legend formatting helper

### 🧾 Code

```python id="lg3"
def format_label(name):
    return name.upper()
```

### 🧠 Explanation

- label formatting clean করে
- dashboard consistency maintain করে

---

## 📄 4. `01_custom_legend.py`

### 🔹 Purpose

- custom legend styling শেখা

### 🧠 Explanation

- `label` দিয়ে series identify করা হয়েছে
- `plt.legend()` customize করা হয়েছে
- position, font size, shadow, title add করা হয়েছে
- professional visualization look তৈরি করা হয়েছে

---

## 📄 5. `02_legend_positioning.py`

### 🔹 Purpose

- legend positioning control করা

### 🧠 Explanation

- legend বিভিন্ন position-এ রাখা যায়
- `loc="lower left"` দিয়ে position control করা হয়েছে
- readability improve করা হয়েছে
- plot overlap avoid করা যায়

---

## 📄 6. `03_multiple_legends.py`

### 🔹 Purpose

- multiple legend system শেখা

### 🧠 Explanation

- আলাদা legend group তৈরি করা হয়েছে
- `add_artist()` ব্যবহার করে multiple legends show করা হয়েছে
- complex visualization structure বোঝানো হয়েছে

---

## 📄 7. `04_figure_layout_control.py`

### 🔹 Purpose

- figure size control শেখা

### 🧠 Explanation

- `figsize=(10,5)` দিয়ে canvas size control করা হয়েছে
- wide chart তৈরি করা হয়েছে
- professional report-style layout তৈরি হয়েছে

---

## 📄 8. `05_subplot_layout.py`

### 🔹 Purpose

- multiple plots এক figure-এ show করা

### 🧠 Explanation

- `subplot(2,2)` দিয়ে 4 charts তৈরি করা হয়েছে
- different mathematical functions show করা হয়েছে
- `tight_layout()` spacing fix করেছে
- dashboard structure তৈরি হয়েছে

---

## 📄 9. `06_professional_dashboard.py`

### 🔹 Purpose

- full dashboard layout তৈরি করা

### 🧠 Explanation

- 4 different charts একসাথে দেখানো হয়েছে
- sin, cos, quadratic, exponential plot করা হয়েছে
- real analytics dashboard style mimic করা হয়েছে
- professional visualization layout তৈরি হয়েছে

---

## 📄 10. `07_csv_dashboard_plot.py`

### 🔹 Purpose

- real CSV dashboard visualization

### 🧠 Explanation

- multiple product sales data load করা হয়েছে
- 3 product line chart একসাথে plot করা হয়েছে
- legend customize করা হয়েছে
- business dashboard style visualization তৈরি হয়েছে

---

## ⚙️ Implementation Flow

- legend system শেখা হয়েছে
- plot labeling করা হয়েছে
- multiple legend handle করা হয়েছে
- figure size control করা হয়েছে
- subplot dashboard তৈরি করা হয়েছে
- real CSV dashboard visualize করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- legend plot readability improve করে
- multiple datasets compare করা সহজ হয়
- subplot dashboard professional insight দেয়
- figure size control layout design improve করে
- real CSV dashboard business analytics show করে

---

## 🚀 What I Learned

- legend customization system
- multiple plot labeling strategy
- subplot dashboard creation
- figure layout control
- real-world dashboard visualization

---

## 🧠 Key Concepts (Quick Revision)

- `plt.legend()` → plot labels show করে
- `loc=` → legend position control করে
- `figsize=` → chart size control করে
- `subplot()` → multiple plots layout
- `add_artist()` → multiple legends support
- dashboard → multiple insights একসাথে show করে

---

## 📝 Notes

- legend overlapping avoid করতে proper position দরকার
- subplot spacing important for readability
- too many legends confusing হতে পারে
- dashboard design clean রাখা উচিত

---

## 📌 Next Day Preview

- Animation basics
- Real-time plotting
- Dynamic visualization
- Moving charts introduction

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- interactive dashboard system
- auto legend generator
- theme-based dashboard styling
- real-time sales dashboard

### 🧪 Practice Ideas

- stock market dashboard বানাও
- multi-city sales compare করো
- interactive subplot layout তৈরি করো
- product performance dashboard বানাও
