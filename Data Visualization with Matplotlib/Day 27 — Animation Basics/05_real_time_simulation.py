import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

"""
REAL-TIME SIMULATION CONCEPT
----------------------------
We simulate incoming data (like sensors or stock price).
"""

fig, ax = plt.subplots()

x_data = []
y_data = []

line, = ax.plot([], [], lw=2)

ax.set_xlim(0, 50)
ax.set_ylim(0, 100)

def update(i):
    # simulate incoming data
    x_data.append(i)
    y_data.append(np.random.randint(20, 80))

    line.set_data(x_data, y_data)

    return line,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=50,
    interval=100
)

plt.title("Real-Time Simulation (Data Stream)")
plt.show()