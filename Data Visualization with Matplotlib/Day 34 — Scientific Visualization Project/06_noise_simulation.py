import numpy as np
import matplotlib.pyplot as plt

"""
NOISE SIMULATION
---------------
Real-world signals always contain noise.
"""

x = np.linspace(0, 10, 100)

clean_signal = np.sin(x)

noise = np.random.normal(0, 0.3, 100)

noisy_signal = clean_signal + noise

plt.plot(x, clean_signal, label="Clean Signal")
plt.plot(x, noisy_signal, label="Noisy Signal")

plt.title("Signal vs Noise")
plt.legend()
plt.grid(True)

plt.show()