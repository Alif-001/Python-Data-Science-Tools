import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

"""
ANIMATED LINE PLOT
------------------
Line moves like a real-time signal.
"""

fig, ax = plt.subplots()

x = np.linspace(0, 4*np.pi, 100)
line, = ax.plot([], [], lw=2)

ax.set_xlim(0, 4*np.pi)
ax.set_ylim(-1, 1)

# Initialize empty line
def init():
    line.set_data([], [])
    return line,

# Update function
def update(i):
    y = np.sin(x + i * 0.1)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(
    fig,
    update,
    init_func=init,
    frames=100,
    interval=50
)

plt.title("Animated Line Plot")
plt.show()