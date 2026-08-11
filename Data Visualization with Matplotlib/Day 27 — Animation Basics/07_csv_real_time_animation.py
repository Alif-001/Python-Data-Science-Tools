import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

"""
CSV REAL-TIME ANIMATION
-----------------------
We simulate reading sensor data over time.
"""

time = []
value = []

# Load CSV data
with open("sensor_data_stream.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        time.append(int(row["time"]))
        value.append(int(row["value"]))

fig, ax = plt.subplots()

line, = ax.plot([], [], lw=2)

ax.set_xlim(0, 10)
ax.set_ylim(20, 60)

x_data = []
y_data = []

def update(i):
    # gradually show data like real-time streaming
    x_data.append(time[i])
    y_data.append(value[i])

    line.set_data(x_data, y_data)
    return line,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(time),
    interval=500
)

plt.title("CSV Real-Time Animation")
plt.show()