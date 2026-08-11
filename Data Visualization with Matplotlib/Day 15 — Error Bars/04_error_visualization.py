import matplotlib.pyplot as plt

"""
ERROR VISUALIZATION
-------------------
Shows real-world measurement uncertainty.
"""

temperature = [30, 32, 31, 33, 34]
time = [1, 2, 3, 4, 5]

# Measurement error for each point
error = [0.5, 0.8, 0.3, 0.6, 0.7]

plt.errorbar(
    time,
    temperature,
    yerr=error,
    fmt='o',
    capsize=5,
    color="red"
)

plt.title("Temperature Measurement Error")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")

plt.show()