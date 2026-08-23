# 07_real_world_eda_report.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("company_data.csv")

# --------------------------------------------

# STEP 1: OVERVIEW

# --------------------------------------------

print(df.describe())

# --------------------------------------------

# STEP 2: CORRELATION

# --------------------------------------------

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Analysis")
plt.show()

# --------------------------------------------

# STEP 3: DISTRIBUTION

# --------------------------------------------

sns.histplot(df["salary"], kde=True)
plt.title("Salary Distribution")
plt.show()

# --------------------------------------------

# STEP 4: OUTLIERS

# --------------------------------------------

sns.boxplot(y=df["salary"])
plt.title("Outlier Detection")
plt.show()

# --------------------------------------------

# FINAL INSIGHT:

# - full EDA pipeline

# --------------------------------------------
