# 03_swarmplot_basic.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# SWARM PLOT

# --------------------------------------------

# Automatically avoids overlapping points

sns.swarmplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Swarm Plot: Clean Point Distribution")
plt.show()

# --------------------------------------------

# IDEA:

# - better than stripplot for clarity

# - but slower for big data

# --------------------------------------------
