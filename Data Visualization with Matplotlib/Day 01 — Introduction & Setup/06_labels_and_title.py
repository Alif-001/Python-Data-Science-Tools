import matplotlib.pyplot as plt

"""
LABELS & TITLE
--------------
These make graphs understandable
"""

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)

# X-axis label
plt.xlabel("Time")

# Y-axis label
plt.ylabel("Value")

# Graph title
plt.title("Simple Growth Chart")

plt.show()