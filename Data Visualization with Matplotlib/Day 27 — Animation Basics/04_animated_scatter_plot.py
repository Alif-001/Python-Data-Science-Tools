import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

"""
ANIMATED SCATTER PLOT
---------------------
Points move over time.
Used in:
- particle simulation
- ML clustering visualization
"""

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# initial random points
x = np.random.rand(20) * 10
y = np.random.rand(20) * 10

scatter = ax.scatter(x, y)

def update(i):
    global x, y

    # random movement (simulation)
    x += np.random.randn(20) * 0.2
    y += np.random.randn(20) * 0.2

    scatter.set_offsets(np.c_[x, y])
    return scatter,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=100,
    interval=100
)

plt.title("Animated Scatter Plot")
plt.show()