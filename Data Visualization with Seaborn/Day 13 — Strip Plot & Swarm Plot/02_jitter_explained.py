# 02_jitter_explained.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# PROBLEM: overlapping points

# SOLUTION: jitter

# --------------------------------------------

# Without jitter (hard to see data)

sns.stripplot(
data=tips,
x="day",
y="total_bill",
jitter=False
)

plt.title("No Jitter (Overlapping Points)")
plt.show()

# With jitter (spread points slightly)

sns.stripplot(
data=tips,
x="day",
y="total_bill",
jitter=True
)

plt.title("With Jitter (Clear View)")
plt.show()

# --------------------------------------------

# IDEA:

# jitter = small random movement

# makes overlapping data visible

# --------------------------------------------
