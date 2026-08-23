# 04_annotation_example.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
data=tips,
x="total_bill",
y="tip"
)

# --------------------------------------------

# ANNOTATION (HIGHLIGHT INSIGHT)

# --------------------------------------------

plt.text(
30, 6,
"High spending customers",
fontsize=10,
color="red"
)

plt.title("Scatter Plot with Annotation")

plt.show()

# --------------------------------------------

# IDEA:

# - highlight important region

# --------------------------------------------
