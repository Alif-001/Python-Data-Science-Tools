import matplotlib.pyplot as plt

"""
DUAL AXIS PLOT
--------------
Two Y-axes in same graph.
Used when units are different.
"""

x = [1, 2, 3, 4, 5]
temperature = [30, 32, 35, 33, 31]
humidity = [60, 65, 70, 75, 80]

fig, ax1 = plt.subplots()

# First axis (Temperature)
ax1.plot(x, temperature, color="red", marker="o")
ax1.set_ylabel("Temperature (°C)", color="red")

# Second axis (Humidity)
ax2 = ax1.twinx()
ax2.plot(x, humidity, color="blue", marker="s")
ax2.set_ylabel("Humidity (%)", color="blue")

plt.title("Dual Axis Plot Example")

plt.show()