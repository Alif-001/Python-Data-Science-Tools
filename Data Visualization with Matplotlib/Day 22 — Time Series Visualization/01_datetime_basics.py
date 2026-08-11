import matplotlib.pyplot as plt
import pandas as pd

"""
DAY 22 - TIME SERIES VISUALIZATION
----------------------------------
Time series = data over time (dates + values)

We use datetime to handle time correctly.
"""

# Create simple time data
dates = pd.date_range(start="2024-01-01", periods=10, freq="D")

values = [10, 12, 15, 14, 18, 20, 19, 22, 25, 28]

# Plot
plt.plot(dates, values)

plt.title("Basic Time Series Plot")
plt.xlabel("Date")
plt.ylabel("Value")

plt.xticks(rotation=45)  # rotate date labels for readability

plt.show()