# 04_advanced_annotation.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
data=tips,
x="total_bill",
y="tip"
)

# --------------------------------------------

# ADD ANNOTATION USING MATPLOTLIB

# --------------------------------------------

plt.text(
30, 6,
"High Bill High Tip Zone",
fontsize=10,
color="red"
)

plt.title("Scatter with Annotation")
plt.show()

# --------------------------------------------

# IDEA:

# - highlight important region

# --------------------------------------------
