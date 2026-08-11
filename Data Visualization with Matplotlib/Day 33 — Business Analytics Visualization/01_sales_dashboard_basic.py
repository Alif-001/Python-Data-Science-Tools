import pandas as pd
import matplotlib.pyplot as plt

"""
DAY 33 - BUSINESS ANALYTICS VISUALIZATION
-----------------------------------------
We start with a simple sales dashboard.
"""

df = pd.read_csv("business_data.csv")

plt.figure(figsize=(10, 5))

# Sales trend line
plt.plot(df["day"], df["sales"], marker="o", label="Sales")

# Revenue trend line
plt.plot(df["day"], df["revenue"], marker="o", label="Revenue")

plt.title("Sales & Revenue Trend")
plt.xlabel("Day")
plt.ylabel("Value")

plt.legend()
plt.grid(True)

plt.show()