import matplotlib.pyplot as plt
import numpy as np

"""
SUBPLOT LAYOUT
-------------
Multiple plots in one figure.
"""

x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 6))

# 1st plot
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x))
plt.title("Sin")

# 2nd plot
plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x))
plt.title("Cos")

# 3rd plot
plt.subplot(2, 2, 3)
plt.plot(x, x**2)
plt.title("x^2")

# 4th plot
plt.subplot(2, 2, 4)
plt.plot(x, np.log1p(x))
plt.title("log(x+1)")

plt.tight_layout()  # auto spacing fix

plt.show()