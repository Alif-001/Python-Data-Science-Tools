import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

"""
FUNCANIMATION BASICS
--------------------
FuncAnimation = core function for animations in matplotlib
"""

fig, ax = plt.subplots()

x = np.linspace(0, 10, 100)
line, = ax.plot(x, np.sin(x))

# Update function (runs repeatedly)
def animate(i):
    # Shift wave over time
    line.set_ydata(np.sin(x + i * 0.1))
    return line,

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=100,
    interval=50
)

plt.title("FuncAnimation Basics")
plt.show()