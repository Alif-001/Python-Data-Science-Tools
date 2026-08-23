# 08_professional_final_plot.py

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

plt.title("Professional Seaborn + Matplotlib Plot")
plt.xlabel("Total Bill")
plt.ylabel("Tip Amount")

plt.grid(True)

plt.show()

# --------------------------------------------

# FINAL GOAL:

# - clean + readable + styled plot

# --------------------------------------------
