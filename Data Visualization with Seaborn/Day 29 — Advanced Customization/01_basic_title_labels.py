# 01_basic_title_labels.py

# --------------------------------------------

# DAY 29: ADVANCED CUSTOMIZATION

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
data=tips,
x="total_bill",
y="tip",
hue="sex"
)

# --------------------------------------------

# TITLE + LABELS

# --------------------------------------------

plt.title("Relationship Between Bill and Tip", fontsize=14)
plt.xlabel("Total Bill Amount ($)", fontsize=12)
plt.ylabel("Tip Amount ($)", fontsize=12)

plt.show()

# --------------------------------------------

# IDEA:

# - labels = explain axes

# - title = story of plot

# --------------------------------------------
