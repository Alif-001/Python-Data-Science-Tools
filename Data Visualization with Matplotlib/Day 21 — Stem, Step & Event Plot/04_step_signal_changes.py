import matplotlib.pyplot as plt
import numpy as np

"""
STEP PLOT FOR STATE CHANGES
---------------------------
Shows sudden changes in values.
"""

time = np.arange(0, 12)

# Example system state (0 = OFF, 1 = ON)
state = [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0]

plt.step(time, state, where="post")

plt.title("System State Changes")
plt.xlabel("Time")
plt.ylabel("State (0/1)")

plt.show()