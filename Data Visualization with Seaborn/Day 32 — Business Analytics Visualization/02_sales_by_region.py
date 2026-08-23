# 02_sales_by_region.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("business_sales.csv")

# --------------------------------------------

# REGION-WISE SALES

# --------------------------------------------

region_sales = df.groupby("region")["sales"].sum().reset_index()

sns.barplot(
data=region_sales,
x="region",
y="sales"
)

plt.title("Sales by Region")
plt.ylabel("Total Sales")

plt.show()

# --------------------------------------------

# INSIGHT:

# - identify best-performing regions

# --------------------------------------------
