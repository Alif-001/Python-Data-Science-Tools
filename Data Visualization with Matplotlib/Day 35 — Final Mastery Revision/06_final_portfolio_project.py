import pandas as pd
import matplotlib.pyplot as plt

"""
FINAL PORTFOLIO PROJECT
----------------------
This is your MASTER PROJECT.
"""

df = pd.read_csv("final_portfolio_data.csv")

plt.figure(figsize=(12, 8))

# Sales trend
plt.subplot(2, 2, 1)
plt.plot(df["day"], df["sales"], color="blue")
plt.title("Sales Trend")

# Profit trend
plt.subplot(2, 2, 2)
plt.plot(df["day"], df["profit"], color="green")
plt.title("Profit Trend")

# Customers
plt.subplot(2, 2, 3)
plt.bar(df["day"], df["customers"], color="orange")
plt.title("Customers")

# Marketing impact
plt.subplot(2, 2, 4)
plt.plot(df["marketing_spend"], df["sales"], marker="o")
plt.title("Marketing vs Sales")

plt.tight_layout()
plt.show()