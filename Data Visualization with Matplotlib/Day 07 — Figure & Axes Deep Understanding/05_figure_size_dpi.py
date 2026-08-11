import matplotlib.pyplot as plt

"""
FIGURE SIZE + DPI
-----------------
figsize = size of image (width, height)
dpi = resolution (quality)
"""

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

# High quality figure
plt.figure(figsize=(8, 4), dpi=120)

plt.plot(x, y, color="green", linewidth=2)

plt.title("Figure Size & DPI Example")

plt.show()