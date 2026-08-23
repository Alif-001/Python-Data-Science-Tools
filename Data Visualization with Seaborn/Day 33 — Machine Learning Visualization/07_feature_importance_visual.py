# 07_feature_importance_visual.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ml_data.csv")

# --------------------------------------------

# CORRELATION WITH TARGET

# --------------------------------------------

corr = df.corr()["final_score"].drop("final_score")

sns.barplot(
x=corr.index,
y=corr.values
)

plt.title("Feature Importance (Correlation-based)")
plt.show()

# --------------------------------------------

# IDEA:

# - shows which feature matters most

# --------------------------------------------
