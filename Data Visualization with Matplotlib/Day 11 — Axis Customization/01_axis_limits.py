import matplotlib.pyplot as plt

"""
DAY 11 - AXIS CUSTOMIZATION
--------------------------
We control what part of graph is visible using:
xlim() and ylim()
"""

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y, marker="o")

# Limit X-axis range
plt.xlim(1, 5)

# Limit Y-axis range
plt.ylim(0, 60)

plt.title("Axis Limits Example")

plt.show()