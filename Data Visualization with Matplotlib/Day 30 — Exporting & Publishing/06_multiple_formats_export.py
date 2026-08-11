import matplotlib.pyplot as plt
import numpy as np

"""
MULTIPLE FORMAT EXPORT
----------------------
We save same plot in different formats.
"""

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

plt.title("Multi Format Export")

# Save in different formats
plt.savefig("figure.png")
plt.savefig("figure.pdf")
plt.savefig("figure.jpg", dpi=300)

plt.show()