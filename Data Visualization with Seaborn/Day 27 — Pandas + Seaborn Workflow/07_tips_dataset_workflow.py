# 07_tips_dataset_workflow.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# GROUP ANALYSIS

# --------------------------------------------

sns.barplot(data=tips, x="day", y="total_bill")
plt.show()

# --------------------------------------------

# RELATIONSHIP ANALYSIS

# --------------------------------------------

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.show()

# --------------------------------------------

# DISTRIBUTION ANALYSIS

# --------------------------------------------

sns.histplot(data=tips, x="total_bill", kde=True)
plt.show()

# --------------------------------------------

# COMPLETE EDA IN ONE DATASET

# --------------------------------------------
