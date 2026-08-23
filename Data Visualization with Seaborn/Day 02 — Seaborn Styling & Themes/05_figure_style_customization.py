# 05_figure_style_customization.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CUSTOM FIGURE STYLING

# --------------------------------------------

sns.set_theme(
style="whitegrid",
palette="pastel",
font_scale=1.3
)

# Create figure manually for more control

plt.figure(figsize=(10, 6))  # width, height

sns.scatterplot(
data=tips,
x="total_bill",
y="tip",
hue="time"
)

# --------------------------------------------

# Customize plot manually (Matplotlib integration)

# --------------------------------------------

plt.title("Customized Figure Styling", fontsize=16)
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")

plt.legend(title="Time of Day")

plt.tight_layout()  # prevents overlap
plt.show()

# --------------------------------------------

# END OF DAY 2

# --------------------------------------------
