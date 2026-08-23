# 08_advanced_palette_story.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# ADVANCED COLOR STORY

# --------------------------------------------

sns.boxplot(
data=tips,
x="day",
y="total_bill",
palette="coolwarm"
)

plt.title("Statistical Story with Diverging Colors")
plt.show()

# --------------------------------------------

# IDEA:

# - colors show intensity differences

# --------------------------------------------
