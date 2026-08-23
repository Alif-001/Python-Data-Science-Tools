# 04_strip_vs_swarm.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# COMPARISON: STRIP vs SWARM

# --------------------------------------------

plt.figure(figsize=(10, 4))

# Strip plot (fast, may overlap)

plt.subplot(1, 2, 1)
sns.stripplot(data=tips, x="day", y="total_bill")
plt.title("Strip Plot")

# Swarm plot (clean, no overlap)

plt.subplot(1, 2, 2)
sns.swarmplot(data=tips, x="day", y="total_bill")
plt.title("Swarm Plot")

plt.tight_layout()
plt.show()

# --------------------------------------------

# IDEA:

# strip = speed

# swarm = clarity

# --------------------------------------------
