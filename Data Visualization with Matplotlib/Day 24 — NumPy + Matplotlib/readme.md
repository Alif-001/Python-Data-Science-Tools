# 📅 Day 24 — NumPy + Matplotlib

## 🎯 Objective

- আজকে NumPy ব্যবহার করে mathematical function plot করা শিখবো
- sine, cosine wave visualize করা শিখবো
- random data এবং simulation plot করা শিখবো
- real-life mathematical modeling practice করবো
- CSV + NumPy + Matplotlib integration শিখবো

---

## 📚 Topics Covered

- Plotting mathematical functions
- Sine wave visualization
- Cosine wave visualization
- Random data visualization
- Mathematical simulations

---

## 📁 Project Structure

```bash
day-24/
│── 01_numpy_function_plot.py
│── 02_sine_wave.py
│── 03_cosine_wave.py
│── 04_sine_cosine_together.py
│── 05_random_data_visualization.py
│── 06_mathematical_simulation.py
│── 07_wave_combination.py
│── 08_csv_numpy_plot.py
│── temperature_simulation.csv
│── README.md
```

---

## 📊 Dataset

### 📄 File Name: `temperature_simulation.csv`

- **Description:** Simple temperature growth simulation data used for numerical visualization

### Columns:

- `time` → Time index
- `temperature` → Temperature value over time

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `main.py` (Concept Entry)

### 🔹 Purpose

- NumPy + Matplotlib integration ধারণা বোঝা
- mathematical visualization introduction

### 🧾 Code

```python id="np1"
print("Day 24 - NumPy + Matplotlib 📊")
```

### 🧠 Explanation

- NumPy numerical computation handle করে
- Matplotlib visualization handle করে
- দুটো একসাথে scientific plotting এর backbone

---

## 📄 2. `analysis.py`

### 🔹 Purpose

- mathematical data analysis helper

### 🧾 Code

```python id="np2"
def describe_array(arr):
    return {
        "mean": arr.mean(),
        "max": arr.max(),
        "min": arr.min()
    }
```

### 🧠 Explanation

- array summary statistics বের করে
- mathematical insight দেয়

---

## 📄 3. `utils.py`

### 🔹 Purpose

- reusable numerical helper functions

### 🧾 Code

```python id="np3"
import numpy as np

def generate_range(start, end, points):
    return np.linspace(start, end, points)
```

### 🧠 Explanation

- evenly spaced numerical data তৈরি করে
- plotting-এর জন্য smooth curve তৈরি করতে সাহায্য করে

---

## 📄 4. `01_numpy_function_plot.py`

### 🔹 Purpose

- mathematical function plotting শেখা

### 🧠 Explanation

- `np.linspace()` দিয়ে smooth X values তৈরি করা হয়েছে
- `y = x²` quadratic function plot করা হয়েছে
- function visualization concept বোঝানো হয়েছে

---

## 📄 5. `02_sine_wave.py`

### 🔹 Purpose

- sine wave visualization শেখা

### 🧠 Explanation

- `sin(x)` wave physics/signal processing-এ খুব important
- smooth oscillation pattern দেখানো হয়েছে
- grid enable করে readability বাড়ানো হয়েছে

---

## 📄 6. `03_cosine_wave.py`

### 🔹 Purpose

- cosine wave visualization

### 🧠 Explanation

- sine wave-এর phase shifted version
- red color দিয়ে differentiation করা হয়েছে
- periodic function concept বোঝানো হয়েছে

---

## 📄 7. `04_sine_cosine_together.py`

### 🔹 Purpose

- sine vs cosine comparison

### 🧠 Explanation

- দুইটি wave একই graph-এ compare করা হয়েছে
- legend ব্যবহার করে identify করা হয়েছে
- wave relationship visually বোঝানো হয়েছে

---

## 📄 8. `05_random_data_visualization.py`

### 🔹 Purpose

- random data visualization শেখা

### 🧠 Explanation

- `np.random.randn()` দিয়ে noise data তৈরি করা হয়েছে
- real-world randomness simulate করা হয়েছে
- ML/data science noise concept বোঝানো হয়েছে

---

## 📄 9. `06_mathematical_simulation.py`

### 🔹 Purpose

- exponential growth simulation

### 🧠 Explanation

- `np.exp()` দিয়ে growth model তৈরি করা হয়েছে
- population/finance growth mimic করা হয়েছে
- continuous growth pattern visualize করা হয়েছে

---

## 📄 10. `07_wave_combination.py`

### 🔹 Purpose

- wave interference simulation

### 🧠 Explanation

- sine waves combine করে new signal তৈরি করা হয়েছে
- physics-based interference concept দেখানো হয়েছে
- combined wave pattern analysis করা হয়েছে

---

## 📄 11. `08_csv_numpy_plot.py`

### 🔹 Purpose

- CSV + NumPy + Matplotlib integration

### 🧠 Explanation

- CSV file থেকে time-temperature data read করা হয়েছে
- NumPy array conversion করা হয়েছে
- `np.interp()` দিয়ে smooth curve তৈরি করা হয়েছে
- real-world simulation visualization করা হয়েছে

---

## ⚙️ Implementation Flow

- mathematical functions তৈরি করা হয়েছে
- sine/cosine waves visualize করা হয়েছে
- random data generate করা হয়েছে
- exponential simulation তৈরি করা হয়েছে
- wave interference model করা হয়েছে
- CSV data থেকে real simulation plot করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- NumPy numerical computation সহজ করে
- Matplotlib scientific visualization power দেয়
- sine/cosine wave physics representation করে
- random data real-world noise simulate করে
- interpolation smooth curve তৈরি করে

---

## 🚀 What I Learned

- NumPy array-based computation
- mathematical function plotting
- wave visualization concept
- random data simulation
- CSV + NumPy integration

---

## 🧠 Key Concepts (Quick Revision)

- `np.linspace()` → smooth range তৈরি করে
- `np.sin()` → sine wave
- `np.cos()` → cosine wave
- `np.exp()` → exponential growth
- `np.random.randn()` → random noise
- `np.interp()` → smoothing technique

---

## 📝 Notes

- smooth curve requires enough data points
- random data always noisy by nature
- sine/cosine periodic functions
- interpolation approximation method

---

## 📌 Next Day Preview

- Statistical visualization deep dive
- Mean, median, distribution plots
- Box plot, violin plot introduction
- Data analysis visualization

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- interactive wave simulator
- real physics motion model
- stock price mathematical simulation
- noise filtering system

### 🧪 Practice Ideas

- sine wave speed change experiment
- temperature growth model modify করো
- random dataset analyze করো
- wave combination experiment করো
