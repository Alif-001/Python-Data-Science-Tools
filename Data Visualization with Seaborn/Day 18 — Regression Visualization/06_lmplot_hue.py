# 06_lmplot_hue.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# GROUPED REGRESSION

# --------------------------------------------

sns.lmplot(
data=tips,
x="total_bill",
y="tip",
hue="sex"
)

plt.title("Regression by Gender")
plt.show()

# --------------------------------------------

# IDEA:

# - separate trend lines per group

# --------------------------------------------
