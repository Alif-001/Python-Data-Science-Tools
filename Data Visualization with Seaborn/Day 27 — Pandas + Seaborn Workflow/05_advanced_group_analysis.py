# 05_advanced_group_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_eda.csv")

# --------------------------------------------

# MULTI GROUP ANALYSIS

# --------------------------------------------

sns.barplot(
data=df,
x="region",
y="profit",
hue="product"
)

plt.title("Profit by Region and Product")
plt.show()

# --------------------------------------------

# IDEA:

# - deeper segmentation

# --------------------------------------------
