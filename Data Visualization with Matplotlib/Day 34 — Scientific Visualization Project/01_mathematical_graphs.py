import numpy as np
import matplotlib.pyplot as plt

"""
DAY 34 - SCIENTIFIC VISUALIZATION PROJECT
----------------------------------------
We start with mathematical function graphs.
Used in physics, math, ML.
"""

# Create x values (continuous range)
x = np.linspace(-10, 10, 200)

# Different mathematical functions
y1 = x**2              # parabola
y2 = x**3              # cubic curve
y3 = np.sin(x)         # wave function

plt.figure(figsize=(10, 5))

plt.plot(x, y1, label="x²")
plt.plot(x, y2, label="x³")
plt.plot(x, y3, label="sin(x)")

plt.title("Mathematical Graphs")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.legend()
plt.grid(True)

plt.show()