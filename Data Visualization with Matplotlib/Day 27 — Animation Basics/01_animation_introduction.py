import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

"""
DAY 27 - ANIMATION BASICS
-------------------------
Animation = changing plot over time (frame by frame)
Used in:
- real-time graphs
- simulations
- ML training visualization
"""

fig, ax = plt.subplots()

x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))

# This function updates the plot every frame
def update(frame):
    # frame = current animation step
    line.set_ydata(np.sin(x + frame / 10))
    return line,

# Create animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=100,
    interval=50
)

plt.title("Animation Introduction (Sine Wave Motion)")
plt.show()