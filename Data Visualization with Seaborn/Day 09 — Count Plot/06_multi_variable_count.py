# 06_multi_variable_count.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# MULTI-VARIABLE COUNT ANALYSIS

# --------------------------------------------

sns.countplot(
data=tips,
x="day",
hue="sex"
)

plt.title("Day-wise Gender Count")
plt.show()

# --------------------------------------------

# INSIGHT:

# - compare multiple categories at once

# --------------------------------------------
