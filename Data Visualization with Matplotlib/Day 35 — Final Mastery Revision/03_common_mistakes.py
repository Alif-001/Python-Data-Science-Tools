import matplotlib.pyplot as plt
import numpy as np

"""
COMMON MISTAKES (AND FIXES)
--------------------------
We show wrong vs correct approach.
"""

x = np.arange(1, 6)
y = [10, 20, 15, 25, 30]

plt.figure(figsize=(10, 4))

# ❌ Mistake: no labels, no title
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Bad Plot")

# ✅ Fix: proper labels + clarity
plt.subplot(1, 2, 2)
plt.plot(x, y, marker="o", color="green")
plt.title("Good Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)

plt.tight_layout()
plt.show()