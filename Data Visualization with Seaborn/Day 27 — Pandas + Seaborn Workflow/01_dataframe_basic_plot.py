# 01_dataframe_basic_plot.py

# --------------------------------------------

# DAY 27: PANDAS + SEABORN WORKFLOW

# --------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

df = pd.read_csv("sales_eda.csv")

# --------------------------------------------

# DIRECT DATAFRAME PLOTTING

# --------------------------------------------

sns.barplot(
data=df,
x="region",
y="sales"
)

plt.title("Sales by Region")
plt.show()

# --------------------------------------------

# IDEA:

# - no preprocessing needed for simple plots

# --------------------------------------------
