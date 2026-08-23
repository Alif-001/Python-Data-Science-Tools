# 📅 Day 39 — Scientific & Research Visualization

---

## 🎯 Objective

- আজকে লক্ষ্য ছিল scientific data এবং real-world simulation visualize করা
- physics, biology এবং research data কিভাবে graph আকারে বোঝানো যায় তা শেখা
- simulation model এবং experimental dataset বিশ্লেষণ করা
- research-quality multi-plot dashboard তৈরি করা

---

## 📚 Topics Covered

- Scientific function plotting (physics-based graphs)
- Simulation models (growth & decay systems)
- Experimental data visualization
- Multi-plot research dashboard (subplot system)

---

## 📁 Project Structure

```text
Day 39 — Scientific & Research Visualization/
│── main.py
│── analysis.py
│── utils.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** experiment_data.csv
- **Description:** Laboratory experiment data containing time-based measurements of temperature and pressure

### Columns:

- time → measurement time steps
- temperature → heat level at each time point
- pressure → pressure value at each time point

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py

### 🔹 Purpose

- scientific function plotting
- physics-based damped wave visualization

### 🧾 Code

```python
import numpy as np
import plotly.graph_objects as go

x = np.linspace(0, 10, 200)
y = np.sin(x) * np.exp(-x * 0.1)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="lines",
    name="Damped Wave"
))

fig.show()
```

### 🧠 Explanation

- Line 1 → NumPy import করা হয়েছে numerical computation এর জন্য
- Line 2 → Plotly ব্যবহার করা হয়েছে visualization এর জন্য
- Line 4 → x-axis তৈরি করা হয়েছে continuous scientific range দিয়ে
- Line 5 → damped wave তৈরি করা হয়েছে (sin + exponential decay)
- Logic → physics-based wave decay visualize করা হয়েছে

---

## 📄 2. analysis.py

### 🔹 Purpose

- simulation model (logistic growth)
- real-world biological growth pattern analysis

### 🧾 Code

```python
import numpy as np
import plotly.graph_objects as go

t = np.arange(0, 50)

K = 100
P0 = 5
r = 0.2

population = K / (1 + ((K - P0) / P0) * np.exp(-r * t))

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=t,
    y=population,
    mode="lines",
    name="Population Growth"
))

fig.show()
```

### 🧠 Explanation

- step 1 → time series তৈরি করা হয়েছে
- step 2 → logistic growth formula ব্যবহার করা হয়েছে
- step 3 → population growth simulate করা হয়েছে
- step 4 → graph দিয়ে growth pattern visualize করা হয়েছে

---

## 📄 3. utils.py (if any)

### 🔹 Purpose

- helper logic for plotting and reusable visualization functions

### 🧾 Code

```python
def normalize(data):
    return (data - min(data)) / (max(data) - min(data))
```

### 🧠 Explanation

- reusable function তৈরি করা হয়েছে
- data scaling এর জন্য ব্যবহার করা হয়
- scientific plotting এর আগে normalization কাজে লাগে

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- scientific model তৈরি করা হয়েছে
- simulation run করা হয়েছে
- experimental data visualize করা হয়েছে
- multi-plot dashboard তৈরি করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- damped wave সময়ের সাথে কমে যায় (energy loss pattern)
- population growth শুরুতে fast, পরে stable হয়
- temperature ও pressure একই time-series pattern follow করে
- multi-variable analysis সহজভাবে বোঝা যায় dashboard দিয়ে

---

## 🚀 What I Learned

- scientific function কিভাবে plot করতে হয়
- real-world simulation model কিভাবে কাজ করে
- experimental data কিভাবে analyze করতে হয়
- research-style dashboard তৈরি করার logic

---

## 🧠 Key Concepts (Quick Revision)

- damped wave = sin(x) × exponential decay
- logistic growth = real biological population model
- time series = continuous data over time
- subplot = multiple graphs in one dashboard

---

## 📝 Notes

- scientific data সবসময় smooth না (noise থাকতে পারে)
- simulation ≠ real data, কিন্তু behavior mimic করে
- model validation করা খুব গুরুত্বপূর্ণ

---

## 📌 Next Day Preview

- আগামী দিনে আমরা advanced analytics dashboard + real-world case study করবো
- business + scientific data combine করে visualization করা হবে
- performance-focused dashboard design শিখবো

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- noise addition in simulation
- interactive sliders for parameters
- real-time data streaming visualization

### 🧪 Practice Ideas

- cosine damped wave try করা
- different growth rate দিয়ে simulation চালানো
- own experiment dataset বানিয়ে plot করা
