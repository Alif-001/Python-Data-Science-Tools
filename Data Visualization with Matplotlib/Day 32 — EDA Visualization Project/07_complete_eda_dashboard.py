import pandas as pd
import matplotlib.pyplot as plt

"""
COMPLETE EDA DASHBOARD
----------------------
All analysis in one view
"""

df = pd.read_csv("eda_data.csv")

fig = plt.figure(figsize=(12, 8))

# ---- Distribution ----
plt.subplot(2, 2, 1)
plt.hist(df["salary"], color="blue")
plt.title("Salary Distribution")

# ---- Correlation insight ----
plt.subplot(2, 2, 2)
plt.scatter(df["experience"], df["salary"], color="green")
plt.title("Experience vs Salary")

# ---- Boxplot ----
plt.subplot(2, 2, 3)
plt.boxplot(df["score"])
plt.title("Score Outliers")

# ---- Department ----
plt.subplot(2, 2, 4)
df["department"].value_counts().plot(kind="bar", color="purple")
plt.title("Department Count")

plt.tight_layout()
plt.show()