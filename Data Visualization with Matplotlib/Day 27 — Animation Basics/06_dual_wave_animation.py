import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

"""
DUAL WAVE ANIMATION
-------------------
Two waves moving together (signal interference idea)
"""

fig, ax = plt.subplots()

x = np.linspace(0, 2*np.pi, 100)

line1, = ax.plot(x, np.sin(x), label="Wave 1")
line2, = ax.plot(x, np.cos(x), label="Wave 2")

ax.set_ylim(-2, 2)

def update(i):
    line1.set_ydata(np.sin(x + i*0.1))
    line2.set_ydata(np.cos(x + i*0.1))
    return line1, line2

ani = animation.FuncAnimation(
    fig,
    update,
    frames=100,
    interval=50
)

plt.title("Dual Wave Animation")
plt.legend()
plt.show()