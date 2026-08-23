# 06_distribution_target_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ml_data.csv")

# --------------------------------------------

# TARGET DISTRIBUTION

# --------------------------------------------

sns.histplot(df["final_score"], kde=True)

plt.title("Final Score Distribution")
plt.show()

# --------------------------------------------

# IDEA:

# - understand target spread

# --------------------------------------------
