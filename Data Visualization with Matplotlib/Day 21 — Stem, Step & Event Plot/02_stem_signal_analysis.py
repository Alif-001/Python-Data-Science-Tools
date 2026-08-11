import matplotlib.pyplot as plt
import numpy as np

"""
STEM PLOT FOR SIGNAL ANALYSIS
-----------------------------
Used in DSP (Digital Signal Processing)
"""

t = np.arange(0, 20)

# Simulated signal (wave + noise)
signal = np.sin(t) + np.random.normal(0, 0.2, len(t))

plt.stem(t, signal)

plt.title("Discrete Signal (Stem Plot)")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.show()