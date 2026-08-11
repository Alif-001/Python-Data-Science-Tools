import matplotlib.pyplot as plt
import numpy as np

"""
EVENT PLOT
----------
Used to show events happening at specific times.
Example:
- spikes
- neuron firing
- logs
"""

# Each list = events for one category
events = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [1.5, 3.5, 6.5, 9]
]

plt.eventplot(events)

plt.title("Basic Event Plot")
plt.xlabel("Time")

plt.show()