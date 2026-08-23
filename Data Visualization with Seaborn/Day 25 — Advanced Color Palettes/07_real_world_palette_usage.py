# 07_real_world_palette_usage.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

df = pd.read_csv("product_sales.csv")

# --------------------------------------------

# BUSINESS VISUALIZATION WITH PALETTE

# --------------------------------------------

sns.barplot(
data=df,
x="product",
y="sales",
hue="region",
palette="Set2"
)

plt.title("Product Sales by Region")
plt.show()

# --------------------------------------------

# INSIGHT:

# - each region = different color

# - easy comparison

# --------------------------------------------
