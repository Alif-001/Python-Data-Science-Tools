import pandas as pd
import matplotlib.pyplot as plt

"""
REGION-WISE BUSINESS ANALYSIS
-----------------------------
We analyze performance by region.
"""

df = pd.read_csv("business_data.csv")

region_sales = df.groupby("region")["sales"].sum()

plt.bar(region_sales.index, region_sales.values, color="purple")

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.show()