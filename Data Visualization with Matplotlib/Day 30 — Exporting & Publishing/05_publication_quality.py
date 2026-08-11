import matplotlib.pyplot as plt
import numpy as np

"""
PUBLICATION QUALITY FIGURE
-------------------------
Used in research papers and professional reports.
"""

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Large figure size for clarity
plt.figure(figsize=(10, 6))

plt.plot(x, y1, label="Sine Wave", linewidth=2)
plt.plot(x, y2, label="Cosine Wave", linewidth=2)

plt.title("Publication Quality Figure", fontsize=14)
plt.xlabel("X axis", fontsize=12)
plt.ylabel("Y axis", fontsize=12)

plt.legend(fontsize=10)
plt.grid(True)

# High-quality export
plt.savefig("publication_quality.png", dpi=300, bbox_inches="tight")

plt.show()