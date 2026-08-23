# 02_correlation_hue.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# HUE = CATEGORY COLORING

# --------------------------------------------

# We separate data by gender (sex)

sns.scatterplot(
data=tips,
x="total_bill",
y="tip",
hue="sex"   # male vs female
)

plt.title("Correlation with Gender (Hue)")
plt.show()

# --------------------------------------------

# INSIGHT:

# - You can see if groups behave differently

# --------------------------------------------

# Example idea:

# Do males/females tip differently?

# --------------------------------------------
