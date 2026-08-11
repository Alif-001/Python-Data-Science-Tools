import matplotlib.pyplot as plt

"""
DAY 14 - AREA CHART
-------------------
Area chart = line plot + filled area under curve

Used for:
- trend visualization
- growth tracking
"""

x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 6, 8]

# Fill area under the line
plt.fill_between(x, y, color="skyblue", alpha=0.5)

plt.plot(x, y, color="blue")

plt.title("Basic Area Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()