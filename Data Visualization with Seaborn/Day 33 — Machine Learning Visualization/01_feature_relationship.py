# 01_feature_relationship.py

# --------------------------------------------

# DAY 33: MACHINE LEARNING VISUALIZATION

# --------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ml_data.csv")

# --------------------------------------------

# FEATURE vs TARGET ANALYSIS

# --------------------------------------------

sns.scatterplot(
data=df,
x="study_hours",
y="final_score"
)

plt.title("Study Hours vs Final Score")
plt.show()

# --------------------------------------------

# IDEA:

# - more study → better score

# --------------------------------------------
