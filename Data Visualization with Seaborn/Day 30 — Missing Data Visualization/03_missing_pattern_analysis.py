# 03_missing_pattern_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_missing.csv")

# --------------------------------------------

# COUNT MISSING VALUES

# --------------------------------------------

missing_counts = df.isnull().sum()

# --------------------------------------------

# VISUALIZE MISSING PATTERN

# --------------------------------------------

sns.barplot(
x=missing_counts.index,
y=missing_counts.values
)

plt.title("Missing Values per Column")
plt.ylabel("Count of Missing Values")
plt.show()

# --------------------------------------------

# IDEA:

# - shows which feature is most incomplete

# --------------------------------------------
