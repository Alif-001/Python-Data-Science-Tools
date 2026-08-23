# 03_multiple_histograms.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# MULTIPLE DISTRIBUTIONS

# --------------------------------------------

# Compare smokers vs non-smokers

sns.histplot(
data=tips,
x="total_bill",
hue="smoker"
)

plt.title("Smoker vs Non-Smoker Bill Distribution")
plt.show()

# --------------------------------------------

# INSIGHT:

# You can compare groups easily

# --------------------------------------------
