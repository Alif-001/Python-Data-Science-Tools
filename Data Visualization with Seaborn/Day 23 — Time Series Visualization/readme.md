# 📅 Day 23 — Time Series Visualization

---

# 🎯 Objective

- Time-based data visualization শেখা
- Trend analysis বোঝা
- Rolling average দিয়ে noise smooth করা শেখা
- Seasonal pattern detect করা
- Real-world business insight তৈরি করা

---

# 📚 Topics Covered

- Time series line plot (`sns.lineplot`)
- Multi-variable time comparison
- Rolling average (smoothing)
- Trend analysis (`regplot`)
- Seasonal pattern visualization
- Business insight extraction

---

# 📁 Project Structure

```bash
day-23/
│── 01_basic_time_series.py
│── 02_sales_vs_temperature.py
│── 03_rolling_average.py
│── 04_trend_analysis.py
│── 05_seasonal_pattern.py
│── 06_multi_variable_time_series.py
│── 07_real_world_business_analysis.py
│── sales_data.csv
│── README.md
```

---

# 📊 Dataset

## 📌 File Name: `sales_data.csv`

## 📌 Description

এই dataset এ daily sales এবং temperature data দেওয়া আছে, যা time-based analysis করার জন্য ব্যবহার করা হয়েছে।

---

## 📌 Columns

- `date` → সময় (দিন অনুযায়ী)
- `sales` → প্রতিদিনের sales value
- `temperature` → daily temperature (external factor)

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_time_series.py

## 🔹 Purpose

- Basic time series line plot তৈরি করা
- Time vs Sales relationship বোঝা

## 🧾 Code

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

sns.lineplot(data=df, x="date", y="sales")

plt.title("Sales Over Time")
plt.xticks(rotation=45)
plt.show()
```

## 🧠 Explanation

- `pd.to_datetime()` → date format convert করা হয়েছে
- `sns.lineplot()` → time-based trend দেখানো হয়েছে
- X-axis = time, Y-axis = sales trend

---

# 📄 2. 02_sales_vs_temperature.py

## 🔹 Purpose

- দুইটা variable একসাথে compare করা
- external factor (temperature) effect বোঝা

## 🧾 Code

```python
sns.lineplot(data=df, x="date", y="sales", label="Sales")
sns.lineplot(data=df, x="date", y="temperature", label="Temperature")
```

## 🧠 Explanation

- Multiple line plot ব্যবহার করা হয়েছে
- Sales vs Temperature relationship compare করা হয়েছে
- Seasonal effect hint পাওয়া যায়

---

# 📄 3. 03_rolling_average.py

## 🔹 Purpose

- Noise remove করে smooth trend বের করা
- Rolling average concept শেখা

## 🧾 Code

```python
df["sales_roll"] = df["sales"].rolling(window=3).mean()

sns.lineplot(data=df, x="date", y="sales", label="Original")
sns.lineplot(data=df, x="date", y="sales_roll", label="Rolling Avg")
```

## 🧠 Explanation

- `rolling(window=3)` → 3 দিনের average নেয়
- Smooth curve তৈরি হয়
- Real trend clearly বোঝা যায়

---

# 📄 4. 04_trend_analysis.py

## 🔹 Purpose

- Overall trend direction বোঝা
- Growth pattern detect করা

## 🧾 Code

```python
sns.regplot(x=df.index, y=df["sales"])
```

## 🧠 Explanation

- Regression line → upward/downward trend দেখায়
- Business growth analysis এর জন্য useful

---

# 📄 5. 05_seasonal_pattern.py

## 🔹 Purpose

- Seasonal pattern detect করা
- Repeating behavior বোঝা

## 🧾 Code

```python
df["day"] = df["date"].dt.day

sns.lineplot(data=df, x="day", y="sales")
```

## 🧠 Explanation

- Day-wise pattern analysis করা হয়েছে
- Cyclical behavior দেখা যায়

---

# 📄 6. 06_multi_variable_time_series.py

## 🔹 Purpose

- Multiple variables একসাথে compare করা

## 🧾 Code

```python
sns.lineplot(data=df, x="date", y="sales", label="Sales")
sns.lineplot(data=df, x="date", y="temperature", label="Temperature")
```

## 🧠 Explanation

- Sales vs temperature relation analysis
- Correlation intuition পাওয়া যায়

---

# 📄 7. 07_real_world_business_analysis.py

## 🔹 Purpose

- Real business insight তৈরি করা
- Trend + smoothing একসাথে দেখা

## 🧾 Code

```python
df["sales_roll"] = df["sales"].rolling(window=3).mean()

sns.lineplot(data=df, x="date", y="sales", label="Sales")
sns.lineplot(data=df, x="date", y="sales_roll", label="Trend")
```

## 🧠 Explanation

- Business decision-making support করে
- Trend vs actual data compare করা যায়

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Date column convert করা হয়েছে
- Line plots তৈরি করা হয়েছে
- Multi-variable comparison করা হয়েছে
- Rolling average calculate করা হয়েছে
- Trend analysis করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Sales সময়ের সাথে পরিবর্তন হয়
- Temperature effect থাকতে পারে
- Rolling average trend clear করে
- Seasonal pattern detect করা যায়

---

# 🚀 What I Learned

- Time series visualization
- Trend analysis technique
- Rolling average concept
- Multi-variable comparison
- Business insight extraction

---

# 🧠 Key Concepts (Quick Revision)

- Time series = time-based data analysis
- `sns.lineplot()` = main tool
- Rolling mean = smoothing technique
- Regression = trend direction
- Seasonality = repeating pattern

---

# 📝 Notes

## 📌 Mistakes

- date column না convert করলে error হয়
- rolling window small/large হলে misleading result হতে পারে

## 📌 Optimization Tips

- Always sort data by date
- Use rolling mean for clean trend
- Compare multiple variables for insight

---

# 📌 Next Day Preview

## 📅 Day 24 — Statistical Visualization

- Mean vs median comparison
- Confidence interval visualization
- Distribution-based insights
- Statistical storytelling

---

# ⭐ Bonus

## 🔥 Improvements Ideas

- Real stock market data try করা
- Crypto price trend analysis করা
- Weather forecasting pattern study করা

---

## 🧪 Practice Ideas

- Different rolling window try করো (3, 5, 7)
- Temperature effect analyze করো
- Uptrend vs downtrend identify করো
