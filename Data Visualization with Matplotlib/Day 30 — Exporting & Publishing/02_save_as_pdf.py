import matplotlib.pyplot as plt
import numpy as np

"""
SAVE AS PDF
-----------
PDF is used for reports, research papers, and printing.
"""

x = np.linspace(0, 10, 100)
y = np.cos(x)

plt.plot(x, y, color="red")

plt.title("Save as PDF Example")
plt.xlabel("X")
plt.ylabel("Y")

# Save as PDF (vector format = high quality)
plt.savefig("plot_graph.pdf")

plt.show()