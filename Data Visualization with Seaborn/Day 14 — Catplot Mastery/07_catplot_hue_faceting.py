# 07_catplot_hue_faceting.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CATPLOT WITH HUE + FACETING

# --------------------------------------------

sns.catplot(
data=tips,
x="day",
y="total_bill",
hue="sex",
col="time",
kind="box"
)

plt.show()

# --------------------------------------------

# INSIGHT:

# - time split (lunch/dinner)

# - gender comparison inside each group

# --------------------------------------------
