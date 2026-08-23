# 03_bubble_chart_size_style.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# BUBBLE CHART

# --------------------------------------------

# size = third variable (important concept)

sns.scatterplot(
data=tips,
x="total_bill",
y="tip",
hue="time",     # lunch vs dinner
size="size",    # number of people
sizes=(20, 200)  # control bubble size range
)

plt.title("Bubble Chart: Bill vs Tip vs Group Size")
plt.legend(bbox_to_anchor=(1.05, 1))
plt.show()

# --------------------------------------------

# KEY IDEA:

# - x = input feature

# - y = output feature

# - size = weight / importance

# - hue = category

# --------------------------------------------
