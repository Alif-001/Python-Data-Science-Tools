# 03_catplot_box.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# BOX PLOT USING CATPLOT

# --------------------------------------------

sns.catplot(
data=tips,
x="day",
y="total_bill",
kind="box"
)

plt.title("Catplot - Box Plot")
plt.show()

# --------------------------------------------

# IDEA:

# shows quartiles + outliers

# --------------------------------------------
