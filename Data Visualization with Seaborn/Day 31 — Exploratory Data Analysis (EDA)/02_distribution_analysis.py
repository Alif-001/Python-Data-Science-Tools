# 02_distribution_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("company_data.csv")

# --------------------------------------------

# DISTRIBUTION OF SALARY

# --------------------------------------------

sns.histplot(
data=df,
x="salary",
kde=True
)

plt.title("Salary Distribution")
plt.show()

# --------------------------------------------

# IDEA:

# - see how values spread

# --------------------------------------------
