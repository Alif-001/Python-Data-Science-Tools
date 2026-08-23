# 07_advanced_business_insights.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("business_sales.csv")

# --------------------------------------------

# PRODUCT PERFORMANCE

# --------------------------------------------

sns.barplot(
data=df,
x="product",
y="sales",
hue="region"
)

plt.title("Product Performance by Region")
plt.show()

# --------------------------------------------

# INSIGHT:

# - best product per region

# --------------------------------------------
