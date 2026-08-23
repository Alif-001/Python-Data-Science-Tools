# 02_multi_feature_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ml_data.csv")

# --------------------------------------------

# MULTI FEATURE ANALYSIS

# --------------------------------------------

sns.scatterplot(
data=df,
x="attendance",
y="final_score",
hue="study_hours",
size="previous_score"
)

plt.title("Attendance vs Final Score")
plt.show()

# --------------------------------------------

# IDEA:

# - multiple factors affect target

# --------------------------------------------
