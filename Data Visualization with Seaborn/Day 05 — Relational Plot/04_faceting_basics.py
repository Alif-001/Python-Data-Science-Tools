# 04_faceting_basics.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# FACETING = SPLITTING INTO MULTIPLE PLOTS

# --------------------------------------------

sns.relplot(
data=tips,
x="total_bill",
y="tip",
col="sex"   # split by gender
)

plt.show()

# --------------------------------------------

# RESULT:

# - one plot for male

# - one plot for female

# --------------------------------------------

# This helps compare groups visually

# --------------------------------------------
