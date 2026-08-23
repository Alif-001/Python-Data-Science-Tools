# 06_real_world_missing_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_missing.csv")

# --------------------------------------------

# STEP 1: HEATMAP OF MISSING DATA

# --------------------------------------------

plt.figure(figsize=(6, 4))
sns.heatmap(df.isnull(), cbar=False, cmap="coolwarm")
plt.title("Missing Data Pattern")
plt.show()

# --------------------------------------------

# STEP 2: COLUMN ANALYSIS

# --------------------------------------------

missing = df.isnull().sum()

sns.barplot(x=missing.index, y=missing.values)
plt.title("Missing Count Analysis")
plt.show()

# --------------------------------------------

# IDEA:

# - combine multiple views for insight

# --------------------------------------------
