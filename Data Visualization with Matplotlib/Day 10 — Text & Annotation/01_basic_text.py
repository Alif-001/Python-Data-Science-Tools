import matplotlib.pyplot as plt

"""
DAY 10 - TEXT & ANNOTATION
--------------------------
plt.text() = add simple text on graph
"""

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y, marker="o")

# Add text at a specific position (x, y)
plt.text(2, 20, "Mid Point", fontsize=12, color="red")

plt.title("Basic Text Example")

plt.show()