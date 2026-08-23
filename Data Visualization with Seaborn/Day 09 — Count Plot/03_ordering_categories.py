# 03_ordering_categories.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# ORDERING CATEGORIES

# --------------------------------------------

# By default order may be alphabetical

# We control it manually

sns.countplot(
data=tips,
x="day",
order=["Thur", "Fri", "Sat", "Sun"]
)

plt.title("Ordered Days Count")
plt.show()

# --------------------------------------------

# WHY IMPORTANT?

# - better storytelling

# - logical ordering instead of random

# --------------------------------------------
