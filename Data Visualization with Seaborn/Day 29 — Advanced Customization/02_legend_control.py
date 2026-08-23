# 02_legend_control.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
data=tips,
x="total_bill",
y="tip",
hue="sex"
)

# --------------------------------------------

# LEGEND CONTROL

# --------------------------------------------

plt.legend(
title="Gender",
loc="upper left"
)

plt.title("Legend Customization Example")

plt.show()

# --------------------------------------------

# IDEA:

# - legend explains categories

# --------------------------------------------
