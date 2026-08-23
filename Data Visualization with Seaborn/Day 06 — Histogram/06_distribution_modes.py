# 06_distribution_modes.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# ELEMENT TYPES IN HISTOGRAM

# --------------------------------------------

# 1. Bars (default)

sns.histplot(
data=tips,
x="total_bill",
element="bars"
)

plt.title("Bars Mode")
plt.show()

# 2. Step histogram

sns.histplot(
data=tips,
x="total_bill",
element="step"
)

plt.title("Step Mode")
plt.show()

# 3. Filled step (density style)

sns.histplot(
data=tips,
x="total_bill",
element="step",
fill=True
)

plt.title("Filled Step Mode")
plt.show()

# --------------------------------------------

# SUMMARY:

# - bars → normal histogram

# - step → outline style

# - fill → smooth visual

# --------------------------------------------
