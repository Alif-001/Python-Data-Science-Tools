# 01_basic_integration.py

# --------------------------------------------

# DAY 28: SEABORN + MATPLOTLIB INTEGRATION

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# SEABORN PLOT

# --------------------------------------------

sns.scatterplot(
data=tips,
x="total_bill",
y="tip",
hue="sex"
)

# --------------------------------------------

# MATPLOTLIB CUSTOMIZATION

# --------------------------------------------

plt.title("Seaborn + Matplotlib Integration")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.show()

# --------------------------------------------

# IDEA:

# - seaborn = plot

# - matplotlib = styling

# --------------------------------------------
