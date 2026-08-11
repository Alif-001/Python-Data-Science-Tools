import matplotlib.pyplot as plt

"""
WATERMARK
---------
Used in reports or dashboards.
"""

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

# Add watermark text
plt.text(
    2.5, 5,
    "CONFIDENTIAL",
    fontsize=30,
    color="gray",
    alpha=0.3,
    rotation=30
)

plt.title("Watermark Example")

plt.show()