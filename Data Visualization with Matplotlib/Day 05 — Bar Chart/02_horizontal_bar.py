import matplotlib.pyplot as plt

"""
HORIZONTAL BAR CHART
--------------------
Used when labels are long or many categories exist.
"""

products = ["A", "B", "C", "D"]
sales = [20, 35, 30, 50]

# Horizontal bar chart
plt.barh(products, sales)

plt.title("Horizontal Bar Chart")
plt.xlabel("Sales")
plt.ylabel("Products")

plt.show()