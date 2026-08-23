# 06_plot_selection_practice.py

"""
TASKS:

1. Show distribution of value_b → histplot
2. Compare category vs value_c → barplot
3. Relationship between value_a and value_b → scatterplot
4. Correlation matrix → heatmap
   """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("master_revision.csv")

# 1. DISTRIBUTION

sns.histplot(df["value_b"])
plt.show()

# 2. CATEGORY ANALYSIS

sns.barplot(data=df, x="category", y="value_c")
plt.show()

# 3. RELATIONSHIP

sns.scatterplot(data=df, x="value_a", y="value_b")
plt.show()

# 4. CORRELATION

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

# --------------------------------------------

# GOAL:

# - correct plot selection skill

# --------------------------------------------
