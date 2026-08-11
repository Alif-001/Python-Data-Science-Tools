import matplotlib.pyplot as plt
import numpy as np

"""
BEST PRACTICES IN VISUALIZATION
------------------------------
Clean, readable, professional graphs.
"""

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 5))

# Good practice 1: clear labels
plt.plot(x, y, label="Sine Wave", linewidth=2)

# Good practice 2: grid
plt.grid(True)

# Good practice 3: legend
plt.legend()

# Good practice 4: title + labels
plt.title("Best Practices Example")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()