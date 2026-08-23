# 05_revision_with_custom_data.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("master_revision.csv")

# --------------------------------------------

# DISTRIBUTION STYLE

# --------------------------------------------

sns.histplot(df["value_a"], kde=True)
plt.title("Distribution of Value A")
plt.show()

# --------------------------------------------

# RELATIONSHIP

# --------------------------------------------

sns.scatterplot(data=df, x="value_a", y="value_b", hue="category")
plt.title("Relationship Plot")
plt.show()

# --------------------------------------------

# CATEGORICAL ANALYSIS

# --------------------------------------------

sns.barplot(data=df, x="category", y="value_c")
plt.title("Category Analysis")
plt.show()

# --------------------------------------------

# IDEA:

# - apply all knowledge on new data

# --------------------------------------------
