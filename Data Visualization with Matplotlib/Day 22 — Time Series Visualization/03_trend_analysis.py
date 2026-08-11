import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
TIME TREND ANALYSIS
-------------------
We analyze upward/downward trends.
"""

dates = pd.date_range("2024-01-01", periods=30, freq="D")

# Simulated increasing trend + noise
values = np.cumsum(np.random.randint(1, 5, size=30))

plt.plot(dates, values, marker="o")

plt.title("Trend Analysis Over Time")
plt.xlabel("Date")
plt.ylabel("Value")

plt.xticks(rotation=45)

plt.show()