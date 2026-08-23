# 06_faceted_distribution.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# FACETED DISTRIBUTION

# --------------------------------------------

sns.displot(
data=tips,
x="total_bill",
col="sex"   # split into columns
)

plt.show()

# --------------------------------------------

# RESULT:

# - separate plot for male

# - separate plot for female

# --------------------------------------------
