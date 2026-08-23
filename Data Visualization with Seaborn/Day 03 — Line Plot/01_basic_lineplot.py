# 01_basic_lineplot.py

# --------------------------------------------

# DAY 3: LINE PLOT (TREND VISUALIZATION)

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in dataset

flights = sns.load_dataset("flights")

# Dataset contains:

# year, month, passengers

# --------------------------------------------

# BASIC LINE PLOT

# --------------------------------------------

sns.lineplot(
data=flights,
x="year",
y="passengers"
)

plt.title("Passengers Over Years")
plt.show()

# --------------------------------------------

# WHAT YOU SEE:

# - X axis = time (year)

# - Y axis = value (passengers)

# - Line = trend over time

# --------------------------------------------
