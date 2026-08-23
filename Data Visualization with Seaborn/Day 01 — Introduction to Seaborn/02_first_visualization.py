# 02_first_visualization.py

# --------------------------------------------

# FIRST REAL SEABORN VISUALIZATION

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset again

tips = sns.load_dataset("tips")

# Set theme for better visuals

sns.set_theme(style="whitegrid")

# --------------------------------------------

# Simple Scatter Plot

# --------------------------------------------

# We compare total bill vs tip

sns.scatterplot(
data=tips,
x="total_bill",
y="tip",
hue="sex"   # different colors for male/female
)

plt.title("Total Bill vs Tip")
plt.show()

# --------------------------------------------

# SEABORN vs MATPLOTLIB idea

# --------------------------------------------

# Matplotlib (manual way):

# - You need to control every detail manually

# - More code

# Seaborn:

# - Less code

# - Better default styling

# - Built-in statistical understanding

# Example idea:

# Matplotlib → you draw everything manually

# Seaborn → you describe what you want

# --------------------------------------------

# END OF FILE

# --------------------------------------------
