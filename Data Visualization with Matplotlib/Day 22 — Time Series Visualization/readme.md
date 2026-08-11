# 📅 Day 22 — Time Series Visualization

## 🎯 Objective

- আজকে time series data visualization শিখবো
- Date handling এবং datetime plotting practice করবো
- Trend analysis ও financial-style chart বানানো শিখবো
- Real dataset ব্যবহার করে sales trend বুঝবো
- Moving average দিয়ে noise-free trend visualization শিখবো

---

## 📚 Topics Covered

- Date handling
- Time axis formatting
- Time trend analysis
- Financial-style plotting
- Datetime plotting

---

## 📁 Project Structure

```bash
day-22/
│── 01_datetime_basics.py
│── 02_time_axis_formatting.py
│── 03_trend_analysis.py
│── 04_financial_style_plot.py
│── 05_datetime_scatter.py
│── 06_moving_average.py
│── 07_real_time_series_analysis.py
│── sales_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `sales_data.csv`
- **Description:** Daily sales data used for time series visualization and trend analysis

### Columns:

- `date` → Transaction date (time axis)
- `sales` → Sales value for each day

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `01_datetime_basics.py`

### 🔹 Purpose

- Basic time series plotting শেখা
- datetime handling practice করা

### 🧠 Explanation

- `pd.date_range()` দিয়ে date sequence তৈরি করা হয়েছে
- `values` list দিয়ে time-based data তৈরি করা হয়েছে
- `plt.plot(dates, values)` দিয়ে line chart আঁকা হয়েছে
- `plt.xticks(rotation=45)` দিয়ে date labels readable করা হয়েছে

---

## 📄 2. `02_time_axis_formatting.py`

### 🔹 Purpose

- Time axis formatting শিখা

### 🧠 Explanation

- Date range তৈরি করা হয়েছে 15 দিনের জন্য
- Simple increasing values plot করা হয়েছে
- X-axis labels rotate করে overlap avoid করা হয়েছে
- Clean time axis visualization তৈরি হয়েছে

---

## 📄 3. `03_trend_analysis.py`

### 🔹 Purpose

- Time-based trend analysis করা

### 🧠 Explanation

- `np.cumsum()` দিয়ে cumulative trend তৈরি করা হয়েছে
- Random noise + growth simulation করা হয়েছে
- Line plot দিয়ে upward trend visualize করা হয়েছে
- Real-world growth pattern mimic করা হয়েছে

---

## 📄 4. `04_financial_style_plot.py`

### 🔹 Purpose

- Financial/stock market style chart তৈরি করা

### 🧠 Explanation

- Random walk style stock price simulation করা হয়েছে
- `linewidth=2` দিয়ে professional look দেওয়া হয়েছে
- Green color দিয়ে growth signal represent করা হয়েছে
- Finance dashboard-style visualization তৈরি হয়েছে

---

## 📄 5. `05_datetime_scatter.py`

### 🔹 Purpose

- Time series scatter plot বোঝা

### 🧠 Explanation

- প্রতিটি date-এর জন্য random value generate করা হয়েছে
- Scatter plot দিয়ে individual data points show করা হয়েছে
- Trend না, বরং distribution over time দেখানো হয়েছে
- Event-based time visualization বুঝতে সাহায্য করে

---

## 📄 6. `06_moving_average.py`

### 🔹 Purpose

- Noise reduction + trend smoothing শেখা

### 🧠 Explanation

- Pandas Series তৈরি করা হয়েছে
- `rolling(window=5).mean()` ব্যবহার করা হয়েছে moving average-এর জন্য
- Original data + smoothed trend একসাথে plot করা হয়েছে
- Short-term fluctuation remove করে long-term trend দেখা যায়

---

## 📄 7. `07_real_time_series_analysis.py`

### 🔹 Purpose

- Real CSV data দিয়ে time series analysis করা

### 🧠 Explanation

- `sales_data.csv` থেকে data load করা হয়েছে
- `pd.to_datetime()` দিয়ে date column convert করা হয়েছে
- Sales over time line plot করা হয়েছে
- Real business trend visualization তৈরি হয়েছে

---

## ⚙️ Implementation Flow

- Date range তৈরি করা হয়েছে
- Synthetic data দিয়ে trend simulation করা হয়েছে
- Financial-style chart তৈরি করা হয়েছে
- Scatter plot দিয়ে time-based distribution দেখা হয়েছে
- Moving average দিয়ে trend smooth করা হয়েছে
- Real CSV data দিয়ে final analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Time series data trend analysis-এর জন্য খুব powerful
- Moving average noise কমিয়ে clear pattern দেখায়
- Financial charts business insight দেয়
- Scatter plot event-based variation দেখায়
- Real dataset analysis সবচেয়ে practical insight দেয়

---

## 🚀 What I Learned

- datetime handling in Pandas
- time series plotting in Matplotlib
- trend analysis techniques
- moving average concept
- financial-style visualization design

---

## 🧠 Key Concepts (Quick Revision)

- `pd.date_range()` → time sequence তৈরি করে
- `pd.to_datetime()` → string date convert করে
- `plt.plot(dates, values)` → time series line chart
- `rolling(window=n).mean()` → moving average
- `xticks(rotation=45)` → readable time axis
- scatter plot → individual time events

---

## 📝 Notes

- Date format ঠিক না হলে plot ভুল হতে পারে
- Moving average window size important (too big = oversmooth)
- Time axis labels overlap হতে পারে
- Real dataset always better for learning insight

---

## 📌 Next Day Preview

- Pandas + Matplotlib integration deep dive
- DataFrame-based plotting
- Grouped visualization
- CSV workflow automation

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Interactive time slider chart
- Multi-product sales comparison over time
- Auto trend detection system
- Forecasting-based visualization add করা

### 🧪 Practice Ideas

- Stock price simulation chart বানাও
- Weather temperature trend plot করো
- Student attendance over time graph বানাও
- Moving average vs raw data compare করো
