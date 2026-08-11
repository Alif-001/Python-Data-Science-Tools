# 📅 Day 19 — Contour Plot

---

## 🎯 Objective

- আজকে Contour Plot শিখবো
- 2D mathematical function visualize করা শিখবো
- Filled contour এবং contour line difference বুঝবো
- Scientific data (temperature/heat map) visualize করা শিখবো
- Real dataset দিয়ে contour analysis করা শিখবো

---

## 📚 Topics Covered

- Contour plot basics
- Filled contour
- 2D function visualization
- Scientific data visualization

---

## 📁 Project Structure

```bash
day-19/
│── 01_contour_plot_basics.py
│── 02_filled_contour.py
│── 03_contour_levels.py
│── 04_2d_function_visualization.py
│── 05_scientific_data_contour.py
│── 06_contour_vs_filled_contour.py
│── 07_real_data_contour.py
│── temperature_grid.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** temperature_grid.csv
- **Description:** 2D grid temperature data, contour map visualization এর জন্য ব্যবহৃত

### Columns:

- row0 → প্রথম row temperature values
- row1 → second row values
- row2 → third row values
- row3 → fourth row values
- row4 → fifth row values

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. 01_contour_plot_basics.py

### 🔹 Purpose

- Basic contour plot ধারণা বোঝা

### 🧾 Code

```python
plt.contour(X, Y, Z)
```

### 🧠 Explanation

- একই value যুক্ত points connect করে line তৈরি করে
- পাহাড়/height map এর মতো visual representation দেয়
- `Z = x² + y²` একটি bowl shape তৈরি করে

---

## 📄 2. 02_filled_contour.py

### 🔹 Purpose

- Color-filled contour visualization

### 🧾 Code

```python
plt.contourf(X, Y, Z, cmap="viridis")
```

### 🧠 Explanation

- contour line এর মধ্যে color fill করে
- smooth heatmap-like visualization তৈরি হয়
- data intensity easily বোঝা যায়

---

## 📄 3. 03_contour_levels.py

### 🔹 Purpose

- Contour level control করা

### 🧾 Code

```python
plt.contour(X, Y, Z, levels=20)
```

### 🧠 Explanation

- `levels` = কতগুলো contour line হবে
- বেশি levels = detailed map
- কম levels = simple map

---

## 📄 4. 04_2d_function_visualization.py

### 🔹 Purpose

- Mathematical function visualize করা

### 🧾 Code

```python
Z = np.sin(X) * np.cos(Y)
```

### 🧠 Explanation

- wave pattern তৈরি হয়
- 2D function visualization সহজ হয়
- physics/math simulation এ ব্যবহার হয়

---

## 📄 5. 05_scientific_data_contour.py

### 🔹 Purpose

- Scientific heat distribution visualization

### 🧾 Code

```python
Z = np.exp(-(X**2 + Y**2) / 20)
```

### 🧠 Explanation

- center heat source তৈরি করে
- temperature spread visualize করে
- physics simulation style output

---

## 📄 6. 06_contour_vs_filled_contour.py

### 🔹 Purpose

- contour vs filled contour comparison

### 🧾 Code

```python
plt.contour(X, Y, Z)
plt.contourf(X, Y, Z)
```

### 🧠 Explanation

- contour = lines only
- contourf = filled color regions
- filled version বেশি readable

---

## 📄 7. 07_real_data_contour.py

### 🔹 Purpose

- Real temperature grid visualization

### 🧾 Code

```python
plt.contourf(X, Y, Z, cmap="coolwarm")
```

### 🧠 Explanation

- CSV data → 2D matrix
- heatmap style contour map তৈরি
- real-world weather pattern analysis

---

## ⚙️ Implementation Flow

- X, Y grid তৈরি করা হয়েছে
- mathematical function ব্যবহার করা হয়েছে
- contour line draw করা হয়েছে
- filled contour visualization করা হয়েছে
- real CSV temperature data visualize করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Contour plot = 3D data কে 2D visualize করে
- Filled contour বেশি readable
- Scientific simulation সহজ হয়
- Heat distribution pattern বোঝা যায়
- Real grid data analysis করা যায়

---

## 🚀 What I Learned

- Contour plot concept
- 2D function visualization
- Filled vs line contour difference
- Scientific heatmap idea
- Real dataset contour mapping

---

## 🧠 Key Concepts (Quick Revision)

- `contour()` → line-based map
- `contourf()` → filled color map
- `meshgrid()` → X,Y grid তৈরি করে
- `levels` → detail control
- `Z = function(X,Y)` → surface model

---

## 📝 Notes

- Too many levels = confusing visualization
- contourf বেশি practical for analysis
- meshgrid না হলে contour কাজ করে না
- scientific visualization এ খুব গুরুত্বপূর্ণ

---

## 📌 Next Day Preview

- Polar Plot
- Circular data visualization
- Radar-style charts
- Angle-based plotting system

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Weather heatmap system
- Terrain elevation map
- Physics simulation visualization
- Interactive contour explorer

### 🧪 Practice Ideas

- mountain height map বানাও
- temperature field simulation করো
- wave function visualize করো
- custom heat source model তৈরি করো
