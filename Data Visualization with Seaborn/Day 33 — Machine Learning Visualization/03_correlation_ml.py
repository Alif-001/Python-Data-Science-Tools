# 03_correlation_ml.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ml_data.csv")

# --------------------------------------------

# CORRELATION MATRIX

# --------------------------------------------

corr = df.corr()

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

# - see strongest predictors of final score

# --------------------------------------------
