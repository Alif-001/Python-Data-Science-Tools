# 📅 Day 28 — 3D Plotting Introduction

## 🎯 Objective

- আজকে 3D visualization শিখবো (X, Y, Z axis)
- 3D scatter, surface, wireframe plot তৈরি করা শিখবো
- Camera angle control করা শিখবো
- Real-world 3D data visualization বোঝা শিখবো
- Mathematical surface এবং spatial data visualize করা শিখবো

---

## 📚 Topics Covered

- 3D axes setup
- 3D scatter plot
- 3D surface plot
- 3D wireframe plot
- Camera angle control (`view_init`)
- Multi 3D visualization

---

## 📁 Project Structure

```bash
day-28/
│── 01_3d_axes_basics.py
│── 02_3d_scatter_plot.py
│── 03_3d_surface_plot.py
│── 04_3d_wireframe_plot.py
│── 05_camera_angle_control.py
│── 06_multiple_3d_plots.py
│── 07_csv_3d_scatter.py
│── 3d_data.csv
│── README.md
```

---

## 📊 Dataset

### **File Name:** `3d_data.csv`

### **Description:**

- 3D coordinate-based dataset used for scatter visualization in space

### **Columns:**

- `x` → X-axis coordinate
- `y` → Y-axis coordinate
- `z` → Z-axis coordinate (height/depth value)

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `main.py`

### 🔹 Purpose

- 3D plotting concept introduce করা
- X, Y, Z axis idea বোঝানো

### 🧾 Code

```python id="d3d1"
print("Day 28 - 3D Plotting Introduction 🚀")
```

### 🧠 Explanation

- Line 1 → simple intro message print করে
- Line 1 → day topic identify করে
- Logic → 2D থেকে 3D visualization ধারণা শুরু করা

---

## 📄 2. `analysis.py`

### 🔹 Purpose

- 3D dataset structure analyze করা
- coordinate range বুঝতে সাহায্য করা

### 🧾 Code

```python id="d3d2"
def get_range(values):
    return min(values), max(values)
```

### 🧠 Explanation

- Step 1 → values list থেকে minimum বের করে
- Step 2 → maximum বের করে
- Logic → 3D plot scaling বুঝতে সাহায্য করে

---

## 📄 3. `utils.py`

### 🔹 Purpose

- Helper formatting functions রাখা
- reusable logic support করা

### 🧾 Code

```python id="d3d3"
def format_axis(label):
    return label.upper()
```

### 🧠 Explanation

- Axis label clean এবং standard করে
- dashboard / visualization styling help করে

---

## 📄 4. `01_3d_axes_basics.py`

### 🔹 Purpose

- basic 3D plot setup শেখা

### 🧾 Code

- `fig.add_subplot(111, projection='3d')` দিয়ে 3D axis তৈরি করা হয়েছে
- simple x, y, z line plot করা হয়েছে

### 🧠 Explanation

- Step 1 → figure তৈরি করা হয়েছে
- Step 2 → 3D axis enable করা হয়েছে
- Step 3 → x, y, z তিনটা dimension plot করা হয়েছে
- Logic → প্রথমবার 3D space visualization

---

## 📄 5. `02_3d_scatter_plot.py`

### 🔹 Purpose

- 3D scatter plot তৈরি করা

### 🧾 Code

- random x, y, z points generate করা হয়েছে
- `ax.scatter()` দিয়ে 3D points plot করা হয়েছে

### 🧠 Explanation

- Step 1 → random 3D dataset তৈরি
- Step 2 → scatter plot render
- Step 3 → color mapping দিয়ে depth highlight
- Logic → clustering / spatial distribution visualization

---

## 📄 6. `03_3d_surface_plot.py`

### 🔹 Purpose

- mathematical surface visualization

### 🧾 Code

- meshgrid তৈরি করা হয়েছে
- `Z = sin(sqrt(X^2 + Y^2))` surface function ব্যবহার করা হয়েছে

