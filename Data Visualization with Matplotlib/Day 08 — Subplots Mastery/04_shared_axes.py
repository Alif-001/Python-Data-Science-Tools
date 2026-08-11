import matplotlib.pyplot as plt

"""
SHARED AXES
-----------
Used when comparing graphs with same scale.
"""

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

# sharex = same X-axis scale
# sharey = same Y-axis scale
fig, ax = plt.subplots(2, 1, sharex=True, figsize=(6, 6))

ax[0].plot(x, y1, color="blue")
ax[0].set_title("Dataset 1")

ax[1].plot(x, y2, color="red")
ax[1].set_title("Dataset 2")

plt.tight_layout()
plt.show()