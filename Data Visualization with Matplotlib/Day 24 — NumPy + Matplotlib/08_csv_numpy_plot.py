import numpy as np
import matplotlib.pyplot as plt
import csv

"""
CSV + NUMPY + MATPLOTLIB
------------------------
Real-world simulation data plotting.
"""

time = []
temperature = []

# Read CSV file
with open("temperature_simulation.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        time.append(int(row["time"]))
        temperature.append(int(row["temperature"]))

# Convert to NumPy arrays
x = np.array(time)
y = np.array(temperature)

# Smooth line simulation (interpolation idea)
x_smooth = np.linspace(x.min(), x.max(), 100)
y_smooth = np.interp(x_smooth, x, y)

plt.plot(x, y, "o", label="Original Data")
plt.plot(x_smooth, y_smooth, label="Smooth Curve")

plt.title("Temperature Simulation (CSV + NumPy)")
plt.xlabel("Time")
plt.ylabel("Temperature")

plt.legend()
plt.grid(True)

plt.show()