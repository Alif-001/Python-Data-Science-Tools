# 07_real_world_storytelling.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# FULL STATISTICAL STORY

# --------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(data=tips, x="day", y="total_bill")
sns.stripplot(data=tips, x="day", y="total_bill", color="black", alpha=0.4)

plt.title("Statistical Storytelling (Box + Points)")
plt.show()

# --------------------------------------------

# INSIGHT:

# - box = summary

# - points = real data

# --------------------------------------------
