# 01_basic_histogram.py

# --------------------------------------------

# DAY 6: HISTOGRAM (FREQUENCY DISTRIBUTION)

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# BASIC HISTOGRAM

# --------------------------------------------

# We analyze how total_bill values are distributed

sns.histplot(
data=tips,
x="total_bill"
)

plt.title("Distribution of Total Bill")
plt.show()

# --------------------------------------------

# KEY IDEA:

# Histogram shows how often values occur

# --------------------------------------------
