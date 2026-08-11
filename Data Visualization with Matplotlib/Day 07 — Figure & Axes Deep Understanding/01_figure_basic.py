import matplotlib.pyplot as plt

"""
DAY 7 - FIGURE UNDERSTANDING
----------------------------
Figure = Whole canvas (like a page)
Everything you draw goes inside a figure.
"""

# Create a figure (empty canvas)
plt.figure()

# Simple data
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

# Plot data
plt.plot(x, y)

plt.title("Basic Figure Example")

plt.show()