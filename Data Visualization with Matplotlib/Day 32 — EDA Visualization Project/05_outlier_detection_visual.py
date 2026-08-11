import pandas as pd
import matplotlib.pyplot as plt

"""
OUTLIER ANALYSIS
----------------
Outliers = unusual/extreme values in data
"""

df = pd.read_csv("eda_data.csv")

plt.figure(figsize=(10, 5))

# Boxplot for salary
plt.subplot(1, 2, 1)
plt.boxplot(df["salary"])
plt.title("Salary Outlier Detection")

# Boxplot for score
plt.subplot(1, 2, 2)
plt.boxplot(df["score"])
plt.title("Score Outlier Detection")

plt.tight_layout()
plt.show()