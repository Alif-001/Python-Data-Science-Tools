# 05_profit_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("business_sales.csv")

# --------------------------------------------

# PROFIT ANALYSIS

# --------------------------------------------

sns.scatterplot(
data=df,
x="sales",
y="profit",
hue="region",
size="orders"
)

plt.title("Sales vs Profit Relationship")
plt.show()

# --------------------------------------------

# INSIGHT:

# - high sales ≠ always high profit

# --------------------------------------------
