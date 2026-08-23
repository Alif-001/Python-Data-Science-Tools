# 02_custom_figsize.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# MATPLOTLIB FIGURE CONTROL

# --------------------------------------------

plt.figure(figsize=(10, 6))  # control size

sns.boxplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Custom Figure Size Boxplot")
plt.show()

# --------------------------------------------

# IDEA:

# - matplotlib controls canvas

# --------------------------------------------
