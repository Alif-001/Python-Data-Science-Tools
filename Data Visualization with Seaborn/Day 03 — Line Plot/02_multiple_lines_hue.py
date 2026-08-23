# 02_multiple_lines_hue.py

import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

# --------------------------------------------

# MULTIPLE LINES USING hue

# --------------------------------------------

# We compare passenger trends by month

sns.lineplot(
data=flights,
x="year",
y="passengers",
hue="month"   # each month becomes a line
)

plt.title("Passenger Trends by Month")
plt.legend(bbox_to_anchor=(1.05, 1))  # move legend outside
plt.show()

# --------------------------------------------

# KEY IDEA:

# hue = category split into multiple lines

# --------------------------------------------
