# 01_basic_countplot.py

# --------------------------------------------

# DAY 9: COUNT PLOT (CATEGORY FREQUENCY)

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# BASIC COUNT PLOT

# --------------------------------------------

# It counts how many rows exist in each category

sns.countplot(
data=tips,
x="day"
)

plt.title("Count of Customers per Day")
plt.show()

# --------------------------------------------

# IDEA:

# - each bar = number of observations

# - no need to manually count

# --------------------------------------------
