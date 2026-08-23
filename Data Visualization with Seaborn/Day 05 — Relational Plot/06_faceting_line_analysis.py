# 06_faceting_line_analysis.py

import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

# --------------------------------------------

# FACETING + LINE PLOT

# --------------------------------------------

sns.relplot(
data=flights,
x="year",
y="passengers",
hue="month",
col="month",   # one plot per month
kind="line",
col_wrap=4     # wrap layout
)

plt.show()

# --------------------------------------------

# INSIGHT:

# You can compare trends month-by-month

# --------------------------------------------
