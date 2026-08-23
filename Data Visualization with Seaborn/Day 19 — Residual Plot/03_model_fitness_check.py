# 03_model_fitness_check.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# MODEL FITNESS CHECK

# --------------------------------------------

sns.residplot(
data=tips,
x="total_bill",
y="tip",
lowess=True  # smooth trend of residuals
)

plt.title("Model Fitness Check (LOWESS)")
plt.show()

# --------------------------------------------

# IDEA:

# - smooth curve shows bias patterns

# --------------------------------------------
