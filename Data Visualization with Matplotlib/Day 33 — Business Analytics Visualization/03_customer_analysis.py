import pandas as pd
import matplotlib.pyplot as plt

"""
CUSTOMER ANALYSIS
-----------------
We analyze customer growth.
"""

df = pd.read_csv("business_data.csv")

plt.bar(df["day"], df["customers"], color="orange")

plt.title("Customer Growth")
plt.xlabel("Day")
plt.ylabel("Customers")

plt.show()