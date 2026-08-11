import matplotlib.pyplot as plt
import numpy as np

"""
MULTIPLE LEGENDS
----------------
Sometimes we need separate legend groups.
"""

x = np.linspace(0, 10, 100)

# First group
line1, = plt.plot(x, np.sin(x), label="Sin Wave")

# Second group
line2, = plt.plot(x, np.cos(x), label="Cos Wave")

# First legend
legend1 = plt.legend(handles=[line1], loc="upper right", title="Group 1")
plt.gca().add_artist(legend1)

# Second legend
plt.legend(handles=[line2], loc="lower right", title="Group 2")

plt.title("Multiple Legends Example")
plt.grid(True)

plt.show()