import matplotlib.pyplot as plt

"""
TICK ROTATION
-------------
Used when labels are long or overlapping
"""

x = ["Very Long Label 1", "Very Long Label 2", "Very Long Label 3"]
y = [10, 20, 30]

plt.bar(x, y)

# Rotate labels for readability
plt.xticks(rotation=45)

plt.title("Tick Rotation Example")

plt.show()