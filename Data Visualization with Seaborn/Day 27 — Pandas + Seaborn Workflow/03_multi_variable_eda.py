# 03_multi_variable_eda.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_eda.csv")

# --------------------------------------------

# MULTI VARIABLE ANALYSIS

# --------------------------------------------

sns.scatterplot(
data=df,
x="sales",
y="profit",
hue="region"
)

plt.title("Sales vs Profit by Region")
plt.show()

# --------------------------------------------

# IDEA:

# - relationship + category insight

# --------------------------------------------
