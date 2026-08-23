# 03_filled_kde.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# FILLED KDE PLOT

# --------------------------------------------

sns.kdeplot(
data=tips,
x="total_bill",
fill=True   # fills area under curve
)

plt.title("Filled KDE Plot")
plt.show()

# --------------------------------------------

# WHY USE FILL?

# - easier visual understanding

# - looks like smooth histogram

# --------------------------------------------
