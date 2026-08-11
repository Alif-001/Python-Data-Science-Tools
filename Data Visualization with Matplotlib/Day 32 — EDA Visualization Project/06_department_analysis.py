import pandas as pd
import matplotlib.pyplot as plt

"""
CATEGORY ANALYSIS
-----------------
We analyze departments (categorical data)
"""

df = pd.read_csv("eda_data.csv")

# Count departments
dept_counts = df["department"].value_counts()

plt.bar(dept_counts.index, dept_counts.values, color="orange")

plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")

plt.show()