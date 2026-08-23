# 04_outlier_detection_boxplot.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("company_data.csv")

# --------------------------------------------

# BOXPLOT FOR OUTLIERS

# --------------------------------------------

sns.boxplot(
data=df,
y="salary"
)

plt.title("Salary Outlier Detection")
plt.show()

# --------------------------------------------

# IDEA:

# - points outside whiskers = outliers

# --------------------------------------------
