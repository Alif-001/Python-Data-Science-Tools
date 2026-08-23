# 📅 Day 38 — Financial Visualization

---

## 🎯 Objective

- আজকে শিখার লক্ষ্য হলো stock market data কিভাবে visualize করা হয় সেটা বোঝা
- financial charts (candlestick, OHLC) ব্যবহার করে market movement analyze করা
- trading dashboard এর basic concept শেখা
- moving average দিয়ে trend বুঝতে শেখা

---

## 📚 Topics Covered

- Stock Price Line Chart Visualization
- Candlestick Chart (OHLC Concept)
- OHLC Chart (Trading style visualization)
- Moving Average Trend Analysis
- Basic Trading Dashboard Design

---

## 📁 Project Structure

```text
Day 38 — Financial Visualization/
│── 1_stock_line_chart.py
│── 2_candlestick_chart.py
│── 3_ohlc_chart.py
│── 4_trading_dashboard.py
│── stock_data.csv
│── README.md
```

---

## 📊 Dataset

**File Name:** stock_data.csv

**Description:**
এই dataset এ একটি stock এর daily price movement দেখানো হয়েছে (Open, High, Low, Close, Volume সহ)।

**Columns:**

- date → trading date
- open → দিনের শুরু price
- high → দিনের সর্বোচ্চ price
- low → দিনের সর্বনিম্ন price
- close → দিনের শেষ price
- volume → কত শেয়ার trade হয়েছে

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_stock_line_chart.py`

### 🔹 Purpose

- stock price এর simple trend visualization

### 🧾 Code

```python
# line chart for closing price
```

### 🧠 Explanation

- Line 1 → dataset load করা হয়েছে
- Line 2 → close price নেওয়া হয়েছে
- Line 3 → line chart তৈরি করা হয়েছে
- Logic → সময়ের সাথে price কিভাবে change হচ্ছে তা দেখা

---

## 📄 2. `2_candlestick_chart.py`

### 🔹 Purpose

- stock market movement detail visualize করা

### 🧾 Code

```python
# candlestick OHLC chart
```

### 🧠 Explanation

- Line 1 → open, high, low, close data ব্যবহার করা হয়েছে
- Line 2 → candlestick chart তৈরি করা হয়েছে
- Logic → bullish/bearish movement বোঝা যায়

---

## 📄 3. `3_ohlc_chart.py`

### 🔹 Purpose

- simplified trading chart visualization

### 🧾 Code

```python
# OHLC chart
```

### 🧠 Explanation

- Line 1 → OHLC structure ব্যবহার করা হয়েছে
- Line 2 → trading style chart তৈরি করা হয়েছে
- Logic → candlestick এর simplified version

---

## 📄 4. `4_trading_dashboard.py`

### 🔹 Purpose

- price trend + moving average একসাথে দেখানো

### 🧾 Code

```python
# moving average + price chart
```

### 🧠 Explanation

- Line 1 → close price data নেওয়া হয়েছে
- Line 2 → rolling mean (moving average) calculate করা হয়েছে
- Line 3 → trend line + price line একসাথে plot করা হয়েছে
- Logic → market trend smooth করে বোঝা

---

## ⚙️ Implementation Flow

- Stock dataset load করা হয়েছে
- Price data visualize করা হয়েছে
- OHLC structure apply করা হয়েছে
- Candlestick chart তৈরি করা হয়েছে
- Moving average দিয়ে trend analysis করা হয়েছে

---

## 📈 Output / Result

**Key findings:**

- stock price সময়ের সাথে fluctuate করে
- candlestick chart দিয়ে market sentiment বোঝা যায়
- OHLC data trading analysis এর core structure
- moving average trend বুঝতে সাহায্য করে

---

## 🚀 What I Learned

- stock market data structure (OHLC)
- candlestick chart interpretation
- financial time-series visualization
- moving average concept
- basic trading dashboard design

---

## 🧠 Key Concepts (Quick Revision)

- OHLC → Open, High, Low, Close
- Candlestick → market movement visualization
- Line chart → simple trend analysis
- Moving average → noise reduce করে trend দেখায়
- Volume → market activity measure করে

---

## 📝 Notes

- financial data is highly noisy
- moving average helps trend detection
- candlestick chart is industry standard in trading
- proper time-series handling is important

---

## 📌 Next Day Preview

- Real-time dashboard system
- Live data streaming visualization
- API-based stock data integration
- Advanced trading indicators (RSI, MACD)

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- add volume subplot
- add RSI indicator
- compare multiple stocks

### 🧪 Practice Ideas

- build buy/sell signal logic
- try crypto price dataset
- create portfolio dashboard
