# 01_basic_heatmap.py

# --------------------------------------------

# DAY 20: HEATMAP BASICS

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# WE NEED A MATRIX FOR HEATMAP

# --------------------------------------------

# So we use correlation matrix

corr = tips.corr(numeric_only=True)

# --------------------------------------------

# BASIC HEATMAP

# --------------------------------------------

sns.heatmap(corr)

plt.title("Basic Correlation Heatmap")
plt.show()

# --------------------------------------------

# IDEA:

# - darker/lighter color = strength of relation

# --------------------------------------------
