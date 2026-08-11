import matplotlib.pyplot as plt
import numpy as np

"""
PROFESSIONAL DASHBOARD STYLE
---------------------------
Used in real analytics dashboards.
"""

x = np.linspace(0, 10, 100)

plt.figure(figsize=(12, 8))

# Top-left
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), color="blue", label="Sin")
plt.legend()
plt.title("Sin Wave")

# Top-right
plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x), color="red", label="Cos")
plt.legend()
plt.title("Cos Wave")

# Bottom-left
plt.subplot(2, 2, 3)
plt.plot(x, x**2, color="green", label="Square")
plt.legend()
plt.title("Quadratic")

# Bottom-right
plt.subplot(2, 2, 4)
plt.plot(x, np.exp(0.3 * x), color="purple", label="Exp")
plt.legend()
plt.title("Exponential")

plt.tight_layout()

plt.show()