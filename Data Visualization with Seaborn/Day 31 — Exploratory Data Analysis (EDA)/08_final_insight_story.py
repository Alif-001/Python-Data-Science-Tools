# 08_final_insight_story.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("company_data.csv")

# --------------------------------------------

# FINAL INSIGHT VISUALIZATION

# --------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
data=df,
x="experience",
y="salary",
hue="performance",
size="projects"
)

plt.title("Final EDA Insight: Salary Growth Pattern")
plt.grid(True)

plt.show()

# --------------------------------------------

# INSIGHT:

# - experience strongly impacts salary

# - performance also matters

# --------------------------------------------
