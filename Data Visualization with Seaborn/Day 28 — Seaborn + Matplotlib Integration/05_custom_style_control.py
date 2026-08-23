# 05_custom_style_control.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# MATPLOTLIB STYLE CONTROL

# --------------------------------------------

plt.style.use("ggplot")

sns.barplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Styled Plot (ggplot style)")
plt.show()

# --------------------------------------------

# IDEA:

# - matplotlib styles change entire look

# --------------------------------------------
