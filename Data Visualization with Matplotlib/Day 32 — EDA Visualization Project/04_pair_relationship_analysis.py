import pandas as pd
import matplotlib.pyplot as plt

"""
PAIR RELATIONSHIP ANALYSIS
--------------------------
We compare two variables at a time.
"""

df = pd.read_csv("eda_data.csv")

plt.figure(figsize=(10, 5))

# Salary vs Experience
plt.subplot(1, 2, 1)
plt.scatter(df["experience"], df["salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

# Age vs Score
plt.subplot(1, 2, 2)
plt.scatter(df["age"], df["score"])
plt.title("Age vs Score")
plt.xlabel("Age")
plt.ylabel("Score")

plt.tight_layout()
plt.show()