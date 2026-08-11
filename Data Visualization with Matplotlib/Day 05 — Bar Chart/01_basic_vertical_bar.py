import matplotlib.pyplot as plt

"""
DAY 5 - BAR CHART
-----------------
Bar chart is used to compare categories.
Example: sales of different products.
"""

# Categories (X-axis)
products = ["A", "B", "C", "D"]

# Values (Y-axis)
sales = [20, 35, 30, 50]

# Vertical bar chart
plt.bar(products, sales)

plt.title("Basic Vertical Bar Chart")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()