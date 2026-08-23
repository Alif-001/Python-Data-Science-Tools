# 05_categorical_scatter_analysis.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CATEGORICAL SCATTER VISUALIZATION

# --------------------------------------------

# x = category (day)

# y = numeric (tip amount)

sns.scatterplot(
data=tips,
x="day",
y="tip",
hue="sex",
style="time",
size="total_bill",
sizes=(20, 200)
)

plt.title("Categorical Scatter Analysis")
plt.show()

# --------------------------------------------

# WHAT YOU LEARN:

# - compare categories visually

# - find patterns in real-world groups

# --------------------------------------------
