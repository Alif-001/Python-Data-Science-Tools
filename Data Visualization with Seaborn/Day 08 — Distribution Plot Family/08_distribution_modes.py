# 08_distribution_modes.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# DIFFERENT ELEMENT TYPES

# --------------------------------------------

# 1. Histogram style

sns.displot(
data=tips,
x="total_bill",
element="bars"
)
plt.title("Bars Style")
plt.show()

# 2. Step style

sns.displot(
data=tips,
x="total_bill",
element="step"
)
plt.title("Step Style")
plt.show()

# 3. Filled step

sns.displot(
data=tips,
x="total_bill",
element="step",
fill=True
)
plt.title("Filled Step Style")
plt.show()

# --------------------------------------------

# STYLE CONTROL FOR DISTRIBUTIONS

# --------------------------------------------
