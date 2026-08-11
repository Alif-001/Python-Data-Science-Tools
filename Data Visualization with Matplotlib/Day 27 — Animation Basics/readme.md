# 📅 Day 27 — Animation Basics

## 🎯 Objective

- আজকে Matplotlib animation system শিখবো
- Frame-by-frame plot update করা শিখবো
- `FuncAnimation` ব্যবহার করে moving plot বানানো শিখবো
- Animated line plot এবং animated scatter plot তৈরি করা শিখবো
- Real-time simulation concept বুঝবো

---

## 📚 Topics Covered

- Introduction to animation
- `FuncAnimation`
- Animated line plot
- Animated scatter plot
- Real-time simulation concept

---

## 📁 Project Structure

```bash
day-27/
│── 01_animation_introduction.py
│── 02_funcanimation_basics.py
│── 03_animated_line_plot.py
│── 04_animated_scatter_plot.py
│── 05_real_time_simulation.py
│── 06_dual_wave_animation.py
│── 07_csv_real_time_animation.py
│── sensor_data_stream.csv
│── README.md
```

---

## 📊 Dataset

### **File Name:** `sensor_data_stream.csv`

- **Description:** Simple sensor-style time series data used for real-time animation simulation

### **Columns:**

- `time` → Time index of the data stream
- `value` → Sensor reading / incoming value

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `main.py`

### 🔹 Purpose

- Animation basics concept বোঝা
- Frame update logic introduction দেওয়া

### 🧾 Code

```python
print("Day 27 - Animation Basics 🎞️")
```

### 🧠 Explanation

- Line 1 → simple intro message print করছে
- Line 1 → day topic identify করতে সাহায্য করছে
- Logic → animation কীভাবে plot পরিবর্তন করে, সেই ধারণা শুরুতেই দেওয়া হয়েছে

---

## 📄 2. `analysis.py`

### 🔹 Purpose

- Animation-এর জন্য data pattern বুঝতে সাহায্য করা
- Incoming values analyze করার ধারণা দেওয়া

### 🧾 Code

```python
def get_value_range(values):
    return min(values), max(values)
```

### 🧠 Explanation

- Step 1 → values list থেকে minimum এবং maximum বের করছে
- Step 2 → animation axis range বুঝতে useful
- Function → moving plot-এর limit ঠিক করতে সাহায্য করতে পারে

---

## 📄 3. `utils.py`

### 🔹 Purpose

- Helper functions রাখা
- Reusable animation logic support করা

### 🧾 Code

```python
def format_title(text):
    return text.strip().title()
```

### 🧠 Explanation

- Text clean করে সুন্দর title বানায়
- Reusable helper হিসেবে কাজ করে
- Dashboard বা animation title formatting-এ useful

---

## 📄 4. `01_animation_introduction.py`

### 🔹 Purpose

- Animation-এর basic idea বোঝা

### 🧾 Code

- `FuncAnimation` দিয়ে sine wave frame-by-frame move করা হয়েছে
- `update(frame)` function plot-এর y-data পরিবর্তন করছে

### 🧠 Explanation

- Line 1 → necessary library import করা হয়েছে
- Line 2 → figure এবং axis তৈরি করা হয়েছে
- Logic → প্রতিটি frame-এ sine wave shift হয়ে motion effect তৈরি করছে
- This is the first step to understand animated plotting

---

## 📄 5. `02_funcanimation_basics.py`

### 🔹 Purpose

- `FuncAnimation` কীভাবে কাজ করে তা শেখা

### 🧾 Code

- `animate(i)` function repeatedly call হচ্ছে
- `line.set_ydata()` দিয়ে wave update করা হচ্ছে

### 🧠 Explanation

- Step 1 → x-axis values তৈরি করা হয়েছে
- Step 2 → initial sine plot draw করা হয়েছে
- Step 3 → `animate()` function প্রতি frame-এ y-values বদলাচ্ছে
- Logic → plot continuously move করছে, তাই animation effect দেখা যাচ্ছে

---

## 📄 6. `03_animated_line_plot.py`

### 🔹 Purpose

- Animated line plot বানানো

### 🧾 Code

- Empty line initialize করা হয়েছে
- `init()` function plot reset করছে
- `update(i)` function line data set করছে

### 🧠 Explanation

- Step 1 → empty line দিয়ে animation start করা হয়েছে
- Step 2 → axis limit set করা হয়েছে
- Step 3 → sine wave প্রতি frame-এ update হচ্ছে
- Logic → smooth moving signal / live chart effect তৈরি করছে

