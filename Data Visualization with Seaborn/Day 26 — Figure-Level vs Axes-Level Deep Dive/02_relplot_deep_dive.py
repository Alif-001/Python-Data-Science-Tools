# 02_relplot_deep_dive.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# RELPLOT = FIGURE-LEVEL RELATIONAL PLOT

# --------------------------------------------

sns.relplot(
data=tips,
x="total_bill",
y="tip",
hue="sex"
)

# NOTE: no plt.title needed (figure-level handles it)

plt.show()

# --------------------------------------------

# IDEA:

# - automatic styling

# - supports faceting

# --------------------------------------------
