# 03_correlation_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("company_data.csv")

# --------------------------------------------

# CORRELATION MATRIX

# --------------------------------------------

corr = df.corr(numeric_only=True)

# --------------------------------------------

# HEATMAP VISUALIZATION

# --------------------------------------------

sns.heatmap(
corr,
annot=True,
cmap="coolwarm",
center=0
)

plt.title("Feature Correlation Heatmap")
plt.show()

# --------------------------------------------

# IDEA:

# - salary relation with experience, performance

# --------------------------------------------