### 🧠 Explanation

- Step 1 → grid তৈরি (X, Y plane)
- Step 2 → Z value compute করা হয়েছে
- Step 3 → surface plot draw
- Logic → terrain / ML loss surface visualization

---

## 📄 7. `04_3d_wireframe_plot.py`

### 🔹 Purpose

- wireframe (grid-based 3D surface) দেখানো

### 🧾 Code

- surface function: `Z = X^2 - Y^2`
- `plot_wireframe()` ব্যবহার করা হয়েছে

### 🧠 Explanation

- Step 1 → grid mesh তৈরি
- Step 2 → mathematical surface তৈরি
- Step 3 → wireframe visualization
- Logic → low-detail surface view

---

## 📄 8. `05_camera_angle_control.py`

### 🔹 Purpose

- 3D plot camera angle control শেখা

### 🧾 Code

- `ax.view_init(elev=30, azim=45)` ব্যবহার করা হয়েছে

### 🧠 Explanation

- Step 1 → 3D surface তৈরি
- Step 2 → elevation + rotation set করা হয়েছে
- Step 3 → different viewing angle পাওয়া যাচ্ছে
- Logic → same data different perspective থেকে দেখা

---

## 📄 9. `06_multiple_3d_plots.py`

### 🔹 Purpose

- একাধিক 3D plot compare করা

### 🧾 Code

- surface plot + wireframe plot side-by-side দেখানো হয়েছে

### 🧠 Explanation

- Step 1 → figure split করা হয়েছে
- Step 2 → left side surface plot
- Step 3 → right side wireframe plot
- Logic → comparison between smooth vs grid surface

---

## 📄 10. `07_csv_3d_scatter.py`

### 🔹 Purpose

- CSV data থেকে 3D scatter plot তৈরি

### 🧾 Code

- CSV থেকে x, y, z read করা হয়েছে
- `ax.scatter()` দিয়ে 3D visualization

### 🧠 Explanation

- Step 1 → CSV file load করা হয়েছে
- Step 2 → 3D coordinate list তৈরি
- Step 3 → scatter plot generate
- Logic → real-world spatial data visualization

---

## ⚙️ Implementation Flow

- 3D plotting concept introduce করা হয়েছে
- axis projection enable করা হয়েছে
- scatter, surface, wireframe শেখা হয়েছে
- camera angle control করা হয়েছে
- multi-plot comparison করা হয়েছে
- CSV based 3D visualization করা হয়েছে

---

## 📈 Output / Result

### **Key findings:**

- 3D plots real-world spatial data বুঝতে সাহায্য করে
- surface plot continuous function show করে
- scatter plot individual points দেখায়
- wireframe simplified structure দেয়
- camera angle change করলে same data different view পাওয়া যায়

---

## 🚀 What I Learned

- Matplotlib 3D plotting system
- scatter vs surface vs wireframe difference
- meshgrid concept
- camera angle control
- real dataset in 3D space

---

## 🧠 Key Concepts (Quick Revision)

- `projection='3d'` → 3D axis enable করে
- `scatter()` → point-based visualization
- `plot_surface()` → smooth surface
- `plot_wireframe()` → grid surface
- `view_init()` → camera angle control
- `meshgrid()` → 2D grid for 3D functions

---

## 📝 Notes

- 3D plots heavy হতে পারে large data-তে
- camera angle visualization বুঝতে important
- surface plot smooth, wireframe lightweight
- axis scaling carefully করতে হয় distortion avoid করতে

---

## 📌 Next Day Preview

- Seaborn advanced visualization
- heatmap deep dive
- pairplot & distribution analysis
- statistical visualization upgrade

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- interactive 3D rotation tool বানানো
- ML loss surface visualization
- terrain generator project
- 3D data clustering visualization

### 🧪 Practice Ideas

- random 3D point cloud বানাও
- sine/cosine 3D surface plot করো
- CSV থেকে 3D stock data visualize করো
- multiple surface compare করো
