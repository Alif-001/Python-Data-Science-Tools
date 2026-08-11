import matplotlib.pyplot as plt
import numpy as np

"""
DAY 26 - ADVANCED LEGENDS & LAYOUT
----------------------------------
Legend = label that explains each line/plot.
We customize legend appearance here.
"""

x = np.linspace(0, 10, 100)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="Sine Wave")
plt.plot(x, y2, label="Cosine Wave")

# Custom legend styling
plt.legend(
    loc="upper right",   # position
    fontsize=10,         # text size
    shadow=True,         # shadow effect
    title="Wave Types"   # legend title
)

plt.title("Custom Legend Example")
plt.grid(True)

plt.show()