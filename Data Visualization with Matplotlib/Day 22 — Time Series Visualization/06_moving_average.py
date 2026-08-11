import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
MOVING AVERAGE (TREND SMOOTHING)
--------------------------------
Removes noise and shows smooth trend.
"""

dates = pd.date_range("2024-01-01", periods=30, freq="D")
values = np.random.randint(10, 50, size=30)

# Convert to pandas series
series = pd.Series(values)

# Moving average (window = 5 days)
moving_avg = series.rolling(window=5).mean()

plt.plot(dates, values, label="Original Data")
plt.plot(dates, moving_avg, label="Moving Average", linewidth=3)

plt.title("Moving Average Trend")
plt.xlabel("Date")
plt.ylabel("Value")

plt.xticks(rotation=45)
plt.legend()

plt.show()