import pandas as pd
import matplotlib.pyplot as plt

"""
PROFIT ESTIMATION VISUALIZATION
-------------------------------
We estimate profit (Revenue - Sales cost assumption).
"""

df = pd.read_csv("business_data.csv")

# Assume cost = 70% of sales
df["profit"] = df["revenue"] - (df["sales"] * 10)

plt.plot(df["day"], df["profit"], marker="o", color="green")

plt.title("Estimated Profit Trend")
plt.xlabel("Day")
plt.ylabel("Profit")

plt.axhline(df["profit"].mean(), color="red", linestyle="--", label="Avg Profit")

plt.legend()
plt.grid(True)

plt.show()