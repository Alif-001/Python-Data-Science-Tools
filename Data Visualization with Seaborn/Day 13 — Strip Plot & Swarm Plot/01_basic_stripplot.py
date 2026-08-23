# 01_basic_stripplot.py

# --------------------------------------------

# DAY 13: STRIP PLOT

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# STRIP PLOT = individual data points

# --------------------------------------------

sns.stripplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Strip Plot: All Data Points per Day")
plt.show()

# --------------------------------------------

# IDEA:

# - each dot = one customer

# - shows full raw distribution

# --------------------------------------------
