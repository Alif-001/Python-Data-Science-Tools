# 06_catplot_swarm.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# SWARM PLOT USING CATPLOT

# --------------------------------------------

sns.catplot(
data=tips,
x="day",
y="total_bill",
kind="swarm"
)

plt.title("Catplot - Swarm Plot")
plt.show()

# --------------------------------------------

# IDEA:

# no overlapping points

# --------------------------------------------
