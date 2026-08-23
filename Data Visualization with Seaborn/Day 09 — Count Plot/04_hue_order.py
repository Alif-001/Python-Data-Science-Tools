# 04_hue_order.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CONTROL HUE ORDER

# --------------------------------------------

sns.countplot(
data=tips,
x="day",
hue="smoker",
hue_order=["Yes", "No"]  # smoker first
)

plt.title("Controlled Hue Order")
plt.show()

# --------------------------------------------

# IDEA:

# - ensures consistent comparison

# --------------------------------------------
