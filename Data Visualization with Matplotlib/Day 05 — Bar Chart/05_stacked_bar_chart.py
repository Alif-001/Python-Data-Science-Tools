import matplotlib.pyplot as plt

"""
STACKED BAR CHART
------------------
Bars are stacked on top of each other.
Used for total + breakdown visualization.
"""

months = ["Jan", "Feb", "Mar", "Apr"]

online_sales = [30, 40, 50, 60]
offline_sales = [20, 30, 40, 50]

# First layer (bottom)
plt.bar(months, online_sales, label="Online Sales", color="green")

# Second layer (stacked on top)
plt.bar(
    months,
    offline_sales,
    bottom=online_sales,
    label="Offline Sales",
    color="orange"
)

plt.title("Stacked Bar Chart")
plt.legend()

plt.show()