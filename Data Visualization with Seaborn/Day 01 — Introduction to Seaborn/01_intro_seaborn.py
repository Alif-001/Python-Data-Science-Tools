# 01_intro_seaborn.py

# --------------------------------------------

# DAY 1: INTRODUCTION TO SEABORN

# --------------------------------------------

# Seaborn is a Python data visualization library

# built on top of Matplotlib.

# It makes statistical plots easier and prettier.

import seaborn as sns   # main library for Seaborn
import matplotlib.pyplot as plt  # base plotting library

# --------------------------------------------

# Why Seaborn?

# --------------------------------------------

# - Easier syntax than Matplotlib

# - Beautiful default styles

# - Works well with Pandas DataFrames

# - Built-in datasets for practice

# --------------------------------------------

# Load built-in dataset

# --------------------------------------------

# Seaborn has built-in datasets for practice

tips = sns.load_dataset("tips")

# tips dataset columns:

# total_bill, tip, sex, smoker, day, time, size

print(tips.head())  # check first 5 rows

# --------------------------------------------

# Theme setup (styling)

# --------------------------------------------

sns.set_theme(style="darkgrid")

# Available styles:

# darkgrid, whitegrid, dark, white, ticks

# --------------------------------------------

# First simple plot (just preview)

# --------------------------------------------

sns.histplot(data=tips, x="total_bill")

plt.title("Distribution of Total Bill")
plt.show()

# --------------------------------------------

# END OF FILE

# --------------------------------------------
