# 02_groupby_visualization.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_eda.csv")

# --------------------------------------------

# GROUPBY ANALYSIS

# --------------------------------------------

grouped = df.groupby("product")["sales"].mean().reset_index()

# --------------------------------------------

# VISUALIZATION

# --------------------------------------------

sns.barplot(
data=grouped,
x="product",
y="sales"
)

plt.title("Average Sales by Product")
plt.show()

# --------------------------------------------

# IDEA:

# - summarize first, then plot

# --------------------------------------------
