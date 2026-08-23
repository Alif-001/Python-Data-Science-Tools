# 06_business_insight_heatmap.py

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
cmap="YlGnBu",
center=0
)

plt.title("Business Insight Heatmap")
plt.show()

# --------------------------------------------

# INSIGHT:

# - identify revenue-driving factors

# --------------------------------------------
