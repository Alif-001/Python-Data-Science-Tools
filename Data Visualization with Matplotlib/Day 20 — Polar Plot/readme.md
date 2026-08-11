# 📅 Day 20 — Polar Plot

---

## 🎯 Objective

- আজকে Polar Plot শিখবো
- Angle (θ) এবং Radius (r) দিয়ে data visualize করা শিখবো
- Circular / radar style chart বানানো শিখবো
- Directional data (wind, movement) visualize করা শিখবো
- Real dataset (CSV) দিয়ে polar plot তৈরি করা শিখবো

---

## 📚 Topics Covered

- Polar coordinates
- Circular visualization
- Angle-based plotting
- Radar-style visualization

---

## 📁 Project Structure

```bash id="p1r8kq"
day-20/
│── 01_polar_plot_basics.py
│── 02_circular_wave_plot.py
│── 03_multi_line_polar.py
│── 04_radar_style_plot.py
│── 05_polar_scatter.py
│── 06_directional_data.py
│── 07_csv_polar_plot.py
│── polar_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** polar_data.csv
- **Description:** Angle-based circular data visualization dataset

### Columns:

- angle → ডিগ্রি (0–360°)
- value → সেই angle-এর measurement/value

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. 01_polar_plot_basics.py

### 🔹 Purpose

- Polar coordinate system বোঝা

### 🧾 Code

```python id="1x8m2p"
plt.subplot(111, projection='polar')
plt.plot(theta, r)
```

### 🧠 Explanation

- X-Y না, এখানে angle + radius ব্যবহার করা হয়
- center থেকে distance অনুযায়ী plot তৈরি হয়
- circular pattern visualize করে

---

## 📄 2. 02_circular_wave_plot.py

### 🔹 Purpose

- Wave pattern in circular form

### 🧾 Code

```python id="k9q2zv"
r = 3 + np.sin(5 * theta)
```

### 🧠 Explanation

- sine wave circular shape তৈরি করে
- repeating pattern দেখা যায়
- signal-like behavior visualize হয়

---

## 📄 3. 03_multi_line_polar.py

### 🔹 Purpose

- Multiple signals compare করা

### 🧾 Code

```python id="m3v8qp"
plt.plot(theta, r1)
plt.plot(theta, r2)
```

### 🧠 Explanation

- একাধিক circular data compare করা যায়
- signal analysis / pattern comparison

---

## 📄 4. 04_radar_style_plot.py

### 🔹 Purpose

- Radar chart তৈরি করা

### 🧾 Code

```python id="r8q1pl"
plt.fill(angles, values, alpha=0.3)
```

### 🧠 Explanation

- skill / performance comparison chart
- circular axis-based evaluation
- business + analytics use case

---

## 📄 5. 05_polar_scatter.py

### 🔹 Purpose

- Polar coordinate scatter plot

### 🧾 Code

```python id="t6w9xk"
plt.scatter(theta, r)
```

### 🧠 Explanation

- random points circular space-এ plot হয়
- distribution analysis সহজ হয়

---

## 📄 6. 06_directional_data.py

### 🔹 Purpose

- Direction-based data visualization

### 🧾 Code

```python id="d4k8zp"
plt.bar(directions, speed)
```

### 🧠 Explanation

- wind direction / movement direction show করে
- angle-based real-world data analysis

---

## 📄 7. 07_csv_polar_plot.py

### 🔹 Purpose

- Real dataset থেকে polar plot তৈরি

### 🧾 Code

```python id="c7p9m2"
angles.append(np.deg2rad(float(row["angle"])))
```

### 🧠 Explanation

- degree → radian conversion করা হয়
- CSV data circular graph-এ convert হয়
- real-world directional analysis

---

## ⚙️ Implementation Flow

- angle + radius data তৈরি করা হয়েছে
- sine wave pattern visualize করা হয়েছে
- multiple signals compare করা হয়েছে
- radar chart তৈরি করা হয়েছে
- directional wind data plot করা হয়েছে
- CSV dataset থেকে polar chart বানানো হয়েছে

---

## 📈 Output / Result

### Key findings:

- Polar plot circular data visualize করে
- Angle-based analysis খুব powerful
- Radar chart comparison সহজ করে
- Directional data real-world use case
- Signal pattern analysis সম্ভব

---

## 🚀 What I Learned

- Polar coordinate system
- Angle vs radius concept
- Radar chart design
- Circular wave patterns
- Real directional data visualization

---

## 🧠 Key Concepts (Quick Revision)

- `projection='polar'` → circular plot
- `theta` → angle (radian)
- `r` → radius (distance)
- radar chart → multi-attribute comparison
- bar polar → directional data

---

## 📝 Notes

- Degree → radian conversion important
- radar chart must be closed loop
- polar plot scientific analysis এ বেশি use হয়
- wind/signal data visualization খুব common

---

## 📌 Next Day Preview

- Stem Plot
- Step Plot
- Event-based visualization
- Discrete signal analysis

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Weather wind direction dashboard
- Radar skill comparison system
- Circular signal analyzer
- Interactive polar visualization tool

### 🧪 Practice Ideas

- student skill radar chart বানাও
- wind direction simulation করো
- circular sine wave experiment করো
- multi-signal comparison system তৈরি করো
