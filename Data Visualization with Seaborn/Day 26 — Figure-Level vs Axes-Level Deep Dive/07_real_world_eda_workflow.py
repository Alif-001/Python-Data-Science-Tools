# 07_real_world_eda_workflow.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# STEP 1: DISTRIBUTION

# --------------------------------------------

sns.displot(tips, x="total_bill", kde=True)
plt.show()

# --------------------------------------------

# STEP 2: RELATIONSHIP

# --------------------------------------------

sns.relplot(data=tips, x="total_bill", y="tip")
plt.show()

# --------------------------------------------

# STEP 3: CATEGORY ANALYSIS

# --------------------------------------------

sns.catplot(data=tips, x="day", y="total_bill", kind="box")
plt.show()

# --------------------------------------------

# IDEA:

# - full analysis pipeline

# --------------------------------------------
