# 02_relplot_line.py

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

flights = sns.load_dataset("flights")

# --------------------------------------------

# LINE PLOT USING relplot

# --------------------------------------------

sns.relplot(
data=flights,
x="year",
y="passengers",
kind="line"
)

plt.title("Relplot - Line Plot Example")
plt.show()

# --------------------------------------------

# WHY USE THIS?

# - automatic aggregation

# - cleaner trend visualization

# --------------------------------------------
