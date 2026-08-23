# 02_violin_vs_box.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# BOX PLOT VS VIOLIN PLOT

# --------------------------------------------

plt.figure(figsize=(10, 5))

# Box plot (summary)

sns.boxplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Box Plot (Summary)")
plt.show()

# Violin plot (full distribution)

sns.violinplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Violin Plot (Full Distribution)")
plt.show()

# --------------------------------------------

# KEY IDEA:

# box = summary only

# violin = full shape

# --------------------------------------------
