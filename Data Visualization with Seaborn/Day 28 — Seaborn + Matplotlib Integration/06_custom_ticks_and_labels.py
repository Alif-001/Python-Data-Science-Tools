# 06_custom_ticks_and_labels.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.boxplot(
data=tips,
x="day",
y="total_bill"
)

# --------------------------------------------

# CUSTOM AXIS CONTROL

# --------------------------------------------

plt.xticks(rotation=45)
plt.yticks([10, 20, 30, 40])

plt.xlabel("Days of Week")
plt.ylabel("Total Bill ($)")
plt.title("Custom Axis Control")

plt.show()

# --------------------------------------------

# IDEA:

# - full control of axes

# --------------------------------------------
