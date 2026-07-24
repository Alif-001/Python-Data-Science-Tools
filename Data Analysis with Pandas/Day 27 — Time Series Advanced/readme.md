# 📅 Day 27 — Time Series Advanced

---

## 🎯 Objective

- Time series data handle করা শেখা
- date কে index বানিয়ে analysis করা
- `resample()` দিয়ে time grouping করা
- `rolling()` দিয়ে moving average/trend smoothing করা
- real-world sales trend analysis করা

---

## 📚 Topics Covered

- datetime index creation
- time series indexing
- `resample()` (time grouping)
- `rolling()` (moving window)
- sum & mean aggregation over time
- trend analysis (daily → weekly)
- forecasting-style thinking basics

---

## 📁 Project Structure

```id="d27proj"
day-27/
│── 01_datetime_index.py
│── 02_resample_basic.py
│── 03_resample_mean.py
│── 04_rolling_basic.py
│── 05_rolling_sum.py
│── 06_combined_resample_rolling.py
│── 07_real_world_time_series.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

### 📄 File Name: data.csv

- **Description:** Daily sales dataset (time series data)

- **Columns:**
  - Date → daily date
  - Sales → sales amount

👉 এটি একটি **time-based sequential dataset**

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry File)

### 🔹 Purpose

- time series module initialization

### 🧾 Code

```python id="ts27main"
print("Day 27 - Time Series Advanced Learning")
```

### 🧠 Explanation

- project start indicator file
- no processing logic

---

## 📄 2. 01_datetime_index.py

### 🔹 Purpose

- date কে datetime index বানানো

### 🧾 Code

```python id="ts27a"
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
```

### 🧠 Explanation

- time series analysis এর জন্য index গুরুত্বপূর্ণ
- date-based operations সহজ হয়

---

## 📄 3. 02_resample_basic.py

### 🔹 Purpose

- daily data → weekly data convert করা

### 🧾 Code

```python id="ts27b"
weekly_sales = df.resample('W').sum()
```

### 🧠 Explanation

- `resample('W')` → weekly grouping
- business reporting সহজ হয়

---

## 📄 4. 03_resample_mean.py

### 🔹 Purpose

- weekly average sales বের করা

### 🧾 Code

```python id="ts27c"
weekly_avg = df.resample('W').mean()
```

### 🧠 Explanation

- average trend analysis
- performance smoothing view

---

## 📄 5. 04_rolling_basic.py

### 🔹 Purpose

- moving average (trend smoothing)

### 🧾 Code

```python id="ts27d"
df['Rolling_Mean'] = df['Sales'].rolling(window=3).mean()
```

### 🧠 Explanation

- 3-day window trend তৈরি করে
- noise কমায়, pattern clear করে

---

## 📄 6. 05_rolling_sum.py

### 🔹 Purpose

- rolling total sales

### 🧾 Code

```python id="ts27e"
df['Rolling_Sum'] = df['Sales'].rolling(window=3).sum()
```

### 🧠 Explanation

- moving total sales trend
- short-term performance analysis

---

## 📄 7. 06_combined_resample_rolling.py

### 🔹 Purpose

- resample + rolling combined analysis

### 🧾 Code

```python id="ts27f"
weekly = df.resample('W').sum()
weekly['Rolling_Avg'] = weekly['Sales'].rolling(window=2).mean()
```

### 🧠 Explanation

- scale change (daily → weekly)
- তারপর trend smoothing

---

## 📄 8. 07_real_world_time_series.py

### 🔹 Purpose

- real-world sales trend analysis

### 🧾 Code

```python id="ts27g"
df['Rolling_3day'] = df['Sales'].rolling(window=3).mean()
weekly = df.resample('W').sum()
```

### 🧠 Explanation

- daily trend + weekly summary
- best sales day identify করা
- business insight extraction

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- date → datetime convert করা হয়েছে
- date কে index বানানো হয়েছে
- resample দিয়ে weekly grouping করা হয়েছে
- rolling window দিয়ে trend smoothing করা হয়েছে
- insights generate করা হয়েছে

---

## 📈 Output / Result

- daily sales trend পাওয়া গেছে
- weekly sales summary তৈরি হয়েছে
- moving average trend তৈরি হয়েছে
- best sales day identify করা হয়েছে

---

## 🚀 What I Learned

- time series = sequential data analysis
- datetime index = essential for time operations
- resample = time grouping tool
- rolling = trend smoothing technique
- forecasting foundation starts here

---

## 🧠 Key Concepts (Quick Revision)

- `set_index(Date)` → time index
- `resample('W')` → weekly grouping
- `rolling(window=n)` → moving window
- `mean()` → smooth trend
- `sum()` → total trend
- time series = business forecasting base

---

## 📝 Notes

- time index is mandatory for resample
- rolling introduces NaN at start
- smoothing helps remove noise
- resample = scale change tool

---

## 📌 Next Day Preview

👉 Day 28 — Window Functions

- expanding window
- cumulative analysis
- rolling vs expanding difference
- advanced trend analytics

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- sales forecasting dashboard
- demand prediction system

### 🧪 Practice Ideas

- different window size try করো
- daily vs weekly vs monthly compare করো
