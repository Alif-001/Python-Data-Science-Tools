# 08_final_master_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(8, 6))

sns.scatterplot(
data=tips,
x="total_bill",
y="tip",
hue="sex",
style="time",
s=100
)

# --------------------------------------------

# FINAL POLISHING

# --------------------------------------------

plt.title("Final Professional Data Visualization", fontsize=18)
plt.xlabel("Total Bill Amount", fontsize=12)
plt.ylabel("Tip Amount", fontsize=12)

plt.legend(title="Category", loc="best")

plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()

plt.show()

# --------------------------------------------

# GOAL:

# - portfolio-ready visualization

# --------------------------------------------
