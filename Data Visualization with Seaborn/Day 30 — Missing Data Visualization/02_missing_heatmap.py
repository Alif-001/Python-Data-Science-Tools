# 02_missing_heatmap.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_missing.csv")

# --------------------------------------------

# MISSING VALUE HEATMAP

# --------------------------------------------

sns.heatmap(
df.isnull(),
cbar=False,
cmap="viridis"
)

plt.title("Missing Data Heatmap")
plt.show()

# --------------------------------------------

# IDEA:

# - yellow/bright = missing values

# - dark = available data

# --------------------------------------------
