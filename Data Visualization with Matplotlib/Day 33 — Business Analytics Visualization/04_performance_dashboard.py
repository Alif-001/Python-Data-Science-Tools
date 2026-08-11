import pandas as pd
import matplotlib.pyplot as plt

"""
PERFORMANCE DASHBOARD
---------------------
Multiple business KPIs in one view.
"""

df = pd.read_csv("business_data.csv")

plt.figure(figsize=(12, 7))

# Sales
plt.subplot(2, 2, 1)
plt.plot(df["day"], df["sales"], color="blue")
plt.title("Sales")

# Revenue
plt.subplot(2, 2, 2)
plt.plot(df["day"], df["revenue"], color="green")
plt.title("Revenue")

# Customers
plt.subplot(2, 2, 3)
plt.bar(df["day"], df["customers"], color="orange")
plt.title("Customers")

# Returns
plt.subplot(2, 2, 4)
plt.bar(df["day"], df["returns"], color="red")
plt.title("Returns")

plt.tight_layout()
plt.show()