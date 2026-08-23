# 01_basic_pairplot.py

# --------------------------------------------

# DAY 16: PAIR PLOT (MULTIVARIABLE ANALYSIS)

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

iris = sns.load_dataset("iris")

# --------------------------------------------

# PAIRPLOT

# --------------------------------------------

# Shows relationship between ALL numeric columns

sns.pairplot(iris)

plt.show()

# --------------------------------------------

# IDEA:

# every variable vs every variable

# --------------------------------------------
