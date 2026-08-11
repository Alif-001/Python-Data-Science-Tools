import matplotlib.pyplot as plt

"""
DISTRIBUTION COMPARISON
----------------------
We compare how data spreads.
"""

group1 = [50, 55, 60, 65, 70]
group2 = [40, 45, 50, 55, 60]
group3 = [60, 65, 70, 75, 80]

data = [group1, group2, group3]

plt.boxplot(data)

plt.xticks([1, 2, 3], ["Group 1", "Group 2", "Group 3"])

plt.title("Distribution Comparison")

plt.show()