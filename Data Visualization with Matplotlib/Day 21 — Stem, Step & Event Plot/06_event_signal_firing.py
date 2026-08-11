import matplotlib.pyplot as plt
import numpy as np

"""
EVENT PLOT FOR SIGNAL FIRING
----------------------------
Used in neuroscience / spike detection
"""

# Simulated neuron firing times
neuron1 = np.sort(np.random.randint(0, 20, 8))
neuron2 = np.sort(np.random.randint(0, 20, 8))
neuron3 = np.sort(np.random.randint(0, 20, 8))

plt.eventplot([neuron1, neuron2, neuron3])

plt.title("Neuron Spike Events")
plt.xlabel("Time")

plt.show()