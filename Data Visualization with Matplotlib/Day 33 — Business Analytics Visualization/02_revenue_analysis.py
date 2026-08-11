import pandas as pd
import matplotlib.pyplot as plt

"""
REVENUE ANALYSIS
----------------
We focus only on revenue growth.
"""

df = pd.read_csv("business_data.csv")

plt.plot(df["day"], df["revenue"], color="green", marker="o")

plt.title("Revenue Growth Trend")
plt.xlabel("Day")
plt.ylabel("Revenue")

# Show average revenue line
avg_revenue = df["revenue"].mean()
plt.axhline(avg_revenue, color="red", linestyle="--", label="Average Revenue")

plt.legend()
plt.grid(True)

plt.show()