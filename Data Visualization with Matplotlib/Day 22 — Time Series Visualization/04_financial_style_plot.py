import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
FINANCIAL STYLE PLOT
--------------------
Used in stock market visualization.
"""

dates = pd.date_range("2024-01-01", periods=20, freq="D")

# Simulated stock prices
prices = np.cumsum(np.random.randn(20) * 2 + 50)

plt.plot(dates, prices, color="green", linewidth=2)

plt.title("Stock Price Simulation")
plt.xlabel("Date")
plt.ylabel("Price")

plt.xticks(rotation=45)

plt.show()