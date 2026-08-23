# 06_publication_style_plot.py

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
s=80
)

# --------------------------------------------

# PROFESSIONAL CUSTOMIZATION

# --------------------------------------------

plt.title("Publication-Style Analysis Plot", fontsize=16)
plt.xlabel("Total Bill ($)", fontsize=12)
plt.ylabel("Tip ($)", fontsize=12)

plt.legend(title="Categories")
plt.grid(True, linestyle="--", alpha=0.5)

plt.show()

# --------------------------------------------

# RESULT:

# - clean + readable + report ready

# --------------------------------------------
