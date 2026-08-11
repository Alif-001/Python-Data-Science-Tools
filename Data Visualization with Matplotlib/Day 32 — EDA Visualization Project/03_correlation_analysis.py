import pandas as pd
import matplotlib.pyplot as plt

"""
CORRELATION ANALYSIS
--------------------
Find relationship between variables.
"""

df = pd.read_csv("eda_data.csv")

# Select numeric columns
numeric_df = df[["age", "salary", "experience", "score"]]

# Correlation matrix
corr = numeric_df.corr()

plt.imshow(corr, cmap="coolwarm")

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap")

plt.show()