import pandas as pd
import matplotlib.pyplot as plt

"""
FULL BUSINESS DASHBOARD
----------------------
Complete analytics dashboard (real-world style)
"""

df = pd.read_csv("business_data.csv")

fig = plt.figure(figsize=(12, 8))

# Sales
plt.subplot(2, 2, 1)
plt.plot(df["day"], df["sales"])
plt.title("Sales Trend")

# Revenue
plt.subplot(2, 2, 2)
plt.plot(df["day"], df["revenue"], color="green")
plt.title("Revenue Trend")

# Customers
plt.subplot(2, 2, 3)
plt.bar(df["day"], df["customers"], color="orange")
plt.title("Customers")

# Region performance
plt.subplot(2, 2, 4)
df.groupby("region")["sales"].sum().plot(kind="bar", color="purple")
plt.title("Region Performance")

plt.tight_layout()
plt.show()