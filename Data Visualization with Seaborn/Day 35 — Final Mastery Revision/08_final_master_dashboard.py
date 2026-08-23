# 08_final_master_dashboard.py

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# DISTRIBUTION

sns.histplot(df["total_bill"], kde=True, ax=axes[0,0])
axes[0,0].set_title("Distribution")

# RELATIONSHIP

sns.scatterplot(data=df, x="total_bill", y="tip", ax=axes[0,1])
axes[0,1].set_title("Relationship")

# CATEGORICAL

sns.boxplot(data=df, x="day", y="total_bill", ax=axes[1,0])
axes[1,0].set_title("Categorical Analysis")

# HEATMAP

sns.heatmap(df.corr(numeric_only=True), annot=True, ax=axes[1,1])
axes[1,1].set_title("Correlation")

plt.tight_layout()
plt.show()

# --------------------------------------------

# FINAL RESULT:

# - complete revision in one dashboard

# --------------------------------------------
