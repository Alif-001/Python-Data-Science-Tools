import matplotlib.pyplot as plt

"""
CUMULATIVE VISUALIZATION
------------------------
Shows total growth over time.
"""

x = [1, 2, 3, 4, 5]

sales_online = [10, 20, 30, 40, 50]
sales_offline = [5, 10, 15, 20, 25]

# Stack them
plt.stackplot(
    x,
    sales_online,
    sales_offline,
    labels=["Online", "Offline"],
    colors=["blue", "orange"],
    alpha=0.6
)

plt.title("Cumulative Sales Growth")
plt.legend()

plt.show()