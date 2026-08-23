# 07_business_data_quality_dashboard.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_missing.csv")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# MISSING HEATMAP

sns.heatmap(df.isnull(), cbar=False, ax=axes[0])
axes[0].set_title("Missing Data Heatmap")

# MISSING COUNT

missing = df.isnull().sum()
sns.barplot(x=missing.index, y=missing.values, ax=axes[1])
axes[1].set_title("Missing Count")

plt.tight_layout()
plt.show()

# --------------------------------------------

# IDEA:

# - quick data quality report

# --------------------------------------------
