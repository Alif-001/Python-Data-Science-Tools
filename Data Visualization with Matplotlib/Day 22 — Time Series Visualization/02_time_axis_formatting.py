import matplotlib.pyplot as plt
import pandas as pd

"""
TIME AXIS FORMATTING
--------------------
We format date labels to look clean and readable.
"""

dates = pd.date_range("2024-01-01", periods=15, freq="D")
values = range(15)

plt.plot(dates, values)

plt.title("Time Axis Formatting")
plt.xlabel("Date")
plt.ylabel("Value")

# Rotate and align labels
plt.xticks(rotation=45)

plt.show()