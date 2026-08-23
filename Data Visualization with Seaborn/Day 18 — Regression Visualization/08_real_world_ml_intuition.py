# 08_real_world_ml_intuition.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REAL-WORLD REGRESSION INSIGHT

# --------------------------------------------

sns.lmplot(
data=tips,
x="total_bill",
y="tip",
hue="smoker"
)

plt.title("ML Style Regression Insight")
plt.show()

# --------------------------------------------

# INSIGHT:

# - relationship strength

# - group differences

# - prediction trend

# --------------------------------------------
