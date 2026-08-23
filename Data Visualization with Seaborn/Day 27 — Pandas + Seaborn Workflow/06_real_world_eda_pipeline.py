# 06_real_world_eda_pipeline.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_eda.csv")

# --------------------------------------------

# STEP 1: BASIC OVERVIEW

# --------------------------------------------

print(df.head())

# --------------------------------------------

# STEP 2: GROUP ANALYSIS

# --------------------------------------------

grouped = df.groupby("region")["sales"].mean().reset_index()

sns.barplot(data=grouped, x="region", y="sales")
plt.title("Average Sales by Region")
plt.show()

# --------------------------------------------

# STEP 3: RELATIONSHIP ANALYSIS

# --------------------------------------------

sns.scatterplot(data=df, x="sales", y="profit", hue="region")
plt.title("Sales vs Profit")
plt.show()

# --------------------------------------------

# FULL EDA PIPELINE COMPLETE

# --------------------------------------------
