# 05_relationship_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("company_data.csv")

# --------------------------------------------

# EXPERIENCE VS SALARY

# --------------------------------------------

sns.scatterplot(
data=df,
x="experience",
y="salary",
hue="performance",
size="projects"
)

plt.title("Experience vs Salary Relationship")
plt.show()

# --------------------------------------------

# IDEA:

# - multiple variables in one plot

# --------------------------------------------
