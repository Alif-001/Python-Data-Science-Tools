import matplotlib.pyplot as plt

"""
BACKGROUND COLOR CONTROL
------------------------
We can style figure background.
"""

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.figure(facecolor="#f0f0f0")  # light gray background

plt.plot(x, y, color="darkblue", linewidth=2)

plt.title("Background Color Example")

plt.show()