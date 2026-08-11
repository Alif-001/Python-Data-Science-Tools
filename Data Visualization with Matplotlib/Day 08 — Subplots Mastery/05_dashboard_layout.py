import matplotlib.pyplot as plt

"""
DASHBOARD STYLE VISUALIZATION
-----------------------------
Multiple charts in one screen (like real BI dashboards).
"""

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

fig, ax = plt.subplots(2, 2, figsize=(8, 6))

# Line plot
ax[0, 0].plot(x, y)
ax[0, 0].set_title("Line Chart")

# Bar chart
ax[0, 1].bar(x, y, color="green")
ax[0, 1].set_title("Bar Chart")

# Scatter plot
ax[1, 0].scatter(x, y, color="red")
ax[1, 0].set_title("Scatter Plot")

# Histogram
ax[1, 1].hist(y, bins=4, color="purple")
ax[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()