import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
DATETIME SCATTER PLOT
---------------------
Each point represents a value at a time.
"""

dates = pd.date_range("2024-01-01", periods=25, freq="D")
values = np.random.randint(10, 50, size=25)

plt.scatter(dates, values)

plt.title("Time Series Scatter Plot")
plt.xlabel("Date")
plt.ylabel("Value")

plt.xticks(rotation=45)

plt.show()