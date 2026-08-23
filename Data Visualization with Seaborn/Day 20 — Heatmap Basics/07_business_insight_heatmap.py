# 07_business_insight_heatmap.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

# --------------------------------------------

# BUSINESS INSIGHT HEATMAP

# --------------------------------------------

sns.heatmap(
corr,
annot=True,
cmap="vlag",
center=0
)

plt.title("Business Correlation Insight")
plt.show()

# --------------------------------------------

# INSIGHT:

# - detect strong relationships

# - useful for decision making

# --------------------------------------------
