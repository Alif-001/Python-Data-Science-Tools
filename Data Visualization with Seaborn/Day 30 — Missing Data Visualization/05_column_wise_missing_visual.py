# 05_column_wise_missing_visual.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_missing.csv")

missing_ratio = df.isnull().mean() * 100

# --------------------------------------------

# PLOT MISSING PERCENTAGE

# --------------------------------------------

sns.barplot(
x=missing_ratio.index,
y=missing_ratio.values
)

plt.title("Missing Data Percentage per Column")
plt.ylabel("Percentage (%)")
plt.show()

# --------------------------------------------

# IDEA:

# - percentage gives better insight than count

# --------------------------------------------
