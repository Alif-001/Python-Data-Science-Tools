# 01_basic_relplot_scatter.py

# --------------------------------------------

# DAY 5: RELATIONAL PLOT (FIGURE-LEVEL)

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# relplot() = figure-level plotting function

# --------------------------------------------

# It automatically creates a full figure

# and manages layout internally

sns.relplot(
data=tips,
x="total_bill",
y="tip",
kind="scatter"   # scatter plot mode
)

plt.title("Relplot - Scatter Example")
plt.show()

# --------------------------------------------

# KEY IDEA:

# relplot = scatterplot + figure management

# --------------------------------------------
