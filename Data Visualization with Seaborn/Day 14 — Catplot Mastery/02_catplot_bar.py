# 02_catplot_bar.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# BAR PLOT USING CATPLOT

# --------------------------------------------

sns.catplot(
data=tips,
x="day",
y="total_bill",
kind="bar"
)

plt.title("Catplot - Bar Plot (Mean Values)")
plt.show()

# --------------------------------------------

# IDEA:

# shows average value per category

# --------------------------------------------
