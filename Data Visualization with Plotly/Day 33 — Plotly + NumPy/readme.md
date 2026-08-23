# 📅 Day 33 — Plotly + NumPy

---

## 🎯 Objective

- আজকে আমরা শিখবো কিভাবে **NumPy দিয়ে mathematical + simulated data তৈরি করে Plotly দিয়ে visualize করা যায়**
- Real-world data কিভাবে generate করা হয় (trend + noise + randomness)
- Scientific + financial simulation বুঝা
- Data science / ML-ready synthetic data তৈরি করা

---

## 📚 Topics Covered

- NumPy mathematical plotting
- Sine / Cosine function visualization
- Random walk simulation (stock-like model)
- Trend + noise data generation
- Scientific data visualization with Plotly

---

## 📁 Project Structure

```text id="p33s13"
Day 33 — Plotly + NumPy/
│── 1_math_plotting.py
│── 2_random_simulation.py
│── 3_numpy_trends.py
│── simulation_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** simulation_data.csv
- **Description:** Simple time-series simulation dataset (temperature, humidity)

### Columns:

- time → সময় (1–10)
- temperature → তাপমাত্রা
- humidity → আর্দ্রতা

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. math_plotting.py

### 🔹 Purpose

- Mathematical functions (sin, cos) visualize করা
- NumPy array ব্যবহার করে function plot করা

### 🧾 Code

```python id="math33a"
import numpy as np
import plotly.graph_objects as go

x = np.linspace(0, 10, 100)

y_sin = np.sin(x)
y_cos = np.cos(x)
```

### 🧠 Explanation

- np.linspace → 0 থেকে 10 পর্যন্ত smooth data তৈরি করে
- sin(x) → wave pattern তৈরি করে
- cos(x) → shifted wave pattern
- Overall → mathematical functions visualization

---

## 📄 2. random_simulation.py

### 🔹 Purpose

- Random walk simulation (stock market model)
- Price movement simulation

### 🧾 Code

```python id="rand33b"
price += np.random.randint(-2, 3)
```

### 🧠 Explanation

- Random change generate করে price update করা হয়
- Stock price যেমন ওঠা-নামা করে, সেটার simulation
- Time series behavior তৈরি করা হয়

---

## 📄 3. numpy_trends.py

### 🔹 Purpose

- Real-world data pattern (trend + noise) তৈরি করা
- Forecasting concept বোঝা

### 🧾 Code

```python id="trend33c"
trend = 2 * t
noise = np.random.normal(0, 2, 100)
data = trend + noise
```

### 🧠 Explanation

- trend → steady increase দেখায়
- noise → real-world randomness add করে
- data → final realistic dataset তৈরি হয়

---

## ⚙️ Implementation Flow

- NumPy দিয়ে data generate করা হয়েছে
- Mathematical functions তৈরি করা হয়েছে
- Random simulation চালানো হয়েছে
- Trend + noise combine করা হয়েছে
- Plotly দিয়ে visualization করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- Sin/cos wave pattern দেখা যায়
- Stock-like random movement simulate হয়
- Real-world data কখনো smooth না (noise থাকে)
- Trend + randomness = realistic dataset

---

## 🚀 What I Learned

- NumPy দিয়ে synthetic data তৈরি করা
- Mathematical function visualization
- Random walk simulation concept
- Real-world data modeling basics

---

## 🧠 Key Concepts (Quick Revision)

- `np.linspace()` → smooth range data
- `sin(x), cos(x)` → wave patterns
- random walk → stock price simulation
- trend + noise → real-world data structure

---

## 📝 Notes

- Real data সবসময় clean হয় না
- Noise ছাড়া data unrealistic হয়
- Simulation data ML training এ ব্যবহার হয়
- Visualization helps to understand hidden patterns

---

## 📌 Next Day Preview

- আগামী দিনে শিখবো:
  - Dash Framework introduction
  - Interactive web dashboard তৈরি
  - Real web-based data apps
  - UI control + callbacks basics

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Moving average add করা
- More complex random walk model
- Real stock data API integration

### 🧪 Practice Ideas

- Weather simulation model বানাও
- Stock price predictor simulation বানাও
- Population growth model visualize করো