---

## 📄 7. `04_animated_scatter_plot.py`

### 🔹 Purpose

- Animated scatter plot তৈরি করা

### 🧾 Code

- Random points generate করা হয়েছে
- প্রতি frame-এ points সামান্য move করছে
- `scatter.set_offsets()` দিয়ে new position বসানো হয়েছে

### 🧠 Explanation

- Step 1 → initial random scatter points তৈরি হয়েছে
- Step 2 → `update()` function প্রতিবার x/y adjust করছে
- Step 3 → scatter plot নতুন position নেয়
- Logic → particle movement বা clustering simulation-এর মতো effect পাওয়া যায়

---

## 📄 8. `05_real_time_simulation.py`

### 🔹 Purpose

- Real-time data stream simulation করা

### 🧾 Code

- `x_data` এবং `y_data` list-এ incoming data append করা হচ্ছে
- `FuncAnimation` দিয়ে live-like chart বানানো হয়েছে

### 🧠 Explanation

- Step 1 → empty data lists রাখা হয়েছে
- Step 2 → প্রতি frame-এ নতুন value add হচ্ছে
- Step 3 → line plot update হচ্ছে
- Logic → sensor data বা stock data live feed-এর মতো visualize করা হয়েছে

---

## 📄 9. `06_dual_wave_animation.py`

### 🔹 Purpose

- একসাথে দুইটি moving wave দেখানো

### 🧾 Code

- Sine এবং cosine line একসাথে animate করা হয়েছে
- দুইটি line একই update function-এ shift হচ্ছে

### 🧠 Explanation

- Step 1 → দুইটি wave plot করা হয়েছে
- Step 2 → `update(i)` function উভয় line পরিবর্তন করছে
- Step 3 → combined motion দেখা যাচ্ছে
- Logic → signal interference বা dual waveform ধারণা বোঝানো হয়েছে

---

## 📄 10. `07_csv_real_time_animation.py`

### 🔹 Purpose

- CSV data ব্যবহার করে real-time style animation করা

### 🧾 Code

- CSV file থেকে time এবং value read করা হয়েছে
- `update(i)` function একে একে data show করছে
- `FuncAnimation` frame-by-frame data reveal করছে

### 🧠 Explanation

- Step 1 → CSV data load করা হয়েছে
- Step 2 → time/value list তৈরি করা হয়েছে
- Step 3 → প্রতি frame-এ একটি নতুন point add হচ্ছে
- Logic → real sensor stream বা incoming data sequence দেখানো হয়েছে

---

## ⚙️ Implementation Flow

- Animation concept introduce করা হয়েছে
- `FuncAnimation` ব্যবহার করা হয়েছে
- Line plot dynamically update করা হয়েছে
- Scatter plot moving effect তৈরি করেছে
- Real-time simulation idea শেখা হয়েছে
- CSV data দিয়ে live-like animation বানানো হয়েছে

---

## 📈 Output / Result

### **Key findings:**

- Animation plot-কে dynamic করে
- `FuncAnimation` Matplotlib animation-এর core
- Line and scatter both animate করা যায়
- Real-time data simulation সহজে করা যায়
- CSV data থেকে streaming-like chart বানানো সম্ভব

---

## 🚀 What I Learned

- Matplotlib animation concept
- `FuncAnimation` usage
- update function কীভাবে কাজ করে
- line and scatter animation
- real-time visualization pattern

---

## 🧠 Key Concepts (Quick Revision)

- `FuncAnimation` → animation creator
- `update()` → প্রতি frame-এ plot change করে
- `init_func` → animation শুরুতে empty state set করে
- `set_ydata()` → line update করে
- `set_offsets()` → scatter update করে
- real-time simulation → live data feel দেয়

---

## 📝 Notes

- Animation smooth রাখতে interval ঠিক রাখা দরকার
- Axis limit fixed না হলে plot jump করতে পারে
- Too much data হলে performance issue হতে পারে
- Real-time visuals clean রাখতে simple layout ভালো

---

## 📌 Next Day Preview

- 3D plotting introduction
- 3D scatter, surface, wireframe
- Camera angle control
- Scientific 3D visualization

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- live sensor dashboard বানানো
- multiple animated signals add করা
- smoother interpolation ব্যবহার করা
- stock market real-time simulator বানানো

### 🧪 Practice Ideas

- sine wave motion animation বানাও
- random particle movement simulation করো
- sensor stream animation তৈরি করো
- two-wave interference animation modify করো
