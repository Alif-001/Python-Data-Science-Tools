import pandas as pd
import matplotlib.pyplot as plt

"""
REAL DASHBOARD FROM CSV
-----------------------
Full real-world workflow:
CSV → Data → Dashboard
"""

df = pd.read_csv("dashboard_sales_data.csv")

days = df["day"]
sales = df["sales"]
profit = df["profit"]
customers = df["customers"]

plt.figure(figsize=(12, 7))

# ---- Sales ----
plt.subplot(2, 2, 1)
plt.plot(days, sales, marker="o")
plt.title("Sales Trend")

# ---- Profit ----
plt.subplot(2, 2, 2)
plt.plot(days, profit, marker="o", color="green")
plt.title("Profit Trend")

# ---- Customers ----
plt.subplot(2, 2, 3)
plt.bar(days, customers, color="orange")
plt.title("Customers")

# ---- Combined Trend ----
plt.subplot(2, 2, 4)
plt.plot(days, sales, label="Sales")
plt.plot(days, profit, label="Profit")
plt.plot(days, customers, label="Customers")
plt.legend()
plt.title("Combined Overview")

plt.tight_layout()

plt.show()