# 04_catplot_violin.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# VIOLIN PLOT USING CATPLOT

# --------------------------------------------

sns.catplot(
data=tips,
x="day",
y="total_bill",
kind="violin"
)

plt.title("Catplot - Violin Plot")
plt.show()

# --------------------------------------------

# IDEA:

# shows distribution shape

# --------------------------------------------
