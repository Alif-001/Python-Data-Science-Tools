# 📅 Day 28 — Window Functions

---

## 🎯 Objective

- Pandas এ window functions বুঝা ও ব্যবহার করা
- rolling window দিয়ে short-term trend analysis করা
- expanding window দিয়ে cumulative long-term analysis করা
- moving average তৈরি করে data smoothing শেখা
- real-world time series insight generate করা

---

## 📚 Topics Covered

- `rolling()` (fixed-size window)
- `expanding()` (cumulative window)
- moving average concept
- rolling sum & mean
- expanding sum & mean
- short-term vs long-term trend analysis
- time series window operations

---

## 📁 Project Structure

```id="d28proj"
day-28/
│── 01_setup_timeseries.py
│── 02_rolling_basic.py
│── 03_rolling_sum.py
│── 04_expanding_basic.py
│── 05_expanding_sum.py
│── 06_moving_average.py
│── 07_real_world_window.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

### 📄 File Name: data.csv

- **Description:** Daily sales time series dataset

- **Columns:**
  - Date → daily date
  - Sales → daily sales value

👉 এটি একটি sequential time-based dataset

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry File)

### 🔹 Purpose

- window functions module start করা

### 🧾 Code

```python id="w28main"
print("Day 28 - Window Functions Learning")
```

### 🧠 Explanation

- learning module initialization file
- no processing logic

---

## 📄 2. 01_setup_timeseries.py

### 🔹 Purpose

- time series setup তৈরি করা

### 🧾 Code

```python id="w28a"
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
```

### 🧠 Explanation

- date কে index বানানো হয়
- window functions এর জন্য mandatory step

---

## 📄 3. 02_rolling_basic.py

### 🔹 Purpose

- rolling mean calculation

### 🧾 Code

```python id="w28b"
df['Rolling_Mean'] = df['Sales'].rolling(window=3).mean()
```

### 🧠 Explanation

- 3-day window average বের করে
- short-term trend analysis করে

---

## 📄 4. 03_rolling_sum.py

### 🔹 Purpose

- rolling sum calculation

### 🧾 Code

```python id="w28c"
df['Rolling_Sum'] = df['Sales'].rolling(window=3).sum()
```

### 🧠 Explanation

- moving total sales trend দেখায়
- short-term performance measure

---

## 📄 5. 04_expanding_basic.py

### 🔹 Purpose

- cumulative mean calculation

### 🧾 Code

```python id="w28d"
df['Expanding_Mean'] = df['Sales'].expanding().mean()
```

### 🧠 Explanation

- শুরু থেকে সব data consider করে
- long-term trend তৈরি করে

---

## 📄 6. 05_expanding_sum.py

### 🔹 Purpose

- cumulative sum calculation

### 🧾 Code

```python id="w28e"
df['Cumulative_Sales'] = df['Sales'].expanding().sum()
```

### 🧠 Explanation

- total sales accumulation
- running total analysis

---

## 📄 7. 06_moving_average.py

### 🔹 Purpose

- trend smoothing (noise reduction)

### 🧾 Code

```python id="w28f"
df['Moving_Avg'] = df['Sales'].rolling(window=3).mean()
```

### 🧠 Explanation

- fluctuation কমায়
- stable trend visualize করে

---

## 📄 8. 07_real_world_window.py

### 🔹 Purpose

- real-world trend analysis system

### 🧾 Code

```python id="w28g"
df['Rolling_3'] = df['Sales'].rolling(window=3).mean()
df['Expanding'] = df['Sales'].expanding().mean()
```

### 🧠 Explanation

- rolling = short-term trend
- expanding = long-term trend
- comparison analysis করা যায়

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- datetime index set করা হয়েছে
- rolling window applied করা হয়েছে
- expanding window applied করা হয়েছে
- moving average calculated করা হয়েছে
- short vs long-term trend analysis করা হয়েছে

---

## 📈 Output / Result

- short-term sales trend পাওয়া গেছে
- long-term growth trend দেখা গেছে
- moving average smooth data তৈরি হয়েছে
- best sales day identify করা হয়েছে

---

## 🚀 What I Learned

- rolling = fixed window analysis
- expanding = full history analysis
- moving average = noise reduction technique
- window functions = time series core concept
- trend analysis = business decision support

---

## 🧠 Key Concepts (Quick Revision)

- `rolling(window=n)` → short-term trend
- `expanding()` → cumulative trend
- `mean()` → smooth value
- `sum()` → total trend
- rolling = local view
- expanding = global view

---

## 📝 Notes

- rolling needs window size
- expanding grows with dataset
- both are essential for forecasting
- smoothing helps remove noise

---

## 📌 Next Day Preview

👉 Day 29 — MultiIndex

- hierarchical indexing
- multi-level data structure
- advanced selection techniques
- complex dataset handling

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- sales forecasting dashboard
- trend comparison system (rolling vs expanding)

### 🧪 Practice Ideas

- different window sizes try করো
- real dataset এ moving average apply করো
