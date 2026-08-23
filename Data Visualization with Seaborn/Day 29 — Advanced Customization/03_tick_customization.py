# 03_tick_customization.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.boxplot(
data=tips,
x="day",
y="total_bill"
)

# --------------------------------------------

# TICK CUSTOMIZATION

# --------------------------------------------

plt.xticks(rotation=45)  # rotate x labels
plt.yticks([10, 20, 30, 40, 50])  # custom scale

plt.title("Tick Customization Example")

plt.show()

# --------------------------------------------

# IDEA:

# - improve readability

# --------------------------------------------
