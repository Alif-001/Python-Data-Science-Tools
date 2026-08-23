# 05_catplot_strip.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# STRIP PLOT USING CATPLOT

# --------------------------------------------

sns.catplot(
data=tips,
x="day",
y="total_bill",
kind="strip"
)

plt.title("Catplot - Strip Plot")
plt.show()

# --------------------------------------------

# IDEA:

# shows all individual points

# --------------------------------------------
