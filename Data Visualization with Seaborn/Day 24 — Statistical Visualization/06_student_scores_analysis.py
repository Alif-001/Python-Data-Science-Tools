# 06_student_scores_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load custom dataset

df = pd.read_csv("student_scores.csv")

# --------------------------------------------

# MEAN SCORE ANALYSIS

# --------------------------------------------

mean_scores = df[["math", "physics", "chemistry"]].mean()

# --------------------------------------------

# VISUALIZATION

# --------------------------------------------

sns.barplot(x=mean_scores.index, y=mean_scores.values)

plt.title("Average Subject Scores")
plt.show()

# --------------------------------------------

# INSIGHT:

# - which subject is hardest/easiest

# --------------------------------------------
