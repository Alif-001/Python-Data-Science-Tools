# 02_countplot_hue.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# HUE = CATEGORY SPLIT

# --------------------------------------------

# We compare smokers vs non-smokers per day

sns.countplot(
data=tips,
x="day",
hue="smoker"
)

plt.title("Smokers vs Non-Smokers per Day")
plt.show()

# --------------------------------------------

# INSIGHT:

# - see group distribution differences

# --------------------------------------------
