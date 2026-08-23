# 05_filled_multiple_kde.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# FILLED MULTIPLE KDE

# --------------------------------------------

sns.kdeplot(
data=tips,
x="total_bill",
hue="smoker",   # smoker vs non-smoker
fill=True,
alpha=0.5       # transparency control
)

plt.title("Smoker vs Non-Smoker KDE")
plt.show()

# --------------------------------------------

# KEY IDEA:

# overlap visualization becomes easier

# --------------------------------------------
