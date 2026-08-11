import pandas as pd
import matplotlib.pyplot as plt

"""
DISTRIBUTION ANALYSIS
---------------------
We understand how data is spread.
"""

df = pd.read_csv("eda_data.csv")

plt.figure(figsize=(10, 5))

# Salary distribution
plt.subplot(1, 2, 1)
plt.hist(df["salary"], bins=5, color="blue", edgecolor="black")
plt.title("Salary Distribution")

# Score distribution
plt.subplot(1, 2, 2)
plt.hist(df["score"], bins=5, color="green", edgecolor="black")
plt.title("Score Distribution")

plt.tight_layout()
plt.show()